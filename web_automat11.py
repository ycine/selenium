#Tak poglądowo co robiłem.. To najdłuższy skrypt jak napisałem :) i najlepiej dzialajacy

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
start = time.time()
# profile = webdriver.FirefoxProfile()
# profile.set_preference("permissions.default.image", 2)
# browser = webdriver.Firefox(firefox_profile=profile)


xchro = r'C:\Users\dom\AppData\Roaming\Mozilla\Firefox\Profiles\ea1nlg8k.default-1479169428934-1528392929578\extensions\{83efb7a7-cf21-4f94-840a-316f651053ef}.xpi'
browser = webdriver.Firefox()
browser.install_addon(xchro, temporary=True)
#skrypt do gry webowej wolałbym nie podawać jakiej :P
browser.get("")

#To jest API performance.timing - służy do zliczania czasu odpowiedzi - czyli czas ladowania strony czy jakiegos elementu na stronie.
navigationStart = browser.execute_script("return window.performance.timing.navigationStart")
responseStart = browser.execute_script("return window.performance.timing.responseStart")
domComplete = browser.execute_script("return window.performance.timing.domComplete")
backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart
print( "Back End: %s" % backendPerformance)
print ("Front End: %s" % frontendPerformance)

wait = WebDriverWait(browser, 55).until(EC.element_to_be_clickable((By.XPATH,\
"/html/body/div[1]/div/div[6]/div/div[2]/div[2]/p")))
ele1h = browser.find_element_by_xpath("/html/body/div[1]/div/div[6]/div/div[2]/div[2]/p").click()

ele2 = browser.find_element_by_class_name("f-input.username")
ele2b = ele2.send_keys("tts")
ele3 = browser.find_element_by_class_name("f-input.password")
ele3b = ele3.send_keys("tts")
ele3c = browser.find_element_by_class_name("btn.norm.bronze.blue.login").click()
    #DON jUAN Pack
try:
    # WebDriverWait(browser, 40).until(EC.visibility_of_element_located((By.XPATH, \
    # "//div[@class='pack right big']")))
    WebDriverWait(browser, 45).until(EC.visibility_of_element_located((By.CLASS_NAME, \
    "effect-tooltip")))
    # WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "//div[@class='button x-pop bronze close']")))
    WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,\
    "//div[@class='button x-pop bronze close']")))
    browser.find_element_by_xpath("//div[@class='button x-pop bronze close']").click()
except TimeoutException:
    pass
#Special offer !
try:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,\
    "/html/body/div[1]/div/div[8]/div[2]/div/div[3]/div[3]")))
    browser.find_element_by_xpath("/html/body/div[1]/div/div[8]/div[2]/div/div[3]/div[3]").click()
except TimeoutException:
    pass


vcc = 0

# Attention!
try:
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, \
    "/html/body/div[1]/div/div[7]/div[2]/div/div/div[4]/div[1]")))
    vc = browser.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]/div/div/div[5]").click()
except TimeoutException:
    pass

while vcc == 0:
    #misja
    WebDriverWait(browser, 50).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'main-map loc005')]//div[6]")))
    ele4 = browser.find_element_by_xpath("//div[contains(@class,'main-map loc005')]//div[6]").click()
    #Battle
    WebDriverWait(browser, 45).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.norm.bronze.green.mission")))
    ele5 = browser.find_element_by_class_name("btn.norm.bronze.green.mission").click()
    #Fight
    WebDriverWait(browser, 35).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.bronze.green.fight")))
    ele6 = browser.find_element_by_class_name("btn.bronze.green.fight").click()
# Buy Energy

    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,\
        "//div[@class='btn norm bronze grey back']")))
        vc = browser.find_element_by_xpath("//div[@class='btn norm bronze grey back']").click()
        vcc += 1
        break
    except TimeoutException:
        pass

    WebDriverWait(browser, 45).until(EC.visibility_of_element_located((By.XPATH, \
    "//canvas[@width='1024']")))

    tp = ActionChains(browser)
    tp.move_by_offset(1045, 318)
    tp.click()
    tp.perform()
    #Congratulations

    try:
        WebDriverWait(browser, 35).until(EC.element_to_be_clickable((By.XPATH, \
         "//div[@class='btn-box']//div[3]")))
        vc = browser.find_element_by_xpath("//div[@class='btn-box']//div[3]").click()
    except TimeoutException:
        pass

    #"//div[@class='btn-box']//div[3]"

    #Close
    WebDriverWait(browser, 55).until(EC.element_to_be_clickable((By.XPATH,\
    "//div[@class='btn norm bronze green close']")))
    ele8 = browser.find_element_by_xpath("//div[@class='btn norm bronze green close']").click()

    trl = ActionChains(browser)
    trl.move_by_offset(-1045, -318)
    trl.click()
    trl.perform()

    try:
        # Congratulations!
        WebDriverWait(browser, 30).until((EC.element_to_be_clickable((By.XPATH, \
        "//div[@class='btn norm bronze green ok']"))))
        browser.find_element_by_xpath("//div[@class='btn norm bronze green ok']").click()
    except TimeoutException:
        pass

    try:
        # Congratulations!(You are Here)
        WebDriverWait(browser, 10).until((EC.element_to_be_clickable((By.XPATH, \
        "//div[@class='button x-pop bronze close']"))))
        browser.find_element_by_xpath("//div[@class='button x-pop bronze close']").click()
    except TimeoutException:
        pass

