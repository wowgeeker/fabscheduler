#-*- coding:utf-8 -*-

from engine import mysql_engine,Base
from sqlalchemy import Column, Integer, String


class Flow(Base):
  __tablename__='t_flows'
  id=Column(Integer,primary_key=True,autoincrement=True)
  owner=Column(String(500))
  name=Column(String(45))
  priority=Column(Integer)
  
  def __init__(self,**args):
    self.__dict__.update(args)