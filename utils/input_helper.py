def int_input(promp):
    try:
      return int(input(promp))
    except ValueError:
      return 0