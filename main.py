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
Questions = {"What type of loop iterates over a sequence?: ":qone_answers, "What function is used to get an input from the user?: ":qtwo_answers, "What symbol is used to assign a variable?: ":qthree_answers, "What brackets indicate a dictionary? Type the brackets directly into the input: ":qfour_answers, "Which type of loop repeats code as long as the condition is true?: ":qfive_answers, "What syntax is often used in exception handling, to try to run a piece of code?":qsix_answers, "What function is used to print text out into the console?: ":qseven_answers, "What symbol is used for multiplication in python?: ":qeight_answers, "What brackets indicate a list? Type the brackets directly into the input: ":qnine_answers, "What error occurs when the user inputs an invalid value type for a function?: ":qten_answers}
length_of_quiz = len(Questions)

# Component 1 ********************

def quiz_intro():
    def get_user():  #gets username if they want
        while True:  
            name_check = long_input("Do you want to input a username or not? Input 'y' for yes and 'n' for no: ")
            name_check = name_check.strip().lower()

            #if they want username
            if name_check == "y":
                print("")
                username = long_input("What do you want me to call you? Please input username in letters only: ")
                print("")
                username = username.strip()
                if username.isalpha():
                    return (username, name_check)
                else:
                    print("Please input username in letters only.")

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

    txtvers_indexzero_n = "Welcome to my quiz! This quiz will test your python programming skills. There are a total of {} questions in this quiz. Good  luck!".format(length_of_quiz)
    txtvers_indexzero_y = "Welcome to my quiz, {}! This quiz will test your python programming skills. There are a total of {} questions in this quiz. Good luck!".format(username, length_of_quiz)

    #dictionary storing different versions of text depending on if user input a username or not. I used a dictionary in case I need to add more text versions.
    text_versions = {txtvers_indexzero_n: txtvers_indexzero_y} 
  
    keys_list_txtvers = list(text_versions)

    #prints text version depending on if user wanted username or not
    def name_check_print(index):
        if name_check == "n":
            print(keys_list_txtvers[index])
        else:                                    
            print(text_versions.get(keys_list_txtvers[index]))
          
    name_check_print(0)
    print("")
  
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
    
    def check_wrong_answers():
      for answer in answers_list:
        if answer in user_answer:
          user_wrong = 1
          return user_wrong, answer
          break
        user_wrong = 0
        answer = None
        return user_wrong, answer
        
    user_wrong = check_wrong_answers()
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

#RUN*PROGRAM******************************

def run_quiz():
  quiz_intro()
  correct_answers = start_questions() #get num of correct ans
