#!/usr/bin/python3
"""
cascade database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    new_state = State(name="California")
    session.add(new_state)

    california = session.query(State).filter(State.name == "California").first()

    new_city = City(name="San Francisco", state_id=california.id)
    session.add(new_city)
    session.commit()
    print("id  name")
    print("{:d}  {:s}".format(california.id, california.name))
    print("id  name    state_id")
    print("{}  {}  {}".format(new_city.id, new_city.name, new_city.state_id))
