"""
测试Flask
"""
# from flask import Flask, jsonify
from flask_cors import CORS

from flask import Flask, jsonify, request

import uuid

# 配置参数,开启debug模式,json转换中文不使用unicode
DEBUG = True
JSON_AS_ASCII = False

# 实例化Flask
app = Flask(__name__)
app.config.from_object(__name__)

# 开启CORS,解决跨域调用问题
CORS(app, resources={r'/*': {'origins': '*'}})
# 也可以简单直接写CORS(app)


# 配置路由
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!中文!')


BOOKS = [{
    'id': uuid.uuid4().hex,
    'title': 'On the Road',
    'author': 'Jack Kerouac',
    'read': True
}, {
    'id': uuid.uuid4().hex,
    'title': 'Harry Potter and the Philosopher\'s Stone',
    'author': 'J. K. Rowling',
    'read': False
}, {
    'id': uuid.uuid4().hex,
    'title': 'Green Eggs and Ham',
    'author': 'Dr. Seuss',
    'read': True
}]


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def update_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


if __name__ == "__main__":
    app.run()

