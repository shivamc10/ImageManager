class Account:

    def __init__(self, user_info):
        self.name = user_info['name']
        self.email = user_info['email'] if 'email' in user_info.keys() else None
        self.user_name = user_info['user name']
        self.accountNo = user_info['accountNo'] if 'accountNo' in user_info.keys() else None
        self.__pass = user_info['password']
        self.__Images = []

    def getImages(self):
        return self.__Images

    def validate_pass(self,password):
        return self.__pass == password

    def add_image(self, file):
        self.__Images.append(file)


