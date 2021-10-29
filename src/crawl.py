import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random

random.seed(42)

#main sourcde url 
#construction accident -> search keyword

if __name__ == "__main__" :
    m_url ="https://www.nytimes.com/search?dropmab=false&endDate=20200229&query=%22construction%22%20accident&sort=best&startDate=20000101"

    session = requests.Session()
    req=session.get(m_url) #default is s_url
    soup = BeautifulSoup(req.text, 'html.parser')

    chrome_options = webdriver.ChromeOptions
    #chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path='/Users/macbookpro/Project_construction/chromedriver')

    link = []
    driver.get(m_url)
    time.sleep(3)
    for i in range(100) :
        a = driver.page_source
        b = BeautifulSoup(a, 'html.parser')
        #stream-panel > div.css-13mho3u > ol > li:nth-child(1) > div > div.css-1l4spti > a
        #stream-panel > div.css-13mho3u > ol > li > div > div.css-1l4spti > a
        #site-content > div > div:nth-child(2) > div.css-46b038 > ol > li:nth-child(1) > div > div > div > a
        c = b.select('#site-content > div >div>div> ol >li> div > div > div > a')
        
        for j in range(len(c)) :
            if c[j].attrs['href'] not in link :
                link.append(c[j].attrs['href'])
            else :
                pass
        
        driver.find_element_by_xpath('//*[@id="site-content"]/div/div[2]/div[2]/div/button').click()
        time.sleep(3)

    #link copy
    a_link = link.copy()
    diff_link = []

    #delete unsupported news 
    for i in range (len(a_link)) :
        print(a_link[i])
        if a_link[i][1] != '2':
            
            diff_link.append(a_link[i])
                
        else : 
            continue

    for j in range(len(diff_link)):
        if diff_link[j] in a_link:
            a_link.remove(diff_link[j])
            
