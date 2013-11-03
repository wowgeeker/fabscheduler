#-*- coding:utf-8 -*-
import threading,time
import inspect

from orms.procedure import Procedure
from orms.schedule import Schedule
from orms.engine import session
from utils.log import Logger

class Scheduler(threading.Thread):
  
  def __init__(self,manager):
    threading.Thread.__init__(self)
    self.op_lock=threading.Lock()
    self.sched_procedures={}
    self.manager=manager
    self.logger=Logger.getRuntimeLogger()
    self.init_status=True
    
  def __update(self,procedure):
    self.op_lock.acqure()
    try:
      session.merge(procedure) 
      session.commit()   
      self.sched_procedures[procedure.id]=procedure       
    except Exception as ex:
      self.logger.error('[Scheduler] %s'%str(inspect.trace()))
    finally:
      self.op_lock.release()
  
  def delete(self,procedure_id):
    self.op_lock.acqure()
    try:
      if procedure_id in self.sched_procedures.items():
        session.delete(sched_procedures[procedure_id])        
        session.commit()
        del self.sched_procedures[procedure.id]
    except Exception as ex:
      self.logger.error('[Scheduler] %s'%str(inspect.trace()))      
    finally:
      self.op_lock.release()
  
  def add(self,procedure):    
    self.op_lock.acquire()
    try:
      if procedure.procedure_id in self.sched_procedures.items():
        self.__update(procedure)
      else:
        session.add(procedure)
        session.commit()
        self.sched_procedures[procedure.procedure_id]=procedure
    except Exception as ex:
      self.logger.error('[Scheduler] %s'%str(inspect.trace()))
    finally:
      self.op_lock.release()
    
  def __getsched_procedures(self):
    scheds=session.query(Schedule).all()
    self.sched_procedures=dict(zip([sched.procedure_id for sched in scheds],scheds))    
  
  def __available_procedures(self):
    result=[]
    stamp=int(time.time())
    if not self.init_status:
      for id,p in self.sched_procedures.items():
        if p.next_time<=stamp:
          p.update_nexttime()
          result.append(p)
          session.merge(p)
    else:
      for id,p in self.sched_procedures.items():
        if p.next_time<stamp:
          p.update_nexttime(current=stamp)
          session.merge(p)
          session.commit()
      self.init_status=False 
    return result
  
  def run(self):
    self.__getsched_procedures()
    while True:
      self.op_lock.acquire()
      try:
        avail_scheds=self.__available_procedures()
        if avail_scheds:
          for p in avail_scheds:
            self.manager.new_procedure(p.procedure_id)
      except Exception as ex:
        self.logger.error('[Scheduler] %s'%str(inspect.trace()))
      finally:
        self.op_lock.release()
      time.sleep(1)