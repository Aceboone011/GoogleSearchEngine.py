#install google lib
#open comand prompt; "pip install google" press enter
 #import lib
#call search function

from googlesearch import search

#user input  = search input + query variable

query = input('What would you like to look up ??')

#Report from the 1st result.
#the pause is needed

for i in search (query, start = 0, pause =4):
    print(i)
    
