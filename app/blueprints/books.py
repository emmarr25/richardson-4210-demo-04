from flask import Blueprint, render_template, request, redirect, url_for
from database import get_connection

books_bp = Blueprint('books', __name__)

@books_bp.route('/books')
def books():
    conn = get_connection()
    cursor = conn.cursor()

    # Get books with author names using JOIN
    cursor.execute('''
        SELECT b.*, a.first_name, a.last_name
        FROM books b
        JOIN authors a ON b.author_id = a.id
        ORDER BY b.title
    ''')
    books = cursor.fetchall()

    # Also get all authors for the dropdown
    cursor.execute('SELECT * FROM authors ORDER BY last_name')
    authors = cursor.fetchall()

    conn.close()
    return render_template('books.html', books=books, authors=authors)

@books_bp.route('/books/add', methods=['POST'])
def add_book():
    conn = get_connection()
    cursor = conn.cursor()

    title = request.form['title']
    author_id = request.form['author_id']
    isbn = request.form['isbn']
    publication_date = request.form['publication_date']
    genre = request.form['genre']
    price = request.form['price']
    description = request.form['description']

    cursor.execute(
        'INSERT INTO books (title, author_id, isbn, publication_date, genre, price, description) VALUES (%s, %s, %s, %s, %s, %s, %s)',
        (title, author_id, isbn, publication_date, genre, price, description)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('books.books'))

@books_bp.route('/books/edit/<int:id>', methods=['POST'])
def edit_book(id):
    conn = get_connection()
    cursor = conn.cursor()

    title = request.form['title']
    author_id = request.form['author_id']
    isbn = request.form['isbn']
    publication_date = request.form['publication_date']
    genre = request.form['genre']
    price = request.form['price']
    description = request.form['description']

    cursor.execute(
        'UPDATE books SET title = %s, author_id = %s, isbn = %s, publication_date = %s, genre = %s, price = %s, description = %s WHERE id = %s',
        (title, author_id, isbn, publication_date, genre, price, description, id)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('books.books'))

@books_bp.route('/books/delete/<int:id>', methods=['POST'])
def delete_book(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM books WHERE id = %s', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('books.books'))
