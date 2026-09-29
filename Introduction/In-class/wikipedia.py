
#Importing a wikipedia page by using URL and opening in a new page.
#Libraries are set of pre-written python code that can be
#used for specific tasks.

import webbrowser


# create a variable called "url"
# assign the variable to tell it to store the text of the url
# we use single = sign
# text data has to be surrounded by quote so python doesn't try
# to intrupt it as instructions, it knows that it is a data
url = 'https://randomincategory.toolforge.org/Featured_articles?site=en.wikipedia.org'

# use the webbrowser library to open web browser and go to the url
# saved in the url variable
# stored and tell the browser to open that page
webbrowser.open(url)

