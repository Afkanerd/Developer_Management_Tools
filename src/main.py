#!/usr/bin/python3

'''
$ main create --scope [read, write, +rw]

# creates users with default scope 'read'
$ main create <name>


$ main delete -scope <name>

# developers
$ ID,AUTH_ID= main create -developer -scopes <scope_name> "<scope_mode>,"
$ main create -developer -scopes "users" --modes "read, write"
$ main create -developer -scopes "users" --modes "+rw"

$ 0,1= main update -developer <ID> <AUTH_ID> -scopes --modes "+r" "-r" "+r-w"

$ 0,1= main delete -developer <ID> <AUTH_ID>

$ SCOPES= main fetch -developer <ID> <AUTH_ID>
'''

from developers import Developers, Developer

if __name__ == "__main__":

    import argparse
    import traceback

    parser = argparse.ArgumentParser(description="cli args")
    parser.add_argument("--scopes", help="Read (can fetch only), Write (can write and update)", default='read', const='read', choices=['read', 'write', '+rw'], nargs='?')
    group = parser.add_argument_group('Actions', '')
    group.add_argument("-create", help="create user with <email address> [--scopes]")
    group.add_argument("-delete", help="delete user with <email address>")
    group.add_argument("-update", help="update user with <email address> [--scopes]")
    group.add_argument("-fetch", help="fetch user with  <email address>")

    args = parser.parse_args()
    print(args)

    host='localhost'
    user='root'
    password='asshole'
    database='developers'
    Developers().init_db(host=host, user=user, database=database, password=password)
    if args.create:
        print(f'>> creating dev with scope [{args.create}, {args.scopes}]')
        try:
            if Developers.create(email=args.create, scopes=args.scopes):
                print('developer created')

        except Exception as error:
            # print(error)
            print(traceback.format_exc())
    elif args.fetch:
        print(f'>> fetching dev with email [{args.fetch}]')
        try:
            dev = Developers.fetch(email=args.fetch)
            # print(dev)
        except Exception as error:
            print(traceback.format_exc())
        else:
            if dev is not None:
                print(f'\nemail: {dev.email}\nauth_id: {dev.auth_id}\nauth_key: {dev.auth_key}')
        
    else:
        parser.print_help()

    '''
    elif args.fetch:
        print(f'>> fetching dev with email [{args.create}]')

    elif args.update:
        print(f'>> updating dev with scope [{args.scopes}]')
    elif args.delete:
        print(f'>> deleting dev [{args.delete}]')
    '''
