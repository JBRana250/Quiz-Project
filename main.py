while True:
  name_check = input("Do you want to input a username     or not? Please type 'y' for yes and 'n' for no: ")
  if name_check == "y":
    print("ok")
    break
  elif name_check == "n":
    print("alr")
    break
  else:
    print("Input is invalid, please try again.")