def int_input(promp):
    try:
      return int(input(promp))
    except ValueError as e:
      print(e)
      return 0