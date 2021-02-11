from pynput.keyboard import Key, KeyCode
from pynput.keyboard import Listener as KeyboardListener
from clicker import ClickMouse
from recorder import Recorder
from application import Program
from times import Times

start_stop_key = Key.f1
record_key = Key.f2
interval_key = Key.f3
repeat_key = KeyCode(char='r')
exit_key = Key.f4

record_thread = Recorder()
record_thread.start()
click_thread = ClickMouse()
click_thread.start()
times_handler = Times()

def on_press(key):
  if key == start_stop_key:
    if click_thread.running:
      print("Stop")
      click_thread.stop_clicking()
    elif not is_something_running():
      print("Working............................")
      click_thread.start_clicking()
  elif key == record_key:
    if record_thread.recording:
      print("Stop recording")
      record_thread.stop_recording()
      click_thread.set_record_tracker(record_thread.record_tracker)
    elif not is_something_running():
      print("Start recording...........................")
      record_thread.start_recording()
  elif key == interval_key:
    if not is_something_running():
      interval = times_handler.input_interval()
      click_thread.set_interval(interval)
  elif key == repeat_key:
    if not is_something_running():
      amount = times_handler.input_repeat()
      click_thread.set_repeat_times(amount)

  elif key == exit_key:
    print("Goodbye!")
    record_thread.exit()
    click_thread.exit()
    listener.stop()

def is_something_running():
  return click_thread.running or record_thread.recording

with KeyboardListener(on_press=on_press) as listener:
  listener.join()