from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, create_engine
from sqlalchemy.orm import backref, mapper, relation

BASE = declarative_base()
APPNAME = 'TestApp'

class Color(BASE):
  __tablename__ = 'Color'

  color = Column(String)
  ada_id = Column(Integer, primary_key = True)
  name = Column(String)
  Person = relation('Person', secondary='personColorfavorite_colorslist')
  

  def __init__(self, color, name):
    self.color = color
    self.name = name
    

  def __repr__(self):
    repr = ''
    repr += 'color: ' + self.color
    repr += 'ada_id: ' + self.ada_id
    repr += 'name: ' + self.name
    
    return repr

class Person(BASE):
  __tablename__ = 'Person'

  favorite_colors = relation('Color', secondary='personColorfavorite_colorslist')
  age = Column(Integer)
  ada_id = Column(Integer, primary_key = True)
  name = Column(String)
  

  def __init__(self, age, name):
    self.age = age
    self.name = name
    

  def __repr__(self):
    repr = ''
    repr += 'age: ' + self.age
    repr += 'ada_id: ' + self.ada_id
    repr += 'name: ' + self.name
    
    return repr

class PersonColorfavorite_colorslist(BASE):
  __tablename__ = 'personColorfavorite_colorslist'

  favorite_colors_id = Column(Integer, ForeignKey('Color.ada_id'))
  Color = relation(Color, backref=backref('PersonColorfavorite_colorslist'))
  Person_id = Column(Integer, ForeignKey('Person.ada_id'))
  Person = relation(Person, backref=backref('PersonColorfavorite_colorslist'))
  ada_id = Column(Integer, primary_key = True)
  

  def __init__(self):
    pass    

  def __repr__(self):
    repr = ''
    repr += 'ada_id: ' + self.ada_id
    
    return repr

class ColorhashCodeList(BASE):
  __tablename__ = 'ColorhashCodeList'

  Color_id = Column(Integer, ForeignKey('Color.ada_id'))
  Color = relation(Color, backref=backref('ColorhashCodeList'))
  ada_id = Column(Integer, primary_key = True)
  hashCode = Column(String)


  def __init__(self, hashCode):
    self.hashCode = hashCode
    

  def __repr__(self):
    repr = ''
    repr += 'ada_id: ' + str(self.ada_id)
    repr += 'hashCode: ' + self.hashCode
    
    return repr


ENGINE = create_engine('sqlite:///adaDB_TestApp.db', echo=False)
BASE.metadata.create_all(ENGINE)

