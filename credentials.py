from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
JAWSDB_URL = environ['JAWSDB_URL']

database_attr = JAWSDB_URL.split(':')
JaName = database_attr[3].split('/')[1].rstrip("'")
JaUser = database_attr[1].lstrip('//')
JaPwrd = database_attr[2].split('@')[0]
JaHost = database_attr[2].split('@')[1]
JaPort = 3306