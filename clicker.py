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

  def start_clicking(self):
    self.running = True

  def stop_clicking(self):
    self.running = False

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
    run_times = 0
    while self.is_running:
      while self.running and self.record_tracker:
        if self.repeat_times == run_times:
          self.stop_clicking()
          run_times = 0
        record = self.record_tracker.get_current_position()
        mouse.position = record.position
        if record.button:
          mouse.click(record.button)
        time.sleep(record.delay)
        if self.record_tracker.is_last_record():
          time.sleep(self.interval)
          run_times += 1
      time.sleep(0.2)