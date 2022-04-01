#Global functions / variables / collections
def long_input(text):
  print(text, end='')
  return input()

  

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
Questions = {"What type of loop iterates over a sequence?: ":qone_answers, "What function is used to get an input from the user?: ":qtwo_answers, "What symbol is used to assign a variable?: ":qthree_answers, "What brackets indicate a dictionary? Type the brackets directly into the input: ":qfour_answers, "Which type of loop repeats code as long as the condition is true?: ":qfive_answers, "What syntax is often used in exception handling, to try to run a piece of code?":qsix_answers, "What function is used to print text out into the console?: ":qseven_answers, "What symbol is used for multiplication in python?: ":qeight_answers, "What brackets indicate a list? Type the brackets directly into the input: ":qnine_answers, "What error occurs when the user inputs an invalid value type for a function?: ":qten_answers}
length_of_quiz = len(Questions)
# Component 1 ********************
def QuizIntro():
    def get_user():  #gets username if they want
        while True:
            name_check = input(
                "Do you want to input a username or not? Input 'y' for yes and 'n' for no: "
            )
            name_check = name_check.strip().lower()
            if name_check == "y":
                username = input(
                    "What do you want me to call you? Please input username in letters only: "
                )
                username = username.strip()
                if username.isalpha():
                    return (username, name_check)
                else:
                    print("Please input username in letters only.")
            elif name_check == "n":
                username = None
                return (username, name_check)
            else:
                print("Input is invalid, please try again.")

    username_and_name_check = get_user()
    username = username_and_name_check[0]
    name_check = username_and_name_check[
        1]  #if they want user or not ('y' or 'n')
    txtvers_indexzero_n = "Welcome to my quiz! This quiz will test your python programming skills. There are a total of {} questions in this quiz. Good  luck!".format(
        length_of_quiz)
    txtvers_indexzero_y = "Welcome to my quiz, {}! This quiz will test your python programming skills. There are a total of {} questions in this quiz. Good luck!".format(
        username, length_of_quiz)
    text_versions = {
        txtvers_indexzero_n: txtvers_indexzero_y
    }  #dictionary storing different versions of text depending on if user input a username or not
    keys_list_txtvers = list(text_versions)

    def name_check_print(index):
        if name_check == "n":
            print(keys_list_txtvers[index])
        else:
            print(text_versions.get(keys_list_txtvers[index]))

    name_check_print(0)
    # will insert length of quiz later
# Components 2 and 3 **********
def StartQuestions():
  correct_answers = 0
  question_num = 1
  for Question in Questions:
    user_answer = long_input("Question {}: {}".format(question_num, Question))
    user_answer = user_answer.strip().lower()
    answers_list = Questions[Question]
    correct_answer = answers_list[0]
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
    if user_wrong[0] == 1:
      print("You got that wrong, you included a wrong answer in your answer which was '{}'.".format(user_wrong[1]))
    elif correct_answer in user_answer:
      print("Correct!")
      correct_answers = correct_answers + 1
    elif user_wrong[0] == 0:
      print("You got that wrong, the correct answer was {}.".format(correct_answer))
    question_num = question_num + 1

#RUN*PROGRAM******************************
QuizIntro()
StartQuestions()