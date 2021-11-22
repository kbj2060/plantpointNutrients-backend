from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# It is important to understand that this is not the class we are using in the business logic,
# but the class that we want to map into the SQL database.
# The structure of this class is thus dictated by the needs of the storage layer, and not by the use cases.

# Obviously, this means that you have to keep the storage
# and the domain levels in sync and that you need to manage migrations on your own.


class Machine(Base):
    __tablename__ = "machine"
    id = Column(Integer, primary_key=True)
    name = Column(String(36), nullable=False)
    section = Column(String(36))
    purpose = Column(String(36))

class Sensor(Base):
    __tablename__ = "sensor"
    id = Column(Integer, primary_key=True)
    name = Column(String(36), nullable=False)
    section = Column(String(36))
