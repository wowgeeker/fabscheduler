#-*- coding:utf-8 -*-
import threading,time
from orms.procedure import Procedure,Schedule
from orms.engine import session

class Scheduler(threading.Thread):
  
  def __init__(self,manager):
    threading.Thread(self)
    self.op_lock=threading.Lock()
    self.sched_procedures={}
    self.manager=manager
    
  def update(self,procedure):
    self.op_lock.acqure()
    self.sched_procedures[procedure.id]=procedure    
    self.op_lock.release()
  
  def delete(self,procedure_id):
    self.op_lock.acqure()
    if procedure.id in self.sched_procedures:
      del self.sched_procedures[procedure.id]
    self.op_lock.release()
  
  def add(self,procedure):    
    self.op_lock.acquire()
    if procedure.id in self.sched_procedures:
      raise ValueError('procedure #%s is already scheduled'%procedure.id)
    else:
      self.sched_procedures[procedure.id]=procedure
    self.op_lock.release()
    
  def __getshed_procedures(self):
    
    pass
  
  def __available_procedures(self):
    return []
  
  def __update_status(self):
    pass
  
  def run(self):
    self.__getshed_procedures()
    while True:
      time.sleep(0.5)
      self.op_lock.acquire()
      available=self.__available_procedures()
      for p in available:
        if self.manager.has_procedure(p):
          continue
        self.manager.new_procedure(p)
      self.__update_status(available)
      self.op_lock.release()