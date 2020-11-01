from flask import jsonify

from src.com.main.ImageManager.Account import Account
from src.com.main.ImageManager.DataStore import DataStore
from src.com.main.ImageManager.Exceptions import no_user_name, user_not_created


def register_account(user_info):
    data_store = DataStore.get_instance()
    user_name = user_info['user name']
    if data_store.validate_user_name(user_name):
        try:
            account = Account(user_info)
            data_store.add_user(account)
        except Exception as e:
            print(user_info)
            print(e)
            return user_not_created(e)
        resp = jsonify({'message': 'account for {} created'.format(user_info['name'])})
        resp.status_code = 201
        return resp
    else:
        return no_user_name()

