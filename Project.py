import time
import datetime
from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler


usernameStr = input('Your fucking account name:')
passwordStr = input('Oneechan pls enter your password owo:')
browser = webdriver.Chrome()
def autosignIn():
    #Megnyitja a google classroom-ot
    browser.get('https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&followup=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    browser.maximize_window()
    #Bejelentkezes felhasznalonev
    username = browser.find_element_by_id('identifierId')
    username.send_keys(usernameStr)
    nextButton = browser.find_element_by_id('identifierNext')
    nextButton.click()
    
    #wait 10 seconds until website load in
    time.sleep(8)
    
    #Jelszo
    password = browser.find_element_by_name('password')
    password.send_keys(passwordStr)
    
    signIn = browser.find_element_by_id('passwordNext')
    signIn.click()
    
#Write in 'Jelen'
def autoJelen():
    button1 = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/section/div/div[1]')
    button1.click()
    time.sleep(3)
    button2 = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/section/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div/div[1]/div[2]/textarea')
    button2.send_keys('Jelen')
    button3 = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/section/div/div[1]/div[2]/div/div/div/div/div/div[3]/div[2]/div[2]/div/span/span')
    button3.click()
  
#Working unit  
def work():
    try:
        global week
        browser.get(orarend[week])
        time.sleep(6)
        autoJelen()
        week += 1
    except KeyError:
        scheduler.shutdown()

#get Curent date
now = datetime.datetime.now()
curdate = ('%s-%s-%s' % (now.year,now.month,now.day))

#Schedulers

scheduler = BlockingScheduler()
scheduler.add_job(work, 'date', run_date='%s 8:00:00' % curdate, args=[])
scheduler.add_job(work, 'date', run_date='%s 8:55:00' % curdate, args=[])
scheduler.add_job(work, 'date', run_date='%s 9:55:00' % curdate, args=[])
scheduler.add_job(work, 'date', run_date='%s 10:50:00' % curdate, args=[])
scheduler.add_job(work, 'date', run_date='%s 11:45:00' % curdate, args=[])
scheduler.add_job(work, 'date', run_date='%s 12:50:00' % curdate, args=[])
scheduler.add_job(work, 'date', run_date='%s 13:45:00' % curdate, args=[])
scheduler.add_job(work, 'date', run_date='%s 14:35:00' % curdate, args=[])


#import orarend
orarend = {}
def oraimport():
    with open('orarend.txt','r') as r:
        for each in r:
            owo = each.strip('\n').split(';')
            orarend.setdefault(int(owo[0]))
            orarend[int(owo[0])] = owo[1]
        

#decide which weekdays
def f():
    weekday = datetime.datetime.today().weekday()
    owo = {1:11,2:21,3:32,4:41,5:51}
    return owo[weekday]

oraimport()

#Sign in
week = f()
autosignIn()
time.sleep(3)
scheduler.start()    



    
    
