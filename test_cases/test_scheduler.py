import sys
sys.path.append('../')

from execute.scheduler import Scheduler

from orm.schedule import Schedule
from orm.engine import session

import unittest

class TestScheduler(unittest.TestCase):
  
  def test_scheduletable(self):
    print 'yo'
    