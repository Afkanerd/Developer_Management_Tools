#!/usr/bin/python3

from datastore import Datastore

class Developer(Datastore):
    ID=None
    AUTH_ID=None
    AUTH_TOKEN=None
    SCOPES=[]

    def __init__(self):
        Datastore.__init__()
        return None

    def create(self, scopes=[]):
        if self.ID is None and self.AUTH_ID is None:
            raise Exception('ID and AUTH_ID cannot be Empty')

    @staticmethod
    def find(ID=None, AUTH_ID=None):
        if ID is None and AUTH_ID is None:
            raise Exception('ID and AUTH_ID cannot be Empty')

    def is_authorized(self, scopes):
        return False

    def update(self, ID=None, AUTH_ID=None):
        if ID is None and AUTH_ID is None:
            raise Exception('ID and AUTH_ID cannot be Empty')

    def delete(self, ID=None, AUTH_ID=None):
        if ID is None and AUTH_ID is None:
            raise Exception('ID and AUTH_ID cannot be Empty')


if __name__ == "__main__":
    dev = Developer()

    '''
    + dev creates scopes
    + scopes are defined with read or write or both

    - database
    # Abstractions
    users:
        users.read
        users.write
    '''
