#-*- coding:utf-8 -*-

from engine import mysql_engine,Base
from sqlalchemy import Column, Integer, String


class Job(Base):
  __tablename__='t_jobs'
  id=Column(Integer,primary_key=True,autoincrement=True)
  name=Column(String(100))
  flow_id=Column(Integer)
  owners=Column(String(500))
  cmd=Column(String(2000))
  retry=Column(Integer)
  priority=Column(Integer)
    
  def __init__(self,**args):
    self.__dict__.update(args)


class JobDepends(Base):
  __tablename__='t_job_depends'
  id=Column(Integer,primary_key=True)
  deps_id=Column(Integer,primary_key=True)
  
  def __init__(self,**args):
    self.__dict__.update(args)
  

  
