#!/usr/bin/python3

from datastore import Datastore


class Developer():
    def __init__(self, email, auth_id, auth_key, scopes):
        self.email = email
        self.auth_id = auth_id
        self.auth_key = auth_key
        self.scopes = scopes

class Developers(Datastore):

    @classmethod
    def __init__(cls):
        Datastore().__init__()

    @classmethod
    def create(cls, email, scopes):
        try:
            import uuid
            import hashlib

            auth_key=hashlib.sha256(str(uuid.uuid4().hex).encode('ascii')).hexdigest()
            auth_id=hashlib.sha256(str(uuid.uuid4().hex).encode('ascii')).hexdigest()
            print(f'auth_key={auth_key}, auth_id={auth_id}')
            cls.__add__(email=email, scopes=scopes, auth_id=auth_id, auth_key=auth_key)
        except Exception as error:
            raise Exception(error)


    @classmethod
    def fetch(cls, email):
        try:
            dev = cls.__fetch__(email=email)
            if len(dev) < 1:
                return None
            dev = dev[0]
            return Developer(email=dev['email'], auth_id=dev['auth_id'], auth_key=dev['auth_key'], scopes=dev['scopes'])
        except Exception as error:
            raise Exception(error)
