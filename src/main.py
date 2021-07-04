#!/usr/bin/python3

'''
# scopes
$ main create -scope <name>
$ main delete -scope <name>

# developers
$ ID,AUTH_ID= main create -developer -scopes <scope_name> "<scope_mode>,"
$ main create -developer -scopes "users" --modes "read, write"
$ main create -developer -scopes "users" --modes "+rw"

$ 0,1= main update -developer <ID> <AUTH_ID> -scopes --modes "+r" "-r" "+r-w"

$ 0,1= main delete -developer <ID> <AUTH_ID>

$ SCOPES= main fetch -developer <ID> <AUTH_ID>
'''
