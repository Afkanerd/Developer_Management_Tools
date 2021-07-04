#!/usr/bin/python3

class Developer(Datastore):
    ID=None
    AUTH_ID=None
    AUTH_TOKEN=None
    SCOPES=[]

    def __init__(self):
        Datastore.__init__()

    # CRUD
    def create(self, scopes=[]):
        if self.ID is None and self.AUTH_ID is None:
            raise Exception('ID and AUTH_ID cannot be Empty')

    @staticmethod
    def find(ID=None, AUTH_ID=None):
        if ID is None and AUTH_ID is None:
            raise Exception('ID and AUTH_ID cannot be Empty')

    def update(self, ID=None, AUTH_ID=None):
        if ID is None and AUTH_ID is None:
            raise Exception('ID and AUTH_ID cannot be Empty')


    def delete(self, ID=None, AUTH_ID=None):
        if ID is None and AUTH_ID is None:
            raise Exception('ID and AUTH_ID cannot be Empty')
