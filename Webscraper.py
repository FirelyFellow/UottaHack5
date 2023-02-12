from bs4 import BeautifulSoup
import requests
  
HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/90.0.4430.212 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

# user define function
# Scrape the data
def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text
  
def html_code(url):
  
    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
  
    # display html code
    return (soup)


def cus_rev(soup):
    # find the Html tag
    # with find()
    # and convert into string
    data_str = ""
    alist = list()
    #data_str_1 = ""
  
    for items in soup.find_all("div", class_="a-row a-spacing-small review-data"):
        #for item in soup.find_all("div", id_='customer_review-R5ZLCO12H50ZL', class_='a-row a-spacing-small review-data'):
           # data_str_1 = data_str_1 + item.get_text()
        #data_str = data_str + items.get_text()
        alist.append(items)
       # result_1 = data_str_1.split("\n")
    #result = data_str.split("\n")
    print(len(alist))
    return(alist)  

def scrape(product):
    url = "https://www.amazon.ca/Apple-MLWK3AM-A-New-AirPods/product-reviews/B09JQMJHXY/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    
    soup = html_code(url)
    #print(soup)

    rev_data = cus_rev(soup)
    rev_result = []
    for i in rev_data:
        if i is "":
            pass
        else:
            rev_result.append(i)

    #print("web_scraper:{}".format(rev_result))

    return rev_result
#print(rev_result)

#headline = div.h2.text
#print(headline)

#subparagraph = div.find('header', class_='major').p.text
#print(subparagraph)

#summary = article.find('div', class_='ml-3').p.text
#print(summary)


