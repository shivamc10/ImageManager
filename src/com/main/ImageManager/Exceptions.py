from flask import jsonify


@Exception
def user_name_already_exist(user_name):
    resp = jsonify({'message': '{} user name already exists'.format(user_name)})
    resp.status_code = 400
    return resp


@Exception
def user_name_password_not_matched(user_name, password):
    resp = jsonify({'message': 'user name and password does not match'})
    resp.status_code = 400
    return resp


def file_type_not_allowed():
    resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
    resp.status_code = 400
    return resp


def no_file_found():
    resp = jsonify({'message': 'No file part in the request'})
    resp.status_code = 400
    return resp


def no_file_selected():
    resp = jsonify({'message': 'No file selected for uploading'})
    resp.status_code = 400
    return resp


def no_user_name():
    resp = jsonify({'message': 'No user name in request'})
    resp.status_code = 400
    return resp


def user_not_created(error_message):
    resp = jsonify({'message': 'user not created {}'.format(error_message)})
    resp.status_code = 400
    return resp