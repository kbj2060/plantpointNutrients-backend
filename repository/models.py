from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql import func

Base = declarative_base()

'''
CREATE TABLE user (
 id        INT NOT NULL AUTO_INCREMENT,
 name     VARCHAR(36),
 password    VARCHAR(36),
 type   VARCHAR(36),
 createdAt    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO user(id, name, password, type, createdAt)
VALUES(1, 'waterpump', '1234', 'admin', now());
'''
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(36))
    password = Column(String(36))
    type = Column(String(36))
    createdAt = Column(DateTime, server_default=func.now())

    switches = relationship("Switch", backref ="user")

'''
CREATE TABLE section (
 id        INT NOT NULL AUTO_INCREMENT,
 main     VARCHAR(36),
 sub    VARCHAR(36),
 createdAt    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO section(id, main, sub, createdAt)
VALUES(1, 's1', 'd1', now());
'''
class Section(Base):
    __tablename__ = "section"
    id = Column(Integer, primary_key=True, autoincrement=True)
    main = Column(String(36))
    sub = Column(String(36))
    createdAt = Column(DateTime, server_default=func.now())

'''
CREATE TABLE machine (
 id        INT NOT NULL AUTO_INCREMENT,
 name     VARCHAR(20),
 section_id    int,
 purpose   VARCHAR(50),
 createdAt    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO machine(id, name, section_id, purpose, createdAt)
VALUES(1, 'waterpump', 's1/d1', 'drain', now());
'''
class Machine(Base):
    __tablename__ = "machine"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(36))
    purpose = Column(String(36))
    createdAt = Column(DateTime, server_default=func.now())

    switches = relationship("Switch", backref ="machine")
    report = relationship("Report", backref ="machine")

# '''
# CREATE TABLE sensor (
#  id        INT NOT NULL AUTO_INCREMENT,
#  name     VARCHAR(20),
#  section_id    int,
#  createdAt    DATETIME,
#   PRIMARY KEY(id)
# );

# INSERT INTO sensor(id, name, section_id, createdAt)
# VALUES(1, 'temperature', 's1/d1', now());
# '''
# class Sensor(Base):
#     __tablename__ = "sensor"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(36))
#     section_id = Column(Integer, ForeignKey('section.id'))
#     createdAt = Column(DateTime, server_default=func.now())
    
#     temperature = relationship("Temperature", backref ="sensor")
#     humidity = relationship("Humidity", backref ="sensor")
#     report = relationship("Report", backref ="sensor")

'''
CREATE TABLE switch (
 id        INT NOT NULL AUTO_INCREMENT,
 section_id    int,
 machine_id     int,
 status   int,
 controlledBy_id   int,
 createdAt    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO switch(id, section_id, machine, status, controlledBy_id, createdAt)
VALUES(1, 1, 'waterpump', true, 1, now());
'''
class Switch(Base):
    __tablename__ = "switch"
    id = Column(Integer, primary_key=True, autoincrement=True)
    machine_id = Column(Integer, ForeignKey('machine.id'))
    status = Column(Integer)
    controlledBy_id = Column(Integer, ForeignKey('user.id'))
    createdAt = Column(DateTime, server_default=func.now())

'''
CREATE TABLE temperature (
 id        INT NOT NULL AUTO_INCREMENT,
 section_id    int,
 sensor_id     int,
 value   float,
 createdAt    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO temperature(id, section_id, sensor_id, value, createdAt)
VALUES(1, 's1/d1', 'temperature', 32, now());
'''
class Temperature(Base):
    __tablename__ = "temperature"
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float)
    createdAt = Column(DateTime, server_default=func.now())

'''
CREATE TABLE humidity (
 id        INT NOT NULL AUTO_INCREMENT,
 section_id    int,
 sensor_id     int,
 value   float,
 createdAt    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO humidity(id, section_id, sensor_id, value, createdAt)
VALUES(1, 's1/d1', 'humidity', 32, now());
'''
class Humidity(Base):
    __tablename__ = "humidity"
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float)
    createdAt = Column(DateTime, server_default=func.now())

'''
CREATE TABLE watersupply (
 id        INT NOT NULL AUTO_INCREMENT,
 section_id    int,
 quantity     float,
 createdAt    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO watersupply(id, section_id, value, createdAt)
VALUES(1, 's1/d1', 10, now());
'''
class WaterSupply(Base):
    __tablename__ = "watersupply"
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Float)
    createdAt = Column(DateTime, server_default=func.now())

'''
CREATE TABLE watercycle (
 id        INT NOT NULL AUTO_INCREMENT,
 section_id    int,
 period     int,
 createdAt    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO watercycle(id, section_id, period, createdAt)
VALUES(1, 's1/d1', 3, now());
'''
class WaterCycle(Base):
    __tablename__ = "watercycle"
    id = Column(Integer, primary_key=True, autoincrement=True)
    period = Column(Integer)
    createdAt = Column(DateTime, server_default=func.now())

'''
CREATE TABLE waterspray (
 id        INT NOT NULL AUTO_INCREMENT,
 section_id    int,
 operating_time     int,
 period     int,
 createdAt    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO waterspray(id, section_id, operating_time, period, createdAt)
VALUES(1, 's1/d1', 2, 3, now());
'''
class WaterSpray(Base):
    __tablename__ = "waterspray"
    id = Column(Integer, primary_key=True, autoincrement=True)
    operating_time = Column(Integer)
    period = Column(Integer)
    createdAt = Column(DateTime, server_default=func.now())

'''
CREATE TABLE nutrientsupply (
 id        INT NOT NULL AUTO_INCREMENT,
 section_id    int,
 quantity     float,
 createdAt    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO nutrientsupply(id, section_id, quantity, createdAt)
VALUES(1, 's1/d1', 3, now());
'''
class NutrientSupply(Base):
    __tablename__ = "nutrientsupply"
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Float)
    createdAt = Column(DateTime, server_default=func.now())

'''
CREATE TABLE report (
 id        INT NOT NULL AUTO_INCREMENT,
 section_id    int,
 level     int,
 subject    str,
 solution   str,
 isFixed    bool,
 createdAt    DATETIME,
  PRIMARY KEY(id)
);

INSERT INTO report(id, section_id, level, subject, solution, isFixed, createdAt)
VALUES(1, 's1/d1', 3, 'temperature', '', false, now());
'''
class Report(Base):
    __tablename__ = "report"
    id = Column(Integer, primary_key=True, autoincrement=True)
    machine_id = Column(Integer, ForeignKey('machine.id'))
    level = Column(Integer)
    isFixed = Column(Boolean)
    createdAt = Column(DateTime, server_default=func.now())

