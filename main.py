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
    length_of_quiz = 0
    txtvers_indexzero_n = "Welcome to my quiz! This quiz will test your python programming skills. There are a total of {} questions in this quiz. Good  luck!".format(
        length_of_quiz)
    txtvers_indexzero_y = "Welcome to my quiz, {}! This quiz will test your python programming skills. There are a total of {} questions in this quiz. Good luck!".format(
        username, length_of_quiz)
    text_versions = {
        txtvers_indexzero_n: txtvers_indexzero_y
    }  #list storing different versions of text depending on if user input a username or not
    keys_list_txtvers = list(text_versions)

    def name_check_print(index):
        if name_check == "n":
            print(keys_list_txtvers[index])
        else:
            print(text_versions.get(keys_list_txtvers[index]))

    name_check_print(0)
    # will insert length of quiz later


# ******************************
QuizIntro()

  