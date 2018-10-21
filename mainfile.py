#!/usr/bin/env python
from behave import given, then, when
from behave import *
import os
import sys
#import wget
#from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from datetime import datetime


@given("I have a new {item} in my cart")

def i_have_itm_in_cart(context, item):
    print("Opened : {}".format(item))
    usr = 'Enter Email Id:'
    pwd = 'Enter Password:'
    # driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    #options.add_argument('--no-sandbox')
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.google.com/')
    print("Opened google home page")
    sleep(1)
    
    # Take a screen shot of the page with time stamp 
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    driver.get_screenshot_as_file('Google_Homepage-%s.png' % now)
    
    
