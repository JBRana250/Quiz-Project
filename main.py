# Component 1
while True:
  name_check = input("Do you want to input a username or not? Input 'y' for yes and  'n' for no: ")
  name_check = name_check.strip().lower()
  if name_check == "y":
    username = input("What do you want me to call you? Please input username in      letters only: ")
    username = username.strip()
    if username.isalpha():
      print("Hello, {}!".format(username))
      break
    else:
      print("Please input username in letters only.")
  elif name_check == "n":
    break
  else:
    print("Input is invalid, please try again.")
if name_check == "y":
  print("Welcome to my quiz! This quiz will test your python programming skills. There are a total of {} questions in this quiz. Good  luck!") 
elif name_check == "n":
  print("Welcome to my quiz! This quiz will test your python programming skills. There are a total of {} questions in this quiz. Good  luck!") 
  # will insert length of quiz later
  