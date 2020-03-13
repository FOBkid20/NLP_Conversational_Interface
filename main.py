from helper import extract_recipe_name
import re

back = True
while back:
    while True:
        user = input("Bot: What do you want to do?(Press q to end this conversation)   ")
        word_list = user.split()
        if word_list[0] == 'what':
            print("\nwhat")
        elif word_list[0] == 'how':
            print('\nhow')
        elif word_list[0] == 'q':
            print("quit the conversation")
            back = False
            break
        else:
            print('\nBot: Sure. Please specify a URL.')
            break
    if not back:
        break
    link = input()
    recipe = extract_recipe_name(link)
    print("Bot: Alright. So let's start working with '",recipe,"' What do you want to do?")
    print('\nBot:  [1] Go over ingredients list or [2] Go over recipe steps.')
    while True:
        
        user = input()
        word_list = user.split()
        if word_list[0] == 'what':
            print("\nwhat")
        elif word_list[0] == 'how':
            print('\nhow')
        elif user.isdigit():
            if int(user) == 1:
                print("go over the list")
            else: 
                print("go over the steps")
        elif re.search('yes',user.lower()):
            print("you say yes")
        elif re.search('no',user.lower()):
            print("you say no")
            back = True
            break
        else:
            print('\nBot:Should I continue to the 2nd step?')

