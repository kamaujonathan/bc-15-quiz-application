import json

 

with open("json/history.json") as json_file:  
    data = json.load(json_file)
    for p in data['questions']:
        print('Question: ' +p['number']+" "+ p['text'])
        print('A: ' + p['A'])
        print('B: ' + p['B'])
        print('C: ' + p['C'])
        print('D: ' + p['D'])
        print('')
        answer = input("Answer:")
        if answer == p['ans']:
            print ("You are correct")
        else:
            print ("Wrong Answer! the correct answer is " +p['ans'])

            input("Press enter to continue")

        


