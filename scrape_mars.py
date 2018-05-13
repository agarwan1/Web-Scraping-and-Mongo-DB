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

def scrape():
    browser = init_browser()
    mars_hemispheres_images = {}
    result = {}
    title_list = []
    url_list = []
    mars_hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/'
    browser.visit(mars_hemisphere_url)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    descriptions = soup.find_all('div', class_='description')
    print(descriptions)
    for description in descriptions:
        title = description.find('h3').text
        img_url = description.a['href']
        img_url = "/Mars/Viking/cerberus_enhanced"
        img_url_final = "https://astropedia.astrogeology.usgs.gov/download" + img_url + ".tif/full.jpg"
        print(title)
        print(img_url_final)
        title_list.append(title)
        url_list.append(img_url_final)

    result = zip(title_list, url_list)
    mars_hemispheres_images = dict(result)
    
    return(mars_hemispheres_images)