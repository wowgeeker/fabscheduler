#-*- coding:utf-8 -*- 
import threading
import settings
from utils.log import Logger
from orms.job import Job,JobTypes,JobDepends
from orms.engine import session
from orms.execution import ExecutionStatus,Execution



class Manager(threading.Thread):
  
  def __init__(self):
    threading.Thread.__init__(self)
    self.max_process=settings.max_process
    self.procedures={}
    self.procedures_lock=threading.Lock()
    self.logger=Logger.getRuntimeLogger()    
    self.op_lock=threading.Lock()
    self.producer_event=threading.Event()
    self.job_types=JobTypeManager(self.op_lock)
    self.status_manager=StatusManager(self)
    self.max_process=settings.max_process
     
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
  
  
class JobTypeManager():
  
  def __init__(self,lock):
    self.lock=lock
    self.__load_job_types()
    
  def __load_job_types(self):
    l_job_types=session.query(JobTypes).all()
    self.jobtypes=dict(zip([job_type.id for job_type in l_job_types],l_job_types))    
  
  def new(self,job_type):
    pass
  
  def update(self,job_type):
    pass
  
  def delete(self,job_type):
    pass
  
  def get(self,job_type_id):
    pass

class StatusManager():
  
  def __init__(self,boss):
    self.boss=boss
  
  def __availables(self):
    pass
  
  def get_execution(self):
    self.boss.op_lock.acquire()
    availables=self.__availables()
    if not availables:
      self.boss.producer_event.clear()
      self.boss.op_lock.release()
      self.boss.producer_event.wait()
    self.boss.op_lock.acquire()
    availables=self.__availables() 
    execution=None   
    for a in availables:
      if execution:
        if a.priority>execution.priority:
          execution=a
      else:
        execution=a
    execution.status=ExecutionStatus.READY   
    self.boss.op_lock.release() 
    return execution
  
    
      
    
     
  
  