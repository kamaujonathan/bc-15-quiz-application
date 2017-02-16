import sys
sys.path.insert(5,'C:\\Users\\JONATHAN\\Desktop\\quiz_app\\quiz\\Lib\\site-packages')
from terminaltables import AsciiTable
import termcolor
from colorama import Fore, Back, Style



print ("\n\n\n")
table_header = [
    ['\t\t\tQuiz Application'],
    ['\t\t\tDone by Jonathan Kamau']
]

"""table_data = [
    ['Heading1', 'Heading2'],
    ['row1 column1', 'row1 column2'],
    ['row2 column1', 'row2 column2'],
    ['row3 column1', 'row3 column2']
]"""
table = AsciiTable(table_header)
print (table.table)
print (Fore.GREEN+"\n")
