from selenium import webdriver
import time

browser=webdriver.Edge('C:\edgedriver_win64\msedgedriver.exe')
browser.get('https://www.codechef.com/')

prob_code=input('Enter the CodeChef problem code: ')
username=input('Enter username: ')
from getpass import getpass
password=getpass('Enter the password: ')

username_element=browser.find_element_by_id('edit-name')
password_element=browser.find_element_by_id('edit-pass')
username_element.send_keys(username)
password_element.send_keys(password)
browser.find_element_by_id('edit-submit').click()

langs=['C' ,'C++' ,'Java' ,'Java Script' , 'Kotlin']
print('Supported langualges: ')
for lang in langs:
	print(lang)
lang=input('Enter the programming language: ')
if lang=='C':	
	xpath='//*[@id="edit-language"]/option[2]'
elif lang=='C++':
	xpath='//*[@id="edit-language"]/option[1]'
elif lang=='Java':
	xpath='//*[@id="edit-language"]/option[3]'
elif lang=='Java Script':
	xpath='//*[@id="edit-language"]/option[14]'
elif lang=='Kotlin':
	xpath='//*[@id="edit-language"]/option[20]'

filename=input('Enter the name of solution file: ')

try:
	browser.get('https://www.codechef.com/submit/'+prob_code)
	time.sleep(4)
	mode_switch=browser.find_element_by_id('edit-submit')
	if mode_switch.get_attribute('value')=='Switch to Non-IDE mode':
		mode_switch.click()
	browser.execute_script("window.scrollTo(0,(document.body.scrollHeight)/3)")
	browser.find_element_by_id('edit_area_toggle_checkbox_edit-program').click()
	with open(filename, 'r') as f:
		code=f.read()
	code_element=browser.find_element_by_id('edit-program')
	code_element.send_keys(code)
	temp_code=code.split(sep='\t')
	code=" ".join(temp_code)
	code_element.send_keys(code)
	browser.find_element_by_xpath(lang).click()
	browser.find_element_by_id('edit-submit-1').click()
	browser.close()
except:
	print('Wrong Credentials')