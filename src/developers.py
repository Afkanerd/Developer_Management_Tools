#!/usr/bin/python3

from datastore import Datastore

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

