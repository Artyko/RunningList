from flask import jsonify, request, Blueprint
from app.models import Task, TaskSerialization
from app import db


task_routes = Blueprint('task_routes', __name__)


def remove_task(task_id):
    task_to_delete = db.session.query(Task).filter_by(id=task_id).one()
    db.session.delete(task_to_delete)
    db.session.commit()


def add_task(request_data):
    task_to_add = Task(title=request_data.get('title'),
                       author=request_data.get('author'),
                       read=request_data.get('read'))
    db.session.add(task_to_add)
    db.session.commit()


def return_all_tasks():
    query_shema = TaskSerialization(many=True)
    query_results = db.session.query(Task).all()
    serialized_results = query_shema.dump(query_results)
    return serialized_results


def update_day(task_id, payload):
    task_to_update = db.session.query(Task).filter_by(id=task_id)
    task_to_update.update(payload)
    db.session.commit()


def change_true_to_True(data):
    return {key: (True if value == 'true' else False) for key, value in data.items()}


@task_routes.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        add_task(post_data)
        response_object['message'] = 'Book added!'
    elif request.method == 'GET':
        response_object['books'] = return_all_tasks()
    return jsonify(response_object)


@task_routes.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_task(book_id)
        add_task(post_data)
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_task(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


@task_routes.route('/books/day/<book_id>', methods=['POST'])
def single_book_day(book_id):
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        normalized_data = change_true_to_True(post_data)
        update_day(book_id, normalized_data)
    return jsonify(response_object)
