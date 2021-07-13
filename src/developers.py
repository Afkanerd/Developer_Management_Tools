#!/usr/bin/python3

from datastore import Datastore

class Developers(Datastore):

    @classmethod
    def __init__(cls):
        Datastore().__init__()

    @classmethod
    def create(cls, email, scopes):
        try:
            cls.__add__(email=email, scopes=scopes, auth_id=auth_id, auth_key=auth_key)
        except Exception as error:
            raise Exception(error)

