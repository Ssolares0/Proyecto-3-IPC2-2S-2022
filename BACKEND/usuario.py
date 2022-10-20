class users:
    def __init__(self, name, apellido, username, email, password):
        self.name = name
        self.apellido = apellido
        self.username = username
        self.email = email
        self.password = password

    def getName(self):
        return self.name

    def getApellido(self):
        return self.apellido

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def setName(self, name):
        self.name = name

    def setApellido(self, apellido):
        self.apellido = apellido

    def setUsername(self, username):
        self.username = username

    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password