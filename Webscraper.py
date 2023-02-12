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
    alist = list()
    data_str = ""
  
    for items in soup.find_all("div", class_="a-row a-spacing-small review-data"):
        alist.append(items)
    print(len(alist))
    return(alist)  

def scrape(product_url):
    #url = "https://www.amazon.ca/Apple-MLWK3AM-A-New-AirPods/product-reviews/B09JQMJHXY/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
    
    soup = html_code(product_url)
    #print(soup)

    for x in range(1,10):
        if x != 1:
            soup = html_code(f'{product_url}&pageNumber={x}')
        

        rev_data = cus_rev(soup)
        rev_result = []
        for i in rev_data:
            if i is "":
                pass
            else:
                rev_result.append(i)

    #print("web_scraper:{}".format(rev_result))
    
    # for x in range(2,10):
        
    #     print(f'Getting page: {x}')
    #     cus_rev(soup)    
    return rev_result



    

