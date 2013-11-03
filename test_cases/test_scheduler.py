import sys
sys.path.append('../')

from execute.scheduler import Scheduler
from execute.manager import Manager

from orms.schedule import Schedule
from orms.engine import session

import unittest

class TestScheduler(unittest.TestCase):
  
  def test_scheduletable(self):
    session.merge(Schedule(procedure_id=1,last_time=1383456861,next_time=1383466861,span=300))
    session.commit()

  def test_scheduler_add(self):
    manager=Manager()
    scheduler=Scheduler(manager)
    scheduler.start()
  
unittest.main()