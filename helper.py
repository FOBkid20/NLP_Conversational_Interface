import nltk
import re
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

def extract_recipe_name(link):
    word_list = link.split('/')
    recipe_name = word_list[len(word_list)-1]
    if recipe_name=='':
        recipe_name = word_list[len(word_list)-2]
    # print(recipe_name)
    recipe_name = recipe_name.replace('-',' ').strip()
    return recipe_name

# link = 'https://www.allrecipes.com/recipe/218091/classic-and-simple-meat-lasagna/'
# recipe = extract_recipe_name(link)
# print(recipe)

def get_cooking_tools(word):
    tools1 = ['[Pp]ot','[Kk]nife','[Pp]an.?','[Kk]nives','[Gg]rater','[Bb]oard','[Oo]pener','[Cc]up.?','[Ss]poon.?','[Bb]owl.?','[Cc]olander.?','[Pp]eeler.?','[Mm]asher.?','[Ww]hisk.?','[Ss]pinner.?','[Gg]rater.?','[Ss]hear.?','[Jj]uicer','[Pp]ress','[Ss]teel','[Ss]harpener.?']
    tools2 = ['[Ff]oil','skillet','plate.?','[Ss]patula.?','[Ss]poon.?','[Tt]ong.?','[Ll]adle.?','[Mm]itt.?','[Oo]ven','[Tt]rivet.?','[Gg]uard','[Tt]hermometer.?','[Bb]lender.?','[Ss]cale.?','[Cc]ontainer.?']
#     print(tools[2])
#     print(re.search(tools[4],'spoon'))
    for tool in tools1:
        if re.search(tool,word):
            return True
    for tool in tools2:
        if re.search(tool,word):
            return True
    return False

def get_cooking_method(word):
    methods1 = ['[Ss]tand','[Ww]ait','[Bb]oil.*','[Ss]aut[eé]','[Bb]ak(e|ing)','[Ff]r(y|ied)','[Rr]oast', '[Gg]rill','[Ss]team','[Pp]oach','[Ss]immer','[Bb]roil','[Bb]lanch','brais(e|ing)','[Ss]tew']
    methods2 =['[Re]move','[Bb]roil','[Bb]rais(e|ing)','[Cc]hop','[Dd]ic(e|ing)','[Mm]inc(e|ing)','[Mm]uddl(e|ing)','[Ss]i[nm]mer','[G]rat(e|ing)','[Ss]tir','[Ss]hak(e|ing)','[Cc]rush','[Ss]queez(e|ing)','[Cc]ook','[Rr]educ(e|ing)','[Dd]rain','[Mm]ix','[Tt]op','[Ss]prinkl(e|ing)','[Cc]ombin(e|ing)','[Ss]pread','[Ss]ear','[Bb]rown','[Cc]har','[Rr]ub','[Cc]hill','[Rr]inc(e|ing)','[Dd]ip','[Hh]eat','[Cc]over']
    for method in methods1:
        if re.search(method,word):
            return True
        
    for method in methods2:
        if re.search(method,word):
            return True
    return False
result = get_cooking_method("chopped")

def get_noun(text):
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    stopwords = stopwords.words('english')
    stop_words = set(stopwords) 
    tokenized = sent_tokenize(text) 
    for i in tokenized: 
        wordsList = nltk.word_tokenize(i) 
        # removing stop words from wordList 
        wordsList = [w for w in wordsList if not w in stop_words]  
        tagged = nltk.pos_tag(wordsList) 
    for i in tagged:
        if i[1] == 'NN'or i[1] == 'NNS' or i[1] == 'NNP' or i[1] == 'NNPS':
            return(i[0])
        
def get_verb(text):
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    stopwords = stopwords.words('english')
    stop_words = set(stopwords) 
    tokenized = sent_tokenize(text) 
    for i in tokenized: 
        wordsList = nltk.word_tokenize(i) 
        # removing stop words from wordList 
        wordsList = [w for w in wordsList if not w in stop_words]  
        tagged = nltk.pos_tag(wordsList) 
    verb_tags = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    for i in tagged:
        if i[1] in verb_tags:
            return(i[0])