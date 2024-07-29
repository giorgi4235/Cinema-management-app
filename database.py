import sqlite3


def create_connection():
    conn = sqlite3.connect('cinema.db')
    return conn


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            genre TEXT NOT NULL,
            release_year INTEGER NOT NULL,
            show_time TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT
        )
    ''')

    conn.commit()
    conn.close()


def add_movie(name, genre, release_year, show_time):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO movies (name, genre, release_year, show_time)
        VALUES (?, ?, ?, ?)
    ''', (name, genre, release_year, show_time))
    conn.commit()
    conn.close()


def get_all_movies():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies')
    movies = cursor.fetchall()
    conn.close()
    return movies


def update_movie(id, name, genre, release_year, show_time):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE movies
        SET name = ?, genre = ?, release_year = ?, show_time = ?
        WHERE id = ?
    ''', (name, genre, release_year, show_time, id))
    conn.commit()
    conn.close()


def delete_movie(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM movies WHERE id = ?', (id,))
    conn.commit()
    conn.close()


def add_customer(name, email, phone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO customers (name, email, phone)
        VALUES (?, ?, ?)
    ''', (name, email, phone))
    conn.commit()
    conn.close()


def get_all_customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    conn.close()
    return customers


def update_customer(id, name, email, phone):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE customers
        SET name = ?, email = ?, phone = ?
        WHERE id = ?
    ''', (name, email, phone, id))
    conn.commit()
    conn.close()


def delete_customer(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM customers WHERE id = ?', (id,))
    conn.commit()
    conn.close()