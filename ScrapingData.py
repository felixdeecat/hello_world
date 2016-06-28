# from http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/

from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.chicagoreader.com"

# @param section_url is the section of the wepage's content list "this uses Food and Drink"
def get_category_links(section_url): 
    soup = make_soup(section_url)
    boccat = soup.find("div", "gridLeader") # find the <d1> element with a class of boccat and store it
    # for every <dd> element in boccat, get the href of its <a> element and concatenate with the BASE_URL to make a link    
    print (boccat)    
#    category_links = [BASE_URL + dd.a["href"] for dd in boccat.find("div")]
#    return category_links

def get_category_winner(category_url):
    soup = make_soup(category_url)
    category = soup.find("h1", "headline").string
    winner = [h2.string for h2 in soup.find_all("h2", "boc1")]
    runners_up = [h2.string for h2 in soup.find_all("h2", "boc2")]
    return {"category": category,
            "category_url": category_url,
            "winner": winner,
            "runners_up": runners_up}
            

def make_soup(url):
    html = urlopen(url).read() # open section_url and read it into the html object
    soup = BeautifulSoup(html,"lxml") # initialize and parse with lxml
    return soup

if __name__ == '__main__':
    food_n_drink = ("http://www.chicagoreader.com/chicago/"
                    "best-of-chicago-2011-food-drink/BestOf?oid=4106228")
    
    categories = get_category_links(food_n_drink)

    data = [] # a list to store our dictionaries
    for category in categories:
        winner = get_category_winner(category)
        data.append(winner)
        sleep(1) # be nice

print data