#!/usr/bin/python3

from datastore import Datastore

class Scopes(Datastore):
    NAME=None
    MODES=['read', 'write']

    def __init__(self):
        Datastore.__init__()

    def create(self, name):
        if name is None:
            raise Exception('name is required')

    @staticmethod
    def find(name):
        if name is None:
            raise Exception('name is required')

    def delete(self, name):
        if name is None:
            raise Exception('name is required')
