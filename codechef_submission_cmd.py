import sys
from selenium import webdriver
import time

# Reading command line arguments
credentials=sys.argv[1]
solution=sys.argv[2]

browser=webdriver.Edge('C:\edgedriver_win64\msedgedriver.exe')
browser.get('https://www.codechef.com/')

temp_sol=solution.split(sep='\\')[-1].split(sep='.')
prob_code, lang=temp_sol[0], temp_sol[1]
with open(credentials) as f:
	cred=f.read()
temp_cred=cred.split(sep='\n')
username, password=temp_cred[0], temp_cred[1]
username_element=browser.find_element_by_id('edit-name')
password_element=browser.find_element_by_id('edit-pass')
username_element.send_keys(username)
password_element.send_keys(password)
browser.find_element_by_id('edit-submit').click()

lang=lang.lower()
if lang=='c':	
	xpath='//*[@id="edit-language"]/option[2]'
elif lang=='cpp':
	xpath='//*[@id="edit-language"]/option[1]'
elif lang=='java':
	xpath='//*[@id="edit-language"]/option[3]'
elif lang=='js':
	xpath='//*[@id="edit-language"]/option[14]'
elif lang=='kt':
	xpath='//*[@id="edit-language"]/option[20]'

try:
	browser.get('https://www.codechef.com/submit/'+prob_code)
	time.sleep(4)
	mode_switch=browser.find_element_by_id('edit-submit')
	if mode_switch.get_attribute('value')=='Switch to Non-IDE mode':
		mode_switch.click()
	browser.execute_script("window.scrollTo(0,(document.body.scrollHeight)/3)")
	browser.find_element_by_id('edit_area_toggle_checkbox_edit-program').click()
	with open(solution, 'r') as f:
		code=f.read()
	code_element=browser.find_element_by_id('edit-program')
	code_element.send_keys(code)
	temp_code=code.split(sep='\t')
	code=" ".join(temp_code)
	code_element.send_keys(code)
	browser.find_element_by_xpath(lang).click()
	browser.find_element_by_id('edit-submit-1').click()
except:
	print('Wrong Credentials or Unknown error')
