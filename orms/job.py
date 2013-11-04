#-*- coding:utf-8 -*-

from engine import mysql_engine,Base
from sqlalchemy import Column, Integer, String

'''
CREATE  TABLE IF NOT EXISTS `duckweed`.`t_jobs` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(100) NULL ,
  `flow_id` MEDIUMTEXT NULL ,
  `cmd` VARCHAR(2000) NULL ,
  `retry` INT NULL ,
  `priority` INT NULL ,
  `exec_dir` VARCHAR(200) NULL ,
  `ip` VARCHAR(20) NULL ,
  `job_type` INT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci

CREATE  TABLE IF NOT EXISTS `duckweed`.`t_job_types` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NULL ,
  `max_process` INT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
'''

class Job(Base):
  __tablename__='t_jobs'
  id=Column(Integer,primary_key=True,autoincrement=True)
  name=Column(String(100))
  flow_id=Column(Integer)
  cmd=Column(String(2000))
  retry=Column(Integer)
  priority=Column(Integer)
  exec_dir=Column(String(200))
  ip=Column(String(20))
  job_type=Column(Integer)
    
  def __init__(self,**args):
    self.__dict__.update(args)


class JobTypes(Base):
  __tablename__='t_job_types'
  id=Column(Integer,primary_key=True)
  name=Column(String(45))
  max_process=Column(Integer)
  
  def __init__(self,**args):
    self.__dict__.update(args)
  
  
class JobDepends(Base):
  __tablename__='t_job_depends'
  id=Column(Integer,primary_key=True)
  deps_id=Column(Integer,primary_key=True)
  
  def __init__(self,**args):
    self.__dict__.update(args)
  

  
