def extract_recipe_name(link):
    word_list = link.split('/')
    recipe_name = word_list[len(word_list)-1]
    if recipe_name=='':
        recipe_name = word_list[len(word_list)-2]
    # print(recipe_name)
    recipe_name = recipe_name.replace('-',' ')
    return recipe_name

# link = 'https://www.allrecipes.com/recipe/218091/classic-and-simple-meat-lasagna/'
# recipe = extract_recipe_name(link)
# print(recipe)