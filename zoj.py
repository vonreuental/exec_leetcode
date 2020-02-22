while True:
  input_msg = input('please input pairs of integers')
  try:
      a = input_msg.split()
      print(int(a[0]) + int(a[1]))
  except:
      break