from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
import time
import urllib2

config = {}
execfile("dnsrecords.config", config) 

domains  = config['domains']
username = config['username']
password = config['password']
cnt = 0

def screenshot(descr):
	global cnt
	global driver
	cnt = cnt + 1
	driver.save_screenshot(str(cnt).zfill(3) + '_' + descr + '.png')

# IP Ophalen	
myip = urllib2.urlopen("http://myip.dnsdynamic.org/").read()
	
# Browser starten
driver = webdriver.PhantomJS()

# Inloggen
driver.get("http://www.mijndomein.nl/login")
driver.find_element_by_name("loginform_username").send_keys(username)
driver.find_element_by_name("loginform_password").send_keys(password) #, Keys.RETURN)
driver.find_element_by_name("loginform_password").submit()
screenshot('na_log-in')

for domain in domains:
	# DNS Instellen scherm openen
	a = driver.execute_script("puntapi.DoCommand('dnsclient','dnsadmin','','','');")
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Formid")))
	screenshot('na_dns_instellen_klik_' + domain['name'])
	
	# Domein kiezen
	elem = driver.find_element_by_id('selectdomainbox_replacement')
	elem.clear()
	elem.send_keys(domain['name'])
	time.sleep(1) # onchange event een kans geven
	elem.send_keys(Keys.RETURN)
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Formid")))
	screenshot('na_domein_keuze_' + domain['name'])

	for subdomain in domain['subdomains']:
		# Klikken op naam subdomein
		driver.find_element_by_xpath("//div[text()='" + subdomain + "']").click()
		screenshot('na_klikken_subdomein_' + subdomain + '.' + domain['name'])

		# Nieuw IP invullen
		elem = driver.find_element_by_xpath("//div[text()='" + subdomain + "']/following::input[2]")
		elem.clear()
		elem.send_keys(myip)
		time.sleep(1) # onchange event een kans geven
		screenshot('na_invoeren_ip_' + subdomain + '.' + domain['name'])

		# Klikken op save icoontje
		driver.find_element_by_xpath("//div[text()='" + subdomain + "']/following::div[6]").click()
		screenshot('na_klikken_save_row_icoon_' + subdomain + '.' + domain['name'])

	# Klikken op opslaan
	driver.find_element_by_xpath("//td[text()='Opslaan']/ancestor::div[1]").click()
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='DNS opgeslagen']")))
	screenshot('na_klikken_opslaan_knop_' + domain['name'])
	
driver.quit
