#-*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Insert

from settings import mysql_profile

@compiles(Insert)
def replace_string(insert, compiler, **kw):
    s = compiler.visit_insert(insert, **kw)
    s = s.replace("INSERT INTO", "REPLACE INTO")
    return s  
  
Base = declarative_base()



class MysqlEngine:
  mysql_engine=None
  session=None
  
  def get_engine(self):
    cls=MysqlEngine
    if cls.mysql_engine is None:
      cls.mysql_engine=create_engine("mysql://{user}:{password}@{host}/{db}?charset=utf8".format(\
                user=mysql_profile['user'],host=mysql_profile['host'],\
                password=mysql_profile['password'],db=mysql_profile['db']),echo=True)
    return self.mysql_engine
  
  def get_session(self):
    cls=MysqlEngine
    if cls.session is None:
      engine=self.get_engine()
      Session=sessionmaker(bind=engine)
      cls.session=Session()         
    return cls.session

mysql_engine=MysqlEngine().get_engine()
session=MysqlEngine().get_session()

