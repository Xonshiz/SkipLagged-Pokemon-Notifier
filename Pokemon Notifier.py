#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Xonshiz"
__email__ = "Xonshiz@psychoticelites.com"
__website__ = "http://www.psychoticelites.com"
__version__ = "v1.0"
__description__ = "Looks for the pokemon on http://skiplagged.com/pokemon and notifies if a particular pokemon is available or not"



import sys,ctypes,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui



def create_driver():
	driver = webdriver.PhantomJS(service_args=['--load-images=no'])
	#options = webdriver.ChromeOptions()
	#options.add_extension('adblockpluschrome-1.11.0.1591.crx')
	#driver = webdriver.Chrome(service_args=["--verbose", "--log-path=Main_Log_File.log"])
	print '######### Pokemon Notifier #########\n'
	print 'Author : Xonshiz (github.com/Xonshiz)\n'
	return driver





def Website_Open(driver):

	f = open('Pokemon.txt','r')
	User_Pokemon_Name = str(f.read())
	print 'I will be looking for ', User_Pokemon_Name

	try:
		if not User_Pokemon_Name:
			ctypes.windll.user32.MessageBoxA(0, "You did not tell me which pokemon you're looking for!", 1)
			sys.exit()
	except Exception, e:
		#raise e
		#print e
		#print "Couldn't Read The File!"
		pass


	driver.get('http://skiplagged.com/pokemon')
	
	try:
		alert = driver.switch_to_alert()
		alert.accept()
	except Exception, e:
		#raise e
		#print e
		pass

	driver.find_element_by_xpath('//*[@id="show-filters"]').click()
	#driver.quit()
	try:
		Poke_List_Raw = driver.find_element_by_xpath('//*[@id="toggles"]/ol')
	except Exception, e:
		#raise e
		print "Coudn't find the Pokemon List!"
		sys.exit()
	Poke_List = Poke_List_Raw.text
	print 'Current Available Pokemons :\n########################################\n',Poke_List
	#User_Pokemon_Name = 'Pidgey'

	if User_Pokemon_Name.upper() in Poke_List.upper():
		#print 'Yep there!'
		Pop_Up = 'Found '+str(User_Pokemon_Name)
		ctypes.windll.user32.MessageBoxA(0, Pop_Up, "Pokemon Found!", 1)
		
	if User_Pokemon_Name.upper() not in Poke_List.upper():
		print 'Not here!\n'
		time.sleep(120)
		print 'Starting the script again!\n'
		Website_Open(driver)
		
		




driver = create_driver()
Website_Open(driver)
