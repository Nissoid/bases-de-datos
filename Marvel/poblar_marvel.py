Python
import oracledb
import os
import random
from dotenv import load_dotenv

load_dotenv()

USUARIO = os.getenv("DB_USUARIO")
CONTRASENA = os.getenv("DB_CONTRASENA")
DSN = os.getenv("DB_HOST")

# Validacion previa para evitar intentos de conexion fallidos si falta el .env
if not USUARIO or not CONTRASENA or not DSN:
    print("[ERROR] Faltan variables de entorno. Revise el archivo .env.")
    exit(1)


def poblar_marvel():
    print("[INFO] Generando conjunto de datos inicial...")

    # Tuplas base para la generacion
    personajes_base = [
        ("Iron Man", "Tony Stark"), ("Capitan America", "Steve Rogers"), ("Thor", "Thor Odinson"),
        ("Hulk", "Bruce Banner"), ("Viuda Negra", "Natasha Romanoff"), ("Ojo de Halcon", "Clint Barton"),
        ("Spider-Man", "Peter Parker"), ("Lobezno", "Logan"), ("Tormenta", "Ororo Munroe"),
        ("Ciclope", "Scott Summers"), ("Jean Grey", "Jean Grey"), ("Magneto", "Max Eisenhardt"),
        ("Profesor X", "Charles Xavier"), ("Bruja Escarlata", "Wanda Maximoff"), ("Vision", "Vision"),
        ("Pantera Negra", "T'Challa"), ("Doctor Extraño", "Stephen Strange"), ("Capitana Marvel", "Carol Danvers"),
        ("Ant-Man", "Scott Lang"), ("Avispa", "Hope van Dyne"), ("Star-Lord", "Peter Quill"),
        ("Gamora", "Gamora"), ("Drax", "Arthur Douglas"), ("Rocket", "Rocket Raccoon"),
        ("Groot", "Groot"), ("Thanos", "Thanos"), ("Loki", "Loki Laufeyson"),
        ("Ultron", "Ultron"), ("Duende Verde", "Norman Osborn"), ("Doctor Octopus", "Otto Octavius"),
        ("Venom", "Eddie Brock"), ("Carnage", "Cletus Kasady"), ("Deadpool", "Wade Wilson"),
        ("Cable", "Nathan Summers"), ("Domino", "Neena Thurman"), ("Daredevil", "Matt Murdock"),
        ("Punisher", "Frank Castle"), ("Elektra", "Elektra Natchios"), ("Kingpin", "Wilson Fisk"),
        ("Bullseye", "Lester"), ("Luke Cage", "Carl Lucas"), ("Puño de Hierro", "Danny Rand"),
        ("Jessica Jones", "Jessica Jones"), ("Caballero Luna", "Marc Spector"), ("Motorista Fantasma", "Johnny Blaze"),
        ("Blade", "Eric Brooks"), ("Silver Surfer", "Norrin Radd"), ("Galactus", "Galan"),
        ("Doctor Muerte", "Victor Von Doom"), ("Mr. Fantastico", "Reed Richards"), ("Mujer Invisible", "Sue Storm"),
        ("Antorcha Humana", "Johnny Storm"), ("La Cosa", "Ben Grimm"), ("Namor", "Namor McKenzie"),
        ("Rayo Negro", "Blackagar Boltagon"), ("Medusa", "Medusalith Amaquelin"), ("Crystal", "Crystalia Amaquelin"),
        ("Gorgon", "Gorgon Petragon"), ("Karnak", "Karnak Mander-Azur"), ("Triton", "Triton"),
        ("Rondador Nocturno", "Kurt Wagner"), ("Coloso", "Piotr Rasputin"), ("Gatasombra", "Kitty Pryde"),
        ("Picara", "Anna Marie"), ("Gambito", "Remy LeBeau"), ("Bestia", "Hank McCoy"),
        ("Arcangel", "Warren Worthington III"), ("Hombre de Hielo", "Bobby Drake"), ("Emma Frost", "Emma Frost"),
        ("Mistica", "Raven Darkholme"), ("Dientes de Sable", "Victor Creed"), ("Juggernaut", "Cain Marko"),
        ("Sapo", "Mortimer Toynbee"), ("Blob", "Fred Dukes"), ("Pyro", "St. John Allerdyce"),
        ("Avalancha", "Dominikos Petrakis"), ("Hombre Multiple", "Jamie Madrox"), ("Estrella Rota", "Gaveedra-Seven"),
        ("Mancha Solar", "Roberto da Costa"), ("Magik", "Illyana Rasputina"), ("Bala de Cañon", "Sam Guthrie"),
        ("Espejismo", "Dani Moonstar"), ("X-23", "Laura Kinney"), ("Daken", "Akihiro"),
        ("Bucky Barnes", "James Buchanan Barnes"), ("Halcon", "Sam Wilson"), ("Maquina de Guerra", "James Rhodes"),
        ("Nick Furia", "Nicholas J. Fury"), ("Maria Hill", "Maria Hill"), ("Quake", "Daisy Johnson"),
        ("Spider-Gwen", "Gwen Stacy"), ("Miles Morales", "Miles Morales"), ("Kraven", "Sergei Kravinoff"),
        ("Buitre", "Adrian Toomes"), ("Mysterio", "Quentin Beck"), ("Hombre de Arena", "Flint Marko"),
        ("Electro", "Max Dillon"), ("Rino", "Aleksei Sytsevich"), ("Lagarto", "Curt Connors"),
        ("Escorpion", "Mac Gargan")
    ]

    datos_a_insertar = []

    for i, personaje in enumerate(personajes_base):
        id_personaje = i + 1
        alias = personaje[0]
        nombre_real = personaje[1]

        bandos = ["Heroe", "Villano", "Anti-heroe"]

        # Logica basica para clasificar villanos conocidos
        if alias in ["Thanos", "Loki", "Ultron", "Duende Verde", "Doctor Octopus", "Venom", "Carnage", "Doctor Muerte",
                     "Kingpin", "Galactus"]:
            bando = "Villano"
        elif alias in ["Deadpool", "Punisher", "Venom", "Motorista Fantasma", "Caballero Luna", "Mistica"]:
            bando = "Anti-heroe"
        else:
            # Distribucion probabilistica para el resto
            bando = random.choices(bandos, weights=[80, 15, 5], k=1)[0]

        nivel_poder = random.randint(10, 100)
        datos_a_insertar.append((id_personaje, alias, nombre_real, bando, nivel_poder))

    try:
        conexion = oracledb.connect(user=USUARIO, password=CONTRASENA, dsn=DSN)
        cursor = conexion.cursor()

        sql_insert = """
            INSERT INTO marvel_personajes (id_personaje, alias_heroe, nombre_real, bando, nivel_poder) 
            VALUES (:1, :2, :3, :4, :5)
        """

        print(f"[INFO] Ejecutando insercion por lotes ({len(datos_a_insertar)} registros)...")

        # executemany optimiza el rendimiento al enviar todo el bloque en una sola transaccion
        cursor.executemany(sql_insert, datos_a_insertar)
        conexion.commit()

        print("[OK] Base de datos poblada correctamente.")

    except oracledb.DatabaseError as e:
        error_obj, = e.args
        if error_obj.code == 1:
            print("[AVISO] Insercion cancelada. Los registros ya existen (violacion de Primary Key).")
        else:
            print(f"[ERROR] Fallo en la insercion: {e}")

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conexion' in locals(): conexion.close()


if __name__ == "__main__":
    poblar_marvel()