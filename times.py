from utils.input_helper import int_input

class Times():
  def input_interval(self):
    return int_input('Interval time in seconds: ')

  def input_repeat(self):
    return int_input('Total amount of times: ')