import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    #executable_path = {"executable_path": "C:\Users\anuj\webScrapingHW"}
    #return Browser("chrome", **executable_path, headless=False)
    return Browser("chrome",headless=False)

#create one python dictionary
def scrape():
    
    result = {}
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)
    html = browser.visit(url)
    soup = BeautifulSoup(html, "html.parser")
    result["news_title"] = soup.find('div', class_="content_title").text
    result["news_para"] = soup.find('div', class_="article_teaser_body").text
    
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA16883-1920x1200.jpg"
    browser.visit(featured_image_url)
    result["featured_image"] = featured_image_url
    
    twitter_url = "https://twitter.com/marswxreport?lang=en "
    twitter_response = requests.get(twitter_url)
    soup_weather = bs(twitter_response.text, 'html.parser')
    result["mars_weather"] = soup_weather.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    
    weather_url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    mars_df = df.transpose()
    mars_df.columns = ['Equatorial Diameter', 'Polar Diameter', 'Mass', 'Moons', 
              'Orbit Distance', 'Orbit Period', 'Surface Temperature', 'First Record', 
              'Recorded By']
    mars_df = mars_df.iloc[1:]
    fact_table = mars_df.to_html(index = False)
    fact_table.replace('\n', '')
    mars_df.to_html('fact_table.html')
    
    return result
    
    #browser = init_browser()
    #mars_hemispheres_images = {}
    #result = {}
    #title_list = []
    #url_list = []
    #mars_hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/'
    #browser.visit(mars_hemisphere_url)
    #html=browser.html
    #soup = BeautifulSoup(html, 'html.parser')
    #descriptions = soup.find_all('div', class_='description')
    #print(descriptions)
    #for description in descriptions:
        #title = description.find('h3').text
        #img_url = description.a['href']
        #img_url = "/Mars/Viking/cerberus_enhanced"
        #img_url_final = "https://astropedia.astrogeology.usgs.gov/download" + img_url + ".tif/full.jpg"
        #print(title)
        #print(img_url_final)
        #title_list.append(title)
        #url_list.append(img_url_final)

    #result = zip(title_list, url_list)
    #mars_hemispheres_images = dict(result)
    
    #return(mars_hemispheres_images)
    
    
                       
    
    

    
    