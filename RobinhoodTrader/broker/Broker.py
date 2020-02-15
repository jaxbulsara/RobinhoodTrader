class Broker:
    def __init__(self):
        self.session = None

    def addSession(self, session):
        self.session = session

    def removeSession(self):
        self.session = None
