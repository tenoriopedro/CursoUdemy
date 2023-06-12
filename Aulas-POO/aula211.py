## method vs @classmethod vs @ staticmethod
## method - self, metodo de instância
## @classmethod - cls, metodo de classe
## @staticmethod - metodo estatico (sem self, sem cls)


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self,password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        return msg

#c1 = Connection()
c1 = Connection.create_with_auth('Pedro', '1234')
#c1.set_user('Pedro')
#c1.set_password('123')
print(c1.user)
print(c1.password)
print(Connection.log('LOG:'))