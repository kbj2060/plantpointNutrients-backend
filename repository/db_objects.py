from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

'''
CREATE TABLE machine (
 id        INT NOT NULL AUTO_INCREMENT,
 name     VARCHAR(20),
 section    VARCHAR(20),
 purpose   VARCHAR(50),
 created    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO machine(id, name, section, purpose, created)
VALUES(1, 'waterpump', 's1/d1', 'drain', now());
'''
class Machine(Base):
    __tablename__ = "machine"
    id = Column(Integer, primary_key=True)
    name = Column(String(36), nullable=False)
    section = Column(String(36))
    purpose = Column(String(36))
    created = Column(DateTime)

'''
CREATE TABLE sensor (
 id        INT NOT NULL AUTO_INCREMENT,
 name     VARCHAR(20),
 section    VARCHAR(20),
 created    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO sensor(id, name, section, created)
VALUES(1, 'temperature', 's1/d1', now());
'''
class Sensor(Base):
    __tablename__ = "sensor"
    id = Column(Integer, primary_key=True)
    name = Column(String(36), nullable=False)
    section = Column(String(36))
    created = Column(DateTime)
