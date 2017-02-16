import json
import os
import re
import sqlite3

file_title = " "
path_to_json = "json"
num = 0
query = {}
test_score = 0
def initialize_database():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    conn.commit()
    conn.close()

def create_tables():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE quiz(id INTEGER PRIMARY KEY, user TEXT, quiz_name TEXT,
                       test_score INTEGER, number_questions INTEGER)
''')
    
def insert_table():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE quiz(id INTEGER PRIMARY KEY, user TEXT, quiz_name TEXT,
                       test_score INTEGER, number_questions INTEGER)
''')
    cursor.execute('''INSERT INTO quiz(user, quiz_name, test_score, number_questions)
                  VALUES(?,?,?,?)''', (enter_name, str.title(quiz_name), test_score, number_questions))





def is_answer(answer):
    if answer == p['ans']:
        return ("You are correct")
        test_score =+ 1
        
    else:
        return ("Wrong Answer! the correct answer is " +p['ans'])
        input("Press enter to continue")
        
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
enter_name = input("Enter your name: ")
first_input = input("Type 'quiz list' to see list of all available quizzes: ")
initialize_database()
create_tables()
for num, files in enumerate(json_files, 1):
    file_name = os.path.splitext(files)
    query[int (num)] =","+file_name[0]
    
    #print (num, str.title(file_name[0]))
    if re.match ("quiz list", first_input):
        
        print (num, str.title(file_name[0]))
    else:
        print ('That is not a valid input!')
        first_input = input("Type 'quiz list' to see list of all available quizzes: ")
        while not re.match ("quiz list", first_input):
            print ('That is not a valid input!')
            try:
                first_input = input("Type 'quiz list' to see list of all available quizzes: ")
            except TypeError:
                print ('That is not a valid input!')

quiz_choice = input('Enter the number of the quiz you would like to do: ')

for k, v in query.items():
    if (k == int(quiz_choice)):
        quiz_name = v
        quiz_name = quiz_name.replace(',', '')
        print ("You have chosen "+str.title(quiz_name))

second_input = input("Type 'quiz take' to take the quiz: ")
if re.match ("quiz take", second_input):
    with open("json/"+quiz_name+".json") as json_file:
        data = json.load(json_file)

        for p in data['questions']:
            number_questions = p['number'] 
            print('Question: ' +p['number']+" "+ p['text'])
            print('A: ' + p['A'])
            print('B: ' + p['B'])
            print('C: ' + p['C'])
            print('D: ' + p['D'])
            print('')
            answer = input("Answer:").upper()
            if re.match ("[A-Da-d]", answer):
                is_answer(answer)
                print (number_questions)
                
            else:
                print ('That is not a valid input!')
                answer= input("Give your answer: ").upper()
                is_answer(answer)
                while not re.match ("[A-Da-d]", answer):
                    print ('That is not a valid input!')
                    try:
                        answer= input("Give your answer: ").upper()
                        is_answer(answer)
                    except TypeError:
                        print ('That is not a valid input!')
                
else:
    print ('That is not a valid input!')
    second_input = input("Type 'quiz take' to take the quiz: ")
    while not re.match ("quiz list", first_input):
        print ('That is not a valid input!')
    try:
        second_input = input("Type 'quiz take' to take the quiz: ")
    except TypeError:
        print ('That is not a valid input!')




    
        
        
    
        
        
   
    
        
            
"""if (k is quiz_choice):
          print ("You have chosen "+v)
        else:
            print ('That quiz is not available. please try again')
            quiz_choice = input('Enter the number of the quiz you would like to do: ')

else:
    print ('That is not a valid input!')
    quiz_choice = input('Enter the number of the quiz you would like to do:')

            
   while (num == quiz_choice):
        print ("You have chosen "+str.title(file_name[0]))
else:
    print ('That is not a valid input!')
    quiz_choice = input('Enter the number of the quiz you would like to do: ')
    
    
        
                    
    else:
        print ('That is not a valid input!')
        quiz_choice = input('Enter the number of the quiz you would like to do: ')
        while not re.match ("quiz list", first_input):
            print ('That is not a valid input!')
            try:
                quiz_choice = input('Enter the number of the quiz you would like to do: ')
            except TypeError:
                print ('That is not a valid input!')"""
    
        
        
            
"""for num, files in enumerate(json_files, 1):
    file_name = os.path.splitext(files)   
    quiz_choice = input('Enter the number of the quiz you would like to do: ')
    
    if quiz_choice == num:
        print ("You have chosen " +str.title(file_name[0]))
    else:
        print("Quiz is not available, please try again")

    #file_title = file_name[0]"""
        