#Duels
WebDriverWait(browser, 70).until(EC.presence_of_element_located((By.XPATH,\
"//p[contains(text(),'Duels')]")))
WebDriverWait(browser, 70).until(EC.element_to_be_clickable((By.XPATH,\
"//p[contains(text(),'Duels')]")))
browser.find_element_by_xpath("//p[contains(text(),'Duels')]").click()

#Otwieranie skrzynek w duels
WebDriverWait(browser, 70).until(EC.presence_of_element_located((By.XPATH,\
("//div[contains(text(),'Star chest')]"))))


def open_duels():
    WebDriverWait(browser, 70).until(EC.element_to_be_clickable((By.XPATH,\
    ('//*[@class="chest-wrapper"]'))))
    skrzy12 = browser.find_elements_by_xpath\
    ('//div[@class="reward bronze ready" or @class="reward silver ready" or @class="reward gold ready"]')
    skrzy21 = len(skrzy12)
    print(len(skrzy12))


    while skrzy21 > 0:
        skrzy13 = browser.find_elements_by_xpath \
        ('//div[@class="reward bronze ready" or @class="reward silver ready" or @class="reward gold ready" or @class="reward platinum ready"]')
        #or @ class ="btn norm bronze blue open"]
        for i in skrzy13:
            WebDriverWait(browser, 70).until(EC.element_to_be_clickable((By.XPATH, \
            '//*[@class="chest-wrapper"]')))
            i.click()

            #Open
            WebDriverWait(browser, 70).until(EC.element_to_be_clickable((By.XPATH,\
            "//div[contains(@class,'btn norm bronze blue open')]")))
            browser.find_element_by_xpath\
            ("//div[contains(@class,'btn norm bronze blue open')]").click()
            skrzy21 -= 1
            print(skrzy21)

            try:
                #Claim
                WebDriverWait(browser, 5).until((EC.element_to_be_clickable((By.XPATH, \
                "//div[@class='btn norm bronze cyan']"))))
                browser.find_element_by_xpath("//div[@class='btn norm bronze cyan']").click()
            except TimeoutException:
                pass
            try:
                #Good
                WebDriverWait(browser, 5).until((EC.element_to_be_clickable((By.XPATH, \
                "//div[@class='btn norm bronze green']"))))
                browser.find_element_by_xpath("//div[@class='btn norm bronze green']").click()
            except TimeoutException:
                pass

            try:
                # Congratulations!
                WebDriverWait(browser, 30).until((EC.element_to_be_clickable((By.XPATH, \
                "//div[@class='btn norm bronze green ok']"))))
                browser.find_element_by_xpath("//div[@class='btn norm bronze green ok']").click()
            except TimeoutException:
                pass
# tutaj jest to potrzebne ale musi byc przypisane do obiektu czyli wait until
            try:
                # Congratulations!
                WebDriverWait(browser, 7).until((EC.visibility_of_element_located((By.XPATH, \
                "//div[@class='popup bronze regular popup-legaue-win']//div[@class='content']"))))
                WebDriverWait(browser, 5).until((EC.element_to_be_clickable((By.XPATH, \
                "//div[@class='button x-pop bronze close']"))))
                browser.find_element_by_xpath("//div[@class='button x-pop bronze close']").click()
            except TimeoutException:
                pass

            skrzy13.clear()
    skrzy12.clear()

open_duels()
# Sprawdza po raz drugi czy sa jakies nagrody duel do otwarcia, jesli tak to puszcza funkcje open 2 raz.
skrzy14 = browser.find_elements_by_xpath\
('//div[@class="reward bronze ready" or @class="reward silver ready" or @class="reward gold ready"\
 or @class="reward platinum ready"]')
skrzy22 = len(skrzy14)
print(len(skrzy14))
if skrzy22 > 0:
    open_duels()
else:
    pass

