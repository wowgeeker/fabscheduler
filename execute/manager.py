#-*- coding:utf-8 -*- 
import threading
import settings
from utils.log import Logger

class Manager(threading.Thread):
  
  def __init__(self):
    threading.Thread.__init__(self)
    self.max_process=settings.max_process
    self.procedures={}
    self.procedures_lock=threading.Lock()
    self.logger=Logger.getRuntimeLogger()
  
  def new_procedure(self,procedure_id):
    self.procedures_lock.acquire()
    try:
      if procedure_id in self.procedures:
        raise ValueError('procedure #%s already has an instance running. '%procedure_id)
      self.logger.info('\t'.join(self.procedures.keys()))
    except Exception as ex:
      self.logger.error('[Manager] %s'%str(ex))
    finally:
      self.procedures_lock.release()
      
  def run(self):
    pass
  
  