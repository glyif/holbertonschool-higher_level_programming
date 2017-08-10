#!/usr/bin/env python3


import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{:s}:{:s}@localhost/{:s}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(engine)
    session = Session()

    data = session.query(State).filter(
            State.name == sys.argv[4].split(' ')[0].split(';')[0]).first()
    if data:
        print(data.id)
    else:
        print("Nothing")
