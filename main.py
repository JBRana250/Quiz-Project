# Component 1
while True:
  name_check = input("Do you want to input a username or not? Input 'y' for yes and 'n' for no: ")
  if name_check == "y":
    username = input("What do you want me to call you?: ")
    print("Hello, {}!".format(username))
    break
  elif name_check == "n":
    break
  else:
    print("Input is invalid, please try again.")
if name_check == "y":
  print("Welcome to my quiz, {}! This quiz will test your python programming skills.".format(username))
elif name_check == "n":
  print("Welcome to my quiz! This quiz will test your python programming skills. There are a total of {} questions in this quiz. Good luck!") 
  # will insert length of quiz later
  