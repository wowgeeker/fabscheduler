#-*- coding:utf-8 -*-

from engine import mysql_engine,Base
from sqlalchemy import Column, Integer, String


class Executions(Base):
  __tablename__='t_executions'
  id=Column(Integer,primary_key=True,autoincrement=True)
  procedure_id=Column(Integer)
  status=Column(Integer)
  
  def __init__(self,**args):
    self.__dict__.update(args)  



class ExecutionObject(Base):
  __tablename__='t_execution_objects'
  execute_id=Column(Integer,primary_key=True)
  object_id=Column(Integer,primary_key=True)
  status=Column(Integer)
  retry=Column(Integer)
  priority=Column(Integer)
  
  def __init__(self,**args):
    self.__dict__.update(args)  
    