#-*- coding:utf-8 -*-
import logging
import os,sys

from settings import log_path


class Logger:
  
  @staticmethod
  def getRuntimeLogger():
    logger = logging.getLogger('runtime')
    logger.setLevel(logging.INFO)
    exec_dir=os.path.abspath(log_path)
    file=os.path.join(exec_dir,'runtime.log')
    if not os.path.exists(exec_dir):os.makedirs(exec_dir)
    if not os.path.exists(file):open(file,'w').close()    
    print >>sys.stderr,file
    fh=logging.FileHandler(file)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)    
    return logger
 
  @staticmethod
  def getJobLogger(exec_id,job_id):
    logger = logging.getLogger('exec_%s_%s'%(exec_id,jobname))
    logger.setLevel(logging.INFO)
    path=os.path.abspath(log_path)
    exec_dir=os.path.join(path,'exec_%s'%exec_id)
    file=os.path.join(exec_dir,'%s.log'%jobname)
    if not os.path.exists(exec_dir):os.makedirs(exec_dir)
    if not os.path.exists(file):open(file,'w').close()
    fh=logging.FileHandler(file)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)        
    return logger   

