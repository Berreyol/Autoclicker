import threading
import time
from application import Program
from pynput.mouse import Listener as MouseListener

class Record():
  def __init__(self, position, button, delay):
    self.position = position
    self.button = button
    self.delay = delay

class RecordTracker():
  def __init__(self):
    self.records = []
    self.position = -1
  
  def add_record(self, record):
    self.records.append(record)    

  def is_last_record(self):
    return self.position == len(self.records)-1

  def get_current_position(self):
    if self.records:
      self.position += 1
      if self.position == len(self.records):
        self.position = 0
      return self.records[self.position]

class Recorder(threading.Thread, Program):
  def __init__(self):
    super(Recorder, self).__init__()
    self.recording = False
    self.record_tracker = None
    self.start_time = 0

  def stop_recording(self):
    self.recording = False

  def start_recording(self):
    self.recording = True
    self.record_tracker = RecordTracker()
    self.start_time = time.time()

  def exit(self):
    self.stop_recording()
    self.is_running = False

  def run(self):
    def create_record(x,y, button=None):
        end_time = time.time()
        total_time = end_time - self.start_time
        record = Record((x,y), button, total_time)
        self.record_tracker.add_record(record)
        self.start_time = end_time

    def on_click(x, y, button, pressed):
      if not self.recording:
        return False
      if pressed:
        create_record(x, y, button)
        
    def on_move(x, y):
      if not self.recording:
        return False
      create_record(x, y)

    while self.is_running:
      while self.recording:
        with MouseListener(
              on_click=on_click,
              on_move=on_move) as listener:
          listener.join()
      time.sleep(0.1)




