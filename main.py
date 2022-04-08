#Global functions / variables / collections

#Repl has bug which breaks long inputs, this fixes.
def long_input(text):
  print(text, end='')
  return input()
  
#right and wrong answers for each question, first string is right answer and following strings are wrong answers.
qone_answers = ["for", "while"]
qtwo_answers = ["input", "print"]
qthree_answers = ["=", "=="]
qfour_answers = ["{}", "[]", "()"]
qfive_answers = ["while", "for"]
qsix_answers = ["try", "except"]
qseven_answers = ["print", "input"]
qeight_answers = ["*", "x"]
qnine_answers = ["[]", "{}", "()"]
qten_answers = ["value", "syntax"]

#questions collection, needed in global since length of quiz is needed as global.
Questions = {"What type of loop iterates over a sequence?: ":qone_answers, "What function is used to get an input from the user?: ":qtwo_answers, "What symbol is used to assign a variable?: ":qthree_answers, "What brackets indicate a dictionary? Type the brackets directly into the input: ":qfour_answers, "Which type of loop repeats code as long as the condition is true?: ":qfive_answers, "What syntax is often used in exception handling, to try to run a piece of code?: ":qsix_answers, "What function is used to print text out into the console?: ":qseven_answers, "What symbol is used for multiplication in python?: ":qeight_answers, "What brackets indicate a list? Type the brackets directly into the input: ":qnine_answers, "What error occurs when the user inputs an invalid value type for a function?: ":qten_answers}
length_of_quiz = len(Questions)

# for when I need to update certain placeholders inside a dictionary that stores different versions of text depending on if the user wanted a username or not.
def format_text_versions(length_of_quiz, username, correct_answers):
  txtvers_indexzero_n = "Welcome to my quiz! This quiz will test your python programming skills. There are a total of {} questions in this quiz. Good  luck!".format(length_of_quiz)
  txtvers_indexzero_y = "Welcome to my quiz, {}! This quiz will test your python programming skills. There are a total of {} questions in this quiz. Good luck!".format(username, length_of_quiz)
  txtvers_indexone_n = "You got {} answer(s) right.".format(correct_answers)
  txtvers_indexone_y = "Congratulations, {}! You got {} answer(s) correct.".format(username, correct_answers)
  text_versions = {txtvers_indexzero_n: txtvers_indexzero_y, txtvers_indexone_n: txtvers_indexone_y}
  return text_versions

# this function prints out a version of text depending on if the user wanted a username or not, using an updated_text_versions dictionary.
def name_check_print(name_check, keys_list_txtvers, updated_text_versions, index):
  if name_check == "n":                        
    print(keys_list_txtvers[index])
  else:                                                print(updated_text_versions.get(keys_list_txtvers[index]))

#this is needed in global for it to work when the user tries again
def check_wrong_answers(answers_list, user_answer):
  for answer in answers_list:
    if answer in user_answer:
      user_wrong = 1
      return user_wrong, answer
  user_wrong = 0
  answer = None
  return user_wrong, answer
  
# Component 1 ********************

def quiz_intro():
    def get_user():  #gets username if they want
        while True:  
            name_check = long_input("Do you want to input a username or not? Input 'y' for yes and 'n' for no: ")
            name_check = name_check.strip().lower()

            #if they want username
            if name_check == "y":
                print("")
                while True:
                  username = long_input("What do you want me to call you? Please input username in letters only: ")
                  username = username.strip()
                  if username.isalpha():
                    print("")  
                    return (username, name_check)
                    
                  else:
                    print("Please input username in letters only.")
                    print("")

            #if they dont want username
            elif name_check == "n":
                print("")
                username = None
                return (username, name_check)

            #if user input is not 'y' or 'n'
            else:
                print("Input is invalid, please try again.")
                print("")

    #getting username and name_check from get_user()
    username_and_name_check = get_user()
    username = username_and_name_check[0]
    name_check = username_and_name_check[1]   
    correct_answers = None
  
    updated_text_versions = format_text_versions(length_of_quiz, username, correct_answers)
    keys_list_txtvers = list(updated_text_versions)

          
    name_check_print(name_check, keys_list_txtvers, updated_text_versions, 0)
    print("")
    return name_check, keys_list_txtvers, username
  
# Components 2 and 3 **********
def start_questions():
  correct_answers = 0
  question_num = 1
  for Question in Questions:

    #prints question num, then prints question and gets user's input
    user_answer = long_input("Question {}: {}".format(question_num, Question))
    
    user_answer = user_answer.strip().lower()
    answers_list = Questions[Question] #get right n wrong ans
    correct_answer = answers_list[0]

    #gets rid of right answer from ans list, only wrong answers remain
    answers_list.pop(0)
        
    user_wrong = check_wrong_answers(answers_list, user_answer)
    print(user_wrong)
    
    if user_wrong[0] == 1: #if user include wrong answer
      print("You got that wrong, you included a wrong answer in your answer which was '{}'.".format(user_wrong[1]))
      print("")
    elif correct_answer in user_answer: #if user include correct ans
      print("Correct!")
      print("")
      correct_answers = correct_answers + 1
    elif user_wrong[0] == 0: #if user did not include any ans from list
      print("You got that wrong, the correct answer was {}.".format(correct_answer))
      print("")
    question_num = question_num + 1
  return(correct_answers)

# Component 4 *****************
def print_correct_answers(name_check, keys_list_txtvers, correct_answers, username):
  updated_text_versions = format_text_versions(length_of_quiz, username, correct_answers)
  keys_list_txtvers = list(updated_text_versions)
  
  name_check_print(name_check, keys_list_txtvers, updated_text_versions, 1)
  print("")
#RUN*PROGRAM******************************
quiz_intro_variables = quiz_intro()
name_check = quiz_intro_variables[0]
keys_list_txtvers = quiz_intro_variables[1]
username = quiz_intro_variables[2]

def run_quiz():
  correct_answers = start_questions()
  print_correct_answers(name_check, keys_list_txtvers, correct_answers, username)

#Component 5 ***************************
def loop_run_quiz():
  while True:
    run_quiz()
    while True:
      rerun_check = input("Do you want to try again? Input 'y' if yes, input 'n' if no: ")
      if rerun_check == "y":
        print("")
        break
      elif rerun_check == "n":
        break
      else:
        print("Input invalid, please try again")
        print("")
    if rerun_check == "n":
      break

loop_run_quiz()
    
