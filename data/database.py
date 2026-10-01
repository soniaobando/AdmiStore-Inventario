import sqlite3

DATABASE_NAME = "admystore.db"


def get_connection():
    """Crea y devuelve una conexión con la base de datos."""
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():
    """Crea la tabla productos si todavía no existe."""
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            stock_minimo INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()