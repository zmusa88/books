import csv
from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)

# load data
with open('books.csv') as f:
    reader = csv.DictReader(f)
    books = list(reader)

# redirect to /books
@app.route('/')
def index():
    return redirect(url_for('get_all_books'))

# get all books
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify({'books': books})

# return book by book id
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = None
    for b in books:
        if int(b['id']) == book_id:
            book = b
            break
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book)

# get all titles
@app.route('/books/title', methods=['GET'])
def get_title():
    titles = [b['title'] for b in books]
    return jsonify({'titles': titles})

# lookup by book title
@app.route('/books/title/<string:title>', methods=['GET'])
def get_book_by_title(title):
    book = None
    for b in books:
        if b['title'].lower().replace(' ', '') == title.lower().replace(' ', ''):
            book = b
            break
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
