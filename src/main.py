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
    group.add_argument("-authenticate", nargs=2, help="authenticate user with <auth_id> against <auth_key>")

    args = parser.parse_args()
    # print(args)

    host='localhost'
    user='root'
    password='asshole'
    database='developers'
    Developers().init_db(host=host, user=user, database=database, password=password)


    if args.create:
        print(f'>> creating dev with scope [{args.create}, {args.scopes}]', end='\n\n')
        try:
            if Developers.create(email=args.create, scopes=args.scopes):
                print('developer created')

        except Exception as error:
            # print(error)
            print(traceback.format_exc())



    elif args.fetch:
        print(f'>> fetching dev with email [{args.fetch}]', end='\n\n')
        try:
            dev = Developers.fetch(email=args.fetch)
            # print(dev)
        except Exception as error:
            print(traceback.format_exc())
        else:
            if dev is not None:
                print(f'email: {dev.email}\nauth_id: {dev.auth_id}\nauth_key: {dev.auth_key}')
        

    elif args.authenticate:
        try:
            auth_id=None
            auth_key=None

            val1 = args.authenticate[0].split('=')
            val2 = args.authenticate[1].split('=')
            if val1[0] == 'auth_id':
                auth_id = val1[1]
                auth_key = val2[1]
            if val1[0] == 'auth_key':
                auth_key = val1[1]
                auth_id = val2[1]
            print(f'>> authenticate user with <auth_id={auth_id}> against <auth_key={auth_key}> for <scopes={args.scopes}>', end='\n\n')
            auth=Developers.authenticate(auth_id=auth_id, auth_key=auth_key, scopes=args.scopes)
        except Exception as error:
            print(traceback.format_exc())
        else:
            if auth:
                print('valid')
            else:
                print('invalid')



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
