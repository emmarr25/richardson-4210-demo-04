from flask import Blueprint, render_template, request, redirect, url_for
from database import get_connection

authors_bp = Blueprint('authors', __name__)

@authors_bp.route('/authors')
def authors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM authors ORDER BY last_name')
    all_authors = cursor.fetchall()
    conn.close()
    return render_template('authors.html', authors=all_authors)

@authors_bp.route('/authors/add', methods=['POST'])
def add_author():
    conn = get_connection()
    cursor = conn.cursor()

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    nationality = request.form['nationality']
    biography = request.form['biography']

    cursor.execute(
        'INSERT INTO authors (first_name, last_name, date_of_birth, nationality, biography) VALUES (%s, %s, %s, %s, %s)',
        (first_name, last_name, date_of_birth, nationality, biography)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('authors.authors'))

@authors_bp.route('/authors/edit/<int:id>', methods=['POST'])
def edit_author(id):
    conn = get_connection()
    cursor = conn.cursor()

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    nationality = request.form['nationality']
    biography = request.form['biography']

    cursor.execute(
        'UPDATE authors SET first_name = %s, last_name = %s, date_of_birth = %s, nationality = %s, biography = %s WHERE id = %s',
        (first_name, last_name, date_of_birth, nationality, biography, id)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('authors.authors'))

@authors_bp.route('/authors/delete/<int:id>', methods=['POST'])
def delete_author(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM authors WHERE id = %s', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('authors.authors'))
