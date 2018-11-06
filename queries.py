from models import *

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.bind = engine

session = session()

def return_christian_bales_roles(session):
    return session.query(Actor).filter(Actor.name == 'Christian Bale').first().roles
    # Return a list of Christian Bale role instances

    # role_objects = session.query(Actor).filter(Actor.name == 'Christian Bale').first().roles
    # return list(map(lambda x: x.character, role_objects))
    # Return a list of Christian Bale role names

def return_catwoman_actors(session):
    return session.query(Role).filter(Role.character == 'Catwoman').first().actors
    #  Return a list of actor instances that have played Catwoman

def return_number_of_batman_actors(session):
    return len(session.query(Role).filter(Role.character == 'Batman').first().actors)
    # Return the number of actors that have played Batman
