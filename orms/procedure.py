#-*- coding:utf-8 -*-

from engine import mysql_engine,Base
from sqlalchemy import Column, Integer, String


class Procedure(Base):
  __tablename__='t_precedures'
  id=Column(Integer,primary_key=True,autoincrement=True)
  name=Column(String(100))
  max_process=Column(Integer)
  
  def __init__(self,**args):
    self.__dict__.update(args)  
    
    
class ProcedureObjects(Base):
  __tablename__='t_procedure_objects'
  procedure_id=Column(Integer,primary_key=True)
  object_id=Column(Integer,primary_key=True)
  object_type=Column(Integer,primary_key=True)
  
  def __init__(self,**args):
    self.__dict__.update(args)  
    
class ProcedurDepends:
  __tablename__='t_procedure_depends'
  procedure_id=Column(Integer,primary_key=True)
  object_id=Column(Integer,primary_key=True)
  deps_id=Column(Integer,primary_key=True)
  deps_option=Column(Integer)    
  def __init__(self,**args):
    self.__dict__.update(args)    
    

from engine import session
procedure=Procedure(name='procedure_test',max_process=10)
session.add(procedure)
print procedure.id
session.commit()  