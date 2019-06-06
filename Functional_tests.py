from selenium import webdriver


#  Start selenium webdriver to pop up a real firefox browser window
browser = webdriver.Firefox()

#  Use to open web page expecting to be served from the local PC
browser.get('http://localhost:8000')

#  Check (making a test assertion) that the page has the word "Django" in its title
assert 'Django' in browser.title
