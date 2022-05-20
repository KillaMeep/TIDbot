from ast import Try
import cmd
import os
from re import L
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime
import time
class utils:
    def txtcln(text):
        return text.encode('ascii','ignore').decode()
    def dt_check():
        year = datetime.datetime.now().year
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        hour = datetime.datetime.now().hour
        if hour > 11:
            day+=1
        date_time = datetime.datetime(year, month, day, 11, 00)
        return '<t:'+str(int(time.mktime(date_time.timetuple())))+':R>'
    def delete(filename):
        if os.name == 'nt':
            os.system(f'del {filename}')
        else:
            os.system(f'rm -rf {filename}')
class chromedriver_init:
    def get_path():
        path = os.getcwd()
        return path
    
    def start(path):
        myoptions = Options()
        global driver
        myoptions.headless = True
        if os.name == 'nt':
            driver = webdriver.Chrome(path+'\\utils\\chromedriver.exe', options=myoptions)
        else:
            driver = webdriver.Chrome(path+'/utils/chromedriver', options=myoptions)
        driver.get('https://www.todayindestiny.com')
        chromedriver_init.clear_ads()
        return driver
    def clear_ads():
        all_iframes = driver.find_elements_by_tag_name("iframe")
        if len(all_iframes) > 0:
            driver.execute_script("""
                var elems = document.getElementsByTagName("iframe"); 
                for(var i = 0, max = elems.length; i < max; i++)
                     {
                         elems[i].hidden=true;
                     }
                                  """)
class tid_lookup:
    def LS_V2():
        driver.refresh()
        chromedriver_init.clear_ads()
        LS_DAT = {}
        chromedriver_init.clear_ads()
        LS2 = driver.find_element(By.XPATH,"//*[starts-with(@id, 'lost_sector_lost_sector')]")
        LS2.click()
        c1 = LS2.find_elements(By.XPATH,".//*")
        chunker = []
        for x in range(0,len(c1)):
            chunker.append(c1[x].text)
        nm = c1[21].text.lower()
        nm2 = ' '.join(elem.capitalize() for elem in nm.split())
        LS_DAT['sectorname']=nm2
        LS_ACTUAL = utils.txtcln(c1[26].text)
        LS_DAT['champs']=LS_ACTUAL.split('Champions: ')[1].split('Burn:')[0].replace('  ',' ')[1:]
        LS_DAT['burn'] = LS_ACTUAL.split('Burn: ')[1].split('Shields:')[0][1:]
        LS_DAT['shield'] = LS_ACTUAL.split('Shields: ')[1].split('Modifiers:')[0][1:]
        LS_DAT['desc'] = LS_ACTUAL.split('Champions: ')[0]
        LS_DAT['time'] = utils.dt_check()
        time.sleep(1)
        c1[53].screenshot('LS.png')
        return LS_DAT
    def VOG_V2():
        driver.refresh()
        chromedriver_init.clear_ads()
        VOG_DAT = {}
        VOG = driver.find_element(By.XPATH,"//*[starts-with(@id, 'raid_vault_of_glass')]")
        VOG.click()
        c1 = VOG.find_elements(By.XPATH,".//*")
        time.sleep(1)
        c1[36].screenshot('vog.png')
        return VOG_DAT
    def NF_V2():
        driver.refresh()
        chromedriver_init.clear_ads()
        NF_DAT = {}
        NF = driver.find_element(By.XPATH,"//*[starts-with(@id, 'milestone_1942283261_1495545956')]")
        NF.click()
        c1 = NF.find_elements(By.XPATH,".//*")
        nm = c1[21].text.lower()
        nm2 = ' '.join(elem.capitalize() for elem in nm.split())
        NF_DAT['name']=nm2
        time.sleep(1)
        c1[30].screenshot('nf.png')
        return NF_DAT