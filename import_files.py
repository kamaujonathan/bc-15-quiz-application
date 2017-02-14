import json
import os
import re
import sqlite3
file_title = " "
path_to_json = "json"
num = 0
query = {}
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

first_input = input("Type 'quiz list' to see list of all available quizzes: ")
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
        print ("You have chosen "+v)
    
        
        
   
    
        
            
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
        



