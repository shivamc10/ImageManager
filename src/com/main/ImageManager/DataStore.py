class DataStore:
    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if DataStore.__instance is None:
            DataStore()
        return DataStore.__instance

    def __init__(self):
        if DataStore.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DataStore.__instance = self
        self.__accountMap = dict()
        self.accountCount = 0

    def validate_user_name(self, user_name):
        if user_name in self.__accountMap.keys():
            return False
        return True

    def add_user(self, account):
        self.__accountMap[account.user_name] = account

    def get_user(self, user_name):
        return self.__accountMap[user_name]

    def show_user(self):
        resp = {'users':[]}
        for k,v in self.__accountMap.items():
            resp['users'].append(k)
        return resp


    def validate_user(self, user_name, password):
        if user_name in self.__accountMap.keys():
            return self.__accountMap[user_name].validate_pass(password)
        return False
