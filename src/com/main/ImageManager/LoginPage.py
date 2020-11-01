from src.com.main.ImageManager.DataStore import DataStore
from flask import jsonify


def show_home_page(user_name):
    data_store = DataStore.get_instance()
    account = data_store.get_user(user_name)
    image_list = account.getImages()
    resp = {'image list': list()}
    for image in image_list:
        resp['image list'].append(image)

    resp = jsonify(resp)
    resp.status_code = 201
    return resp