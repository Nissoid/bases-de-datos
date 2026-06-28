import oracledb
import os
import random
from dotenv import load_dotenv

# Cargamos las credenciales del archivo .env
load_dotenv()
USUARIO = os.getenv("DB_USUARIO")
CONTRASENA = os.getenv("DB_CONTRASENA")
DSN = os.getenv("DB_HOST")

if not USUARIO or not CONTRASENA or not DSN:
    print("❌ Error crítico: Faltan credenciales en el archivo .env.")
    exit(1)


def poblar_marvel():
    print("Preparando el Multiverso Marvel...")

    # Lista base de 100 personajes de Marvel (Alias y Nombre Real)
    personajes_base = [
        ("Iron Man", "Tony Stark"), ("Capitán América", "Steve Rogers"), ("Thor", "Thor Odinson"),
        ("Hulk", "Bruce Banner"), ("Viuda Negra", "Natasha Romanoff"), ("Ojo de Halcón", "Clint Barton"),
        ("Spider-Man", "Peter Parker"), ("Lobezno", "Logan"), ("Tormenta", "Ororo Munroe"),
        ("Cíclope", "Scott Summers"), ("Jean Grey", "Jean Grey"), ("Magneto", "Max Eisenhardt"),
        ("Profesor X", "Charles Xavier"), ("Bruja Escarlata", "Wanda Maximoff"), ("Visión", "Visión"),
        ("Pantera Negra", "T'Challa"), ("Doctor Extraño", "Stephen Strange"), ("Capitana Marvel", "Carol Danvers"),
        ("Ant-Man", "Scott Lang"), ("Avispa", "Hope van Dyne"), ("Star-Lord", "Peter Quill"),
        ("Gamora", "Gamora"), ("Drax", "Arthur Douglas"), ("Rocket", "Rocket Raccoon"),
        ("Groot", "Groot"), ("Thanos", "Thanos"), ("Loki", "Loki Laufeyson"),
        ("Ultrón", "Ultrón"), ("Duende Verde", "Norman Osborn"), ("Doctor Octopus", "Otto Octavius"),
        ("Venom", "Eddie Brock"), ("Carnage", "Cletus Kasady"), ("Deadpool", "Wade Wilson"),
        ("Cable", "Nathan Summers"), ("Domino", "Neena Thurman"), ("Daredevil", "Matt Murdock"),
        ("Punisher", "Frank Castle"), ("Elektra", "Elektra Natchios"), ("Kingpin", "Wilson Fisk"),
        ("Bullseye", "Lester"), ("Luke Cage", "Carl Lucas"), ("Puño de Hierro", "Danny Rand"),
        ("Jessica Jones", "Jessica Jones"), ("Caballero Luna", "Marc Spector"), ("Motorista Fantasma", "Johnny Blaze"),
        ("Blade", "Eric Brooks"), ("Silver Surfer", "Norrin Radd"), ("Galactus", "Galan"),
        ("Doctor Muerte", "Victor Von Doom"), ("Mr. Fantástico", "Reed Richards"), ("Mujer Invisible", "Sue Storm"),
        ("Antorcha Humana", "Johnny Storm"), ("La Cosa", "Ben Grimm"), ("Namor", "Namor McKenzie"),
        ("Rayo Negro", "Blackagar Boltagon"), ("Medusa", "Medusalith Amaquelin"), ("Crystal", "Crystalia Amaquelin"),
        ("Gorgon", "Gorgon Petragon"), ("Karnak", "Karnak Mander-Azur"), ("Tritón", "Triton"),
        ("Rondador Nocturno", "Kurt Wagner"), ("Coloso", "Piotr Rasputin"), ("Gatasombra", "Kitty Pryde"),
        ("Pícara", "Anna Marie"), ("Gambito", "Remy LeBeau"), ("Bestia", "Hank McCoy"),
        ("Arcángel", "Warren Worthington III"), ("Hombre de Hielo", "Bobby Drake"), ("Emma Frost", "Emma Frost"),
        ("Mística", "Raven Darkholme"), ("Dientes de Sable", "Victor Creed"), ("Juggernaut", "Cain Marko"),
        ("Sapo", "Mortimer Toynbee"), ("Blob", "Fred Dukes"), ("Pyro", "St. John Allerdyce"),
        ("Avalancha", "Dominikos Petrakis"), ("Hombre Múltiple", "Jamie Madrox"), ("Estrella Rota", "Gaveedra-Seven"),
        ("Mancha Solar", "Roberto da Costa"), ("Magik", "Illyana Rasputina"), ("Bala de Cañón", "Sam Guthrie"),
        ("Espejismo", "Dani Moonstar"), ("X-23", "Laura Kinney"), ("Daken", "Akihiro"),
        ("Bucky Barnes", "James Buchanan Barnes"), ("Halcón", "Sam Wilson"), ("Máquina de Guerra", "James Rhodes"),
        ("Nick Furia", "Nicholas J. Fury"), ("Maria Hill", "Maria Hill"), ("Quake", "Daisy Johnson"),
        ("Spider-Gwen", "Gwen Stacy"), ("Miles Morales", "Miles Morales"), ("Kraven", "Sergei Kravinoff"),
        ("Buitre", "Adrian Toomes"), ("Mysterio", "Quentin Beck"), ("Hombre de Arena", "Flint Marko"),
        ("Electro", "Max Dillon"), ("Rino", "Aleksei Sytsevich"), ("Lagarto", "Curt Connors"),
        ("Escorpión", "Mac Gargan")
    ]

    # Generamos los datos completos para insertar
    datos_a_insertar = []

    for i, personaje in enumerate(personajes_base):
        id_personaje = i + 1  # Los IDs irán del 1 al 100
        alias = personaje[0]
        nombre_real = personaje[1]

        # Asignamos bando de forma un poco aleatoria (o lógica basándonos en si es villano conocido)
        bandos = ["Héroe", "Villano", "Anti-héroe"]
        # Truco: Si el nombre suena a villano o lo es (por simplificar, hacemos un random con pesos)
        if alias in ["Thanos", "Loki", "Ultrón", "Duende Verde", "Doctor Octopus", "Venom", "Carnage", "Doctor Muerte",
                     "Kingpin", "Galactus"]:
            bando = "Villano"
        elif alias in ["Deadpool", "Punisher", "Venom", "Motorista Fantasma", "Caballero Luna", "Mística"]:
            bando = "Anti-héroe"
        else:
            # 80% héroes, 15% villanos, 5% anti-héroes para el resto
            bando = random.choices(bandos, weights=[80, 15, 5], k=1)[0]

        # Nivel de poder del 1 al 100
        nivel_poder = random.randint(10, 100)

        # Guardamos la tupla (Debe coincidir EXACTAMENTE con el orden del INSERT)
        datos_a_insertar.append((id_personaje, alias, nombre_real, bando, nivel_poder))

    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        # Usamos :1, :2, etc. como siempre
        sql_insert = """
            INSERT INTO marvel_personajes (id_personaje, alias_heroe, nombre_real, bando, nivel_poder) 
            VALUES (:1, :2, :3, :4, :5)
        """

        print(f"Insertando {len(datos_a_insertar)} personajes en la base de datos...")

        # EXECUTEMANY: La forma profesional de hacer inserciones masivas
        cursor.executemany(sql_insert, datos_a_insertar)

        # Confirmamos los cambios
        conexion.commit()

        print("✅ ¡El Multiverso ha sido creado! 100 personajes añadidos correctamente.")

    except oracledb.DatabaseError as e:
        error_obj, = e.args
        if error_obj.code == 1:  # Error de ID duplicado (Unique Constraint Violated)
            print("⚠️ Los personajes ya existen en la base de datos (Error de ID duplicado).")
        else:
            print(f"❌ Error al insertar datos en Oracle: {e}")

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()


if __name__ == "__main__":
    poblar_marvel()