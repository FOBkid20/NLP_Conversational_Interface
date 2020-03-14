from helper import extract_recipe_name, get_verb, get_noun
import re

back = True
while back:
    while True:
        user = input("Bot: What do you want to do? (Press q to end this conversation)\n")
        word_list = user.split()
        if word_list[0] == 'what':
            print("\nwhat")
            print(get_noun(user))
        elif word_list[0] == 'how':
            print('\nhow')
            print(get_verb(user))
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
    while 'allrecipes.com' not in link:
        print('\nBot: Sorry, please give me a URL from allrecipes.com.')
        link = input()
    recipe = extract_recipe_name(link).strip().title()
    print("\nBot: Alright. So let's start working with '",recipe,"'. What do you want to do?", sep = '')
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
                print("\nBot: Here are the ingredients for '", recipe, "':", sep = '')
            elif int(user) == 2:
                print("\nBot: The 1st step is:")
            elif int(user) > 2 or int(user) < 1:
                print('\nBot: Please choose what you want to do. ')
        elif re.search('yes',user.lower()):
            print("you say yes")
        elif re.search('no',user.lower()):
            print("you say no")
            back = True
            break
        else:
            print('\nBot:Should I continue to the 2nd step?')

