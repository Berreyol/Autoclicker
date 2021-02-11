import threading
import time
from application import Program
from pynput.mouse import Controller
from copy import deepcopy

mouse = Controller()

class ClickMouse(threading.Thread, Program):
  def __init__(self):
    super(ClickMouse, self).__init__()
    self.record_tracker = []
    self.running = False
    self.interval = 0
    self.repeat_times = 1
    self.run_times = 0

  def start_clicking(self):
    self.running = True

  def stop_clicking(self):
    self.running = False
    self.run_times = 0

  def exit(self):
    self.stop_clicking()
    self.is_running = False

  def set_record_tracker(self, record_tracker):
    self.record_tracker = record_tracker
  
  def set_interval(self, interval):
    self.interval = interval

  def set_repeat_times(self, repeat_times):
    self.repeat_times = repeat_times

  def run(self):
    def is_repeat_time_over():
      return self.repeat_times == self.run_times

    def execute_record(record):
      mouse.position = record.position
      if record.button:
        mouse.click(record.button)
      execute_delay(record.delay)

    def execute_delay(delay):
      time.sleep(delay)
        
    while self.is_running:
      while self.running and self.record_tracker:
        if is_repeat_time_over():
          self.stop_clicking()
        record = self.record_tracker.get_current_position()
        execute_record(record)
        if self.record_tracker.is_last_record():
          execute_delay(self.interval)
          self.run_times += 1
      time.sleep(0.2)