#Duels fight
for i in range(9):
    #Fight
    WebDriverWait(browser, 75).until(EC.element_to_be_clickable((By.XPATH,\
    "//div[@class='btn-fight']")))
    ele8 = browser.find_element_by_xpath\
    ("//div[@class='btn-fight']").click()

    #Funkcja przechodząca przez wszystkie etapy w duels
    def ready_duels():
        # Ready
        WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH, \
        "//div[@class='btn start']")))
        ele9 = browser.find_element_by_xpath("//div[@class='btn start']").click()

        # Ready!
        WebDriverWait(browser, 40).until(EC.visibility_of_element_located((By.XPATH, \
         "//canvas[@width='1024']")))

        tr = ActionChains(browser)
        tr.move_by_offset(1045, 318)
        tr.click()
        tr.perform()

        WebDriverWait(browser, 80).until(EC.invisibility_of_element((By.CLASS_NAME, \
        "eff-hints")))
        # Victory! - Close
        WebDriverWait(browser, 50).until((EC.element_to_be_clickable((By.XPATH, \
        "//div[@class='btn norm bronze green close']"))))
        browser.find_element_by_xpath("//div[@class='btn norm bronze green close']").click()
        trp = ActionChains(browser)
        trp.move_by_offset(-1045, -318)
        trp.perform()

        try:
            # Congratulations!
            WebDriverWait(browser, 25).until((EC.element_to_be_clickable((By.XPATH, \
             "//div[@class='btn norm bronze green close']"))))
            browser.find_element_by_xpath("//div[@class='btn norm bronze green close']").click()
        except TimeoutException:
            pass

        try:
            # Congratulations!
            WebDriverWait(browser, 5).until((EC.element_to_be_clickable((By.XPATH, \
             "//div[@class='btn norm bronze green ok']"))))
            browser.find_element_by_xpath("//div[@class='btn norm bronze green ok']").click()
        except TimeoutException:
            pass



#Ready!
    tt = browser.find_elements_by_xpath\
    ("//div[@class='btn norm bronze red fight']")

    if len(tt) > 0 and tt[0].is_displayed() and WebDriverWait(browser, 55).until(EC.element_to_be_clickable((By.XPATH,\
        "//div[@class='btn norm bronze red fight']")))\
        :
        # walcz pomimo iz full
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH,\
        "//div[@class='btn norm bronze red fight']" )))
        tt1 = browser.find_element_by_xpath\
        ("//div[@class='btn norm bronze red fight']").click()

        ready_duels()

    else:
        ready_duels()

#Close
WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH,\
"//div[@class='button x-pop bronze close']")))
browser.find_element_by_xpath("//div[@class='button x-pop bronze close']").click()

#Wheel of fortune
ele12g = browser.find_element_by_xpath("//div[@class='btn-submenu wof']")
browser.find_element_by_xpath("//div[@class='btn-submenu wof']").click()


for i in range(3):
    #tego uzywa sie jesli cos zaslania jakis element
    WebDriverWait(browser, 40).until(EC.invisibility_of_element_located((By.CLASS_NAME,\
    "blend-55")))

    # Rotate
    WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.XPATH,\
    "//div[@class='btn-spin-box']//div[contains(@class,'btn-spin')]")))

    browser.find_element_by_xpath(\
    "//div[@class='btn-spin-box']//div[contains(@class,'btn-spin')]").click()

    #wylosowana karta Good
    t1 = browser.find_elements_by_xpath("//div[@class='btn norm bronze green']")
    #skrzynka
    t2 = browser.find_elements_by_xpath("//canvas[@width='1024']")
    #Good
    t3 = browser.find_elements_by_xpath("//div[@class='btn norm bronze green close']")

    try:
        WebDriverWait(browser, 35).until((EC.invisibility_of_element_located((By.CLASS_NAME, "blend-55"))))
        # WebDriverWait(browser, 30).until(EC.element_to_be_clickable \
        # ((By.XPATH, "/html/body/div[1]/div/div[7]/div[2]/div/div/div[3]")))
        # browser.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]/div/div/div[3]").click()

        WebDriverWait(browser, 30).until(EC.element_to_be_clickable \
        ((By.XPATH, "//div[@class='btn norm bronze green close']")))
        browser.find_element_by_xpath("//div[@class='btn norm bronze green close']").click()

        print("kasa")
    except TimeoutException:
        pass

    try:
        WebDriverWait(browser, 0.5).until(EC.element_to_be_clickable\
        ((By.XPATH,"//canvas[@width='1024']")))
        print("canvas")
        browser.find_element_by_xpath("//canvas[@width='1024']").click()
    except TimeoutException:
        pass
    try:
        WebDriverWait(browser, 0.5).until(EC.element_to_be_clickable \
        ((By.XPATH, "//div[@class='btn norm bronze green']")))
        browser.find_element_by_xpath("//div[@class='btn norm bronze green']").click()
        print("karta")
    except TimeoutException:
        pass


#TO mierzy czas wykonania skryptu od danego punktu w skrypcie do danego punktu w sekundach(poczatek jest na gorze)
end = time.time()
se = (end - start) / 60
print("czas wykonania: %s" % se)
