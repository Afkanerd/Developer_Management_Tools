#!/usr/bin/python3

'''
$ main create -scope <name>
$ main delete -scope <name>

$ ID,AUTH_ID= main create -developer -scopes <scope_name> "<scope_mode>,"
$ main create -developer -scopes "users" --modes "read, write"
$ main create -developer -scopes "users" --modes "+rw"

$ main update -developer <ID> <AUTH_ID> -scopes --modes "+r" "-r" "+r-w"

$ main delete -developer <ID> <AUTH_ID>
'''
