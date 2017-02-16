"""
- creating the JSON files with each containing a quiz
	- add keys (questions, text and options)
	- for options, indicate whether the option is correct or not using is_answer
- create class
- create functions
score out of questions he got right
adding timing as a parameter in the JSON file
import quizes from JSON files
"""

import json
import os
import re
import sqlite3
import command_list
import time
import signal
from terminaltables import AsciiTable


class quizApp:  # initialize an instance of the class

    def __init__(self):

        """ constructor of the class """

    def check_command(self, cmd_check, enter_name):  # function that checks if the command is correct

        if re.match("quiz list", cmd_check):
            self.check_for_quiz_list(cmd_check, enter_name)
        else:
            print ('That is not a valid input!')

            cmd_check = raw_input("\nType Command: ")

        while not re.match("quiz list", cmd_check):
            print ('That is not a valid input!')
            try:
                cmd_check = raw_input("\nType Command: ")

            except TypeError:
                print ('That is not a valid input!')


    def check_input(self):  # function that validates name input and calls the check_command function
        enter_name = raw_input("\nEnter your name: ")


        while not all(x.isalpha() or x.isspace() for x in enter_name):
            print("\nThat is not a valid input!\n")
            enter_name = raw_input("Enter your name: ")

        else:
            self.insert_table(enter_name)
            cmd_check = raw_input("\nType Command: ")

            self.check_command(cmd_check, enter_name)

    """def countdown(self,time):
        s = 0
        while True:
            mins = 5
            secs = 20
            #mins, secs = divmod(int(s), time)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            sleep(1)
            time -= 1
        print('Goodbye!\n\n\n\n\n')"""

    """def countdown(self,time):
        print('Time Left : {}s'.format(t))
        time.sleep(t)"""

    def initialize_database(self):  # initializes the sqlite database
        sqlite_file = 'quiz_db.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        conn.commit()
        conn.close()

    def create_table(self):  # creates tables on the database
        sqlite_file = 'quiz_db.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE quiz(id INTEGER PRIMARY KEY, user TEXT, quiz_name TEXT,
                       test_score INTEGER, number_questions INTEGER)''')

    def insert_table(self, enter_name):  # inserts data into the table created
        sqlite_file = 'quiz_db.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('''INSERT INTO quiz(user)
                  VALUES (?)''', (enter_name,))
        conn.commit()
        conn.close()

    def update_table(self, enter_name, quiz_name, test_score,
                     number_questions):  # updates table with data from the quiz being done
        sqlite_file = 'quiz_db.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('''UPDATE quiz SET quiz_name = ?, test_score = ?, number_questions = ? WHERE user = ? ''',
                  (quiz_name, test_score, number_questions, enter_name))
        conn.commit()
        conn.close()

    def select_from_table(self, enter_name, quiz_name, test_score, number_questions):  # selects data from table

        sqlite_file = 'quiz_db.sqlite'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        c.execute('''SELECT * FROM quiz WHERE user = ?''', (enter_name,))
        for row in c:
            table_data = [
                ['NAME', row[1]],
                ['QUIZ NAME', row[2]],
                ['TEST SCORE', row[3]],
                ['NUMBER OF QUESTIONS', row[4]]
            ]

        table = AsciiTable(table_data)
        print (table.table)
        conn.commit()
        conn.close()

    def check_for_quiz_list(self, cmd_check, enter_name):  # checks for availability of quiz files
        path_to_json = "json"
        num = 0
        query = {}

        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        first_input = input("Press enter to see list of all available quizzes: ")
        for num, files in enumerate(json_files, 1):
            file_name = os.path.splitext(files)
            query[int(num)] = "," + file_name[0]

            if re.match("quiz list", cmd_check):

                print (num, str.title(file_name[0]))
            else:
                print ('Quiz not available!')

                while not re.match("quiz list", cmd_check):
                    print ('That is not a valid input!')
                try:
                    exit_cmd = ("Type 'exit' to leave the program")
                    if exit_cmd == 'exit':
                        exit(0)

                except TypeError:
                    print ('That is not a valid input!')

        self.check_what_is_chosen(query, enter_name)

    def check_what_is_chosen(self, query, enter_name):  # allows user to choose the quiz he/she would like to do
        number_questions = 0
        test_score = 0
        quiz_choice = raw_input('Enter the number of the quiz you would like to do: ')

        for k, v in query.items():
            if (k == int(quiz_choice)):
                quiz_name = v
                quiz_name = quiz_name.replace(',', '')
                print ("You have chosen " + str.title(quiz_name))
                self.check_for_quiz_take(quiz_name, enter_name, test_score, number_questions)

    def check_for_quiz_take(self, quiz_name, enter_name, test_score, number_questions):  # allows useer to take the quiz
        data = ' '

        # test = 1
        second_input = raw_input("Type 'quiz take' to take the quiz: ")
        if re.match("quiz take", second_input):
            with open("json/" + quiz_name + ".json") as json_file:
                data = json.load(json_file)
            for p in data['questions']:

                # self.countdown(time)
                number_questions = int(p['number'])
                print('Question ' + p['number'] + " :" + p['text'])
                print('A: ' + p['A'])
                print('B: ' + p['B'])
                print('C: ' + p['C'])
                print('D: ' + p['D'])
                print('')

                answer = raw_input("Answer:").upper()


                """time.sleep(5)
                if answer == "":
                    continue"""

                if re.match("[A-Da-d]", answer):
                    correct_message = 'You are correct'
                    if answer == p['ans']:

                        test_score += 1
                        print (correct_message)

                        self.update_table(enter_name, quiz_name, test_score, number_questions)
                    elif answer != p['ans']:
                        print ("Wrong Answer! the correct answer is " + p['ans'])
                        raw_input("Press enter to continue")

                elif not re.match("[A-Da-d]", answer):
                    print ('That is not a valid input!')
                    answer = raw_input("Give your answer: ").upper()
                    correct_message = 'You are correct'
                    if answer == p['ans']:
                        test_score += 1
                        print (correct_message)

                        self.update_table(enter_name, quiz_name, test_score, number_questions)
                    while not re.match("[A-Da-d]", answer):
                        print ('That is not a valid input!')
                    else:
                        correct_message = 'You are correct'
                        if answer == p['ans']:
                            test_score += 1
                            print (correct_message)

                            self.update_table(enter_name, quiz_name, test_score, number_questions)





        elif re.match("quiz take", second_input):
            print ('That is not a valid input!')
            second_input = raw_input("Type 'quiz take' to take the quiz: ")
            while not re.match("quiz list", second_input):
                print ('That is not a valid input!')
                try:
                    second_input = raw_input("Type 'quiz take' to take the quiz: ")
                except TypeError:
                    print ('That is not a valid input!')
        print ("You have reached the end of Quiz")
        raw_input("\n\nPress enter to view results")
        self.select_from_table(enter_name, quiz_name, test_score, number_questions)





obj = quizApp()
obj.check_input()


