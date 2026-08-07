document.addEventListener('DOMContentLoaded', () => {

    const formulario = document.getElementById('formulario-busqueda');
    const buscador = document.getElementById('buscador');
    const btnLimpiar = document.getElementById('btn-limpiar');
    const cuerpoTabla = document.getElementById('cuerpo-tabla');
    
    const filtroBando = document.getElementById('filtro-bando');
    const filtroOrden = document.getElementById('filtro-orden');

    // Variable global para almacenar los datos traídos de la API
    let datosCargados = [];

    // Función encargada de traer los datos (si no están ya cargados)
    async function realizarBusqueda() {
        try {
            // Si aún no hemos pedido los datos a la API, hacemos el fetch
            if (datosCargados.length === 0) {
                const url = `http://localhost:8000/api/marvel/personajes`;
                const respuesta = await fetch(url);

                if (!respuesta.ok) {
                    throw new Error(`Error en el servidor: Status ${respuesta.status}`);
                }

                const datosAPI = await respuesta.json();
                
                if (Array.isArray(datosAPI)) {
                    datosCargados = datosAPI;
                } else if (typeof datosAPI === 'object' && datosAPI !== null) {
                    datosCargados = [datosAPI];
                } else {
                    datosCargados = [];
                }
            }

            // Aplicar filtros y pintar resultados
            procesarYRenderizar();

        } catch (error) {
            console.error("Detalle del error:", error);
            cuerpoTabla.innerHTML = `
                <tr>
                    <td colspan="5" style="color: #ff5252; text-align: center; padding: 20px;">
                        ⚠️ Error al conectar con la API en Python. Verifica que el servidor esté activo.
                    </td>
                </tr>`;
        }
    }

    // --- EVENTO 1: BÚSQUEDA AL PULSAR ENTER O BUSCAR ---
    formulario.addEventListener('submit', (evento) => {
        evento.preventDefault(); 
        realizarBusqueda();
    });

    // --- EVENTOS DE RE-FILTRADO AUTOMÁTICO AL CAMBIAR SELECTS ---
    filtroBando.addEventListener('change', () => {
        if (datosCargados.length > 0) {
            procesarYRenderizar();
        } else {
            realizarBusqueda();
        }
    });

    filtroOrden.addEventListener('change', () => {
        if (datosCargados.length > 0) {
            procesarYRenderizar();
        } else {
            realizarBusqueda();
        }
    });

    // Función principal para filtrar, ordenar y renderizar los datos
    function procesarYRenderizar() {
        if (datosCargados.length === 0) return;

        const textoBuscado = buscador.value.trim().toLowerCase();
        const bandoSeleccionado = filtroBando.value;
        const ordenSeleccionado = filtroOrden.value;

        // 1. Filtrar por texto (si está vacío, muestra todos)
        let resultados = datosCargados.filter(personaje => {
            if (!textoBuscado) return true;
            const alias = (personaje.alias_heroe || '').toLowerCase();
            const nombreReal = (personaje.nombre_real || '').toLowerCase();
            return alias.includes(textoBuscado) || nombreReal.includes(textoBuscado);
        });

        // 2. Filtrar por Bando (Héroe / Villano)
        if (bandoSeleccionado !== 'todos') {
            resultados = resultados.filter(personaje => {
                const bando = (personaje.bando || '').toLowerCase();
                if (bandoSeleccionado === 'heroe') {
                    return bando.includes('héroe') || bando.includes('heroe');
                } else if (bandoSeleccionado === 'villano') {
                    return bando.includes('villano');
                }
                return true;
            });
        }

        // 3. Ordenar resultados
        resultados.sort((a, b) => {
            if (ordenSeleccionado === 'alias-az') {
                return (a.alias_heroe || '').localeCompare(b.alias_heroe || '');
            } else if (ordenSeleccionado === 'alias-za') {
                return (b.alias_heroe || '').localeCompare(a.alias_heroe || '');
            } else if (ordenSeleccionado === 'poder-desc') {
                return (b.nivel_poder || 0) - (a.nivel_poder || 0);
            } else if (ordenSeleccionado === 'poder-asc') {
                return (a.nivel_poder || 0) - (b.nivel_poder || 0);
            }
            return 0;
        });

        // 4. Si no hay resultados tras los filtros
        if (resultados.length === 0) {
            cuerpoTabla.innerHTML = `
                <tr>
                    <td colspan="5" class="sin-resultados">
                        No se encontraron personajes que coincidan con los criterios seleccionados.
                    </td>
                </tr>`;
            return;
        }

        // 5. Renderizar filas en la tabla
        cuerpoTabla.innerHTML = "";
        resultados.forEach(personaje => {
            const fila = document.createElement('tr');

            const esHeroe = (personaje.bando || '').toLowerCase().includes('héroe') || (personaje.bando || '').toLowerCase().includes('heroe');
            const claseBando = esHeroe ? 'bando-heroe' : 'bando-villano';

            fila.innerHTML = `
                <td><strong>#${personaje.id_personaje}</strong></td>
                <td><strong style="color: #fff;">${personaje.alias_heroe}</strong></td>
                <td style="color: #aaa;">${personaje.nombre_real || 'Desconocido'}</td>
                <td><span class="bando-tag ${claseBando}">${personaje.bando}</span></td>
                <td style="font-weight: bold; color: var(--hero-gold);">${personaje.nivel_poder} pts</td>
            `;

            cuerpoTabla.appendChild(fila);
        });
    }

    // --- EVENTO 2: BOTÓN DE LIMPIAR ---
    btnLimpiar.addEventListener('click', () => {
        buscador.value = "";
        filtroBando.value = "todos";
        filtroOrden.value = "alias-az";
        datosCargados = [];
        limpiarTabla("Realiza una búsqueda para mostrar los personajes.");
        buscador.focus();
    });

    function limpiarTabla(mensaje) {
        cuerpoTabla.innerHTML = `
            <tr>
                <td colspan="5" class="estado-inicial">${mensaje}</td>
            </tr>`;
    }
});