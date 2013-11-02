#-*- coding:utf-8 -*-

from engine import mysql_engine,Base
from sqlalchemy import Column, Integer, String
import datetime


class Schedule(Base):
  
  __tablename__='t_schedule'
  procedure_id=Column(Integer,primary_key=True)
  last_time=Column(Integer)
  next_time=Column(Integer)
  repeat=Column(Integer)
  span=Column(Integer)
  
  def __init__(self,**args):
    self.__dict__.update(args)  