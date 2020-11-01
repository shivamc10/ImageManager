import os
from functools import wraps

from werkzeug.utils import secure_filename
from flask import request, Response
from flask import Flask, jsonify
from flask import make_response
from src.com.main.ImageManager.DataStore import DataStore
from src.com.main.ImageManager.Exceptions import user_name_password_not_matched, no_file_found, no_file_selected, \
    file_type_not_allowed
from src.com.main.ImageManager.LoginPage import show_home_page
from src.com.main.ImageManager.Register import register_account

UPLOAD_FOLDER = './uploads'
app = Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def home():
    return "<h1>Login/Register</h1><p>This site is a prototype API for managing images for different users.</p>"


def authentication(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        user_name = request.args.get('user name')
        password = request.args.get('password')
        data_store = DataStore.get_instance()
        if not user_name or not password or not data_store.validate_user(user_name, password):
            return Response('Login!', 401, {'WWW-Authenticate': 'Basic realm="Login!"'})
        return f(*args, **kwargs)

    return wrapper


@authentication
@app.route('/login', methods=['GET'])
def login():
    return show_home_page(request.args.get('user name'))


@app.route('/register', methods=['POST'])
def register():
    user_info = request.get_json()
    return register_account(user_info)


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@authentication
@app.route('/upload', methods=['POST'])
def upload_image():
    user_name = request.args.get('user name')
    if 'file' not in request.files.keys():
        return no_file_found()
    file = request.files['file']
    if file.filename == '':
        no_file_selected()
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD FOLDER"], filename)
        file.save(filepath)
        data_store = DataStore.get_instance()
        account = data_store.get_user(user_name)
        account.add_image(filepath)
        resp = jsonify({'message': 'File successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        return file_type_not_allowed()


@app.route('/show_user', methods=["GET"])
def get_all_user():
    data_store = DataStore.get_instance()
    resp = data_store.show_user()
    resp = jsonify(resp)
    resp.status_code = 201
    return resp


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    dataStore = DataStore.get_instance()
    app.run()
