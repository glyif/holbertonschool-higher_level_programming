#!/usr/bin/python3
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{:s}:{:s}@localhost/{:s}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(state.id, state.name))
        for city in session.query(City). \
                join(State). \
                filter(City.state_id == state.id). \
                order_by(City.id):
            print("\t{:d}: {:s}".format(city.id, city.name))
