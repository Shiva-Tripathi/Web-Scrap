#PROJECT INCLUDES 2 SYSTEMS :
#1- RAILWAY ENQUIRY SYSTEM AND 2- MOVIE ENQUIRY SYSTEM
# Modules used : BeautifulSoup4 , requests , Selenium , time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests


def RailMenu():
        print("=========== Railway Enquiry System ===========")
        print("         1.Train Status                   ")
        print("         2.Live Trains                    ")
        print("         3.Cancelled Trains               ")
        print("         4.Seat Availability              ")
        print("         5.Diverted Trains                ")
        print("         6.Quit                           ")

        n=int(input("\nEnter your choice: "))
        if(n==1):
            TrainStatus()
        elif(n==2):
            LiveTrain()

        elif(n==3):
            TrainCancel()

        elif(n==4):
            TrainSeat()
        elif(n==5):
            Divert()
        elif(n==6):
            Quit()

        else:
            print("Please enter valid choice !")


def TrainStatus():
    '''This function will give you status of the train you are
        looking for '''

    print('------------ Welcome to Indian Railways System -----------\n')
    Train_number=input('Enter train number : ')
    print('\nYour Train Number is : ',Train_number)

    date = input('Enter date in YYYYMMDD Format only : ')
    time.sleep(2)
    print('Fetching Data....')
    print('\nPlease wait!')
    time.sleep(1)

      #establishing connection to website using get() function
    source = requests.get('https://runningstatus.in/status/'+ Train_number+'-on-'+date).text

    soup = BeautifulSoup(source,'lxml')
    #In the above line , lxml acts as a parser through which information is
    #extracted from the webpage
    info = soup.find('div', class_="card-header")
    #print(article.prettify())
    line = info.text
    print(line)

    table = soup.find('table', class_='table table-bordered table-responsive')
    #Data from html table with specified class will be stored
    new_line= table.text
    print(new_line)

    print('Thank you for coming ')
    print("Have a great day ahead :) ")
    #returning to main menu
    RailMenu()

def LiveTrain():
    ''' This function allows you fetch details of those trains
        which are available to your station '''

    print('------------ Welcome to Indian Railways System -----------\n')
    Code = input('Enter station code : ')
    time.sleep(2)
    print('Fetching data .........')
    print('Please wait !')
    time.sleep(1)

    source = requests.get('https://runningstatus.in/livetrains/'+Code).text

    soup = BeautifulSoup(source , 'lxml')
    info =  soup.find('div', class_="card-header").text
    print(info)
    #.text is applied so as to avoid the <tr>,<td>,etc to be printed

    outline = soup.find('thead').text
    print(outline)

            #Extracting data from webpage
    trains = soup.find('tbody').text
    print(trains)
    print('\nThank you for using our service :) ')
    print("Have a great day ahead")

    RailMenu()

def TrainCancel():
    ''' This function helps you get details of trains that has been
        cancelled for today '''

    print('------------ Welcome to Indian Railways System -----------\n')
    source = requests.get('https://runningstatus.in/cancelledtrains').text

    soup = BeautifulSoup(source , 'lxml')
                  #Thead is the outline of rows are coded
    info = soup.find('thead').text
    print(info)
                  #List of trains that has been cancelled are

    data = soup.find('tbody').text
    time.sleep(2)
    print('Fetching data.........')
    print('Please wait ! ')
    time.sleep(1)
    print('\nThe following trains are cancelled:')
    time.sleep(1)
    print(data)
    print('Further informations will be put up on bulletin as soon as data gets updated')
    print('\nThank you for using our service :) ')
    print("Have a great day ahead")

    RailMenu()

def TrainSeat():
    ''' This function will help you search for availability of seats
        and will also give details of train '''
    print('------------ Welcome to Indian Railways System -----------\n')

    Src = input('Enter Source Station Code : ')
    Dest = input('\nEnter Destination Station Code : ')
    Day = input('Enter date (DD) : ')
    Mon = input('Enter month (MM) : ')
    Year = input('Enter year YYYY : ')
    print('Available quota are : ')
    print('1.Tatkal --> Code : TQ ')
    print('2.Premium Tatkal --> Code : PT ')
    print('3.Ladies --> Code : LD')
    print('4.Defence --> Code : DF ')
    print('5.Duty Pass --> Code : DP ')
    print('6.Foreign Tourist --> Code : FT ')
    print('7.Lower Berth --> Code : SS')
    print('8.General --> Code : GN')

               # Above parameters will be attached to the website and accordingly results
              # will be generated and shown over here
    Quota = input('\nEnter your quota code : ')
    source = requests.get('https://runningstatus.in/trains/'+Src+'-to-'+Dest+'-on-'+Day+'-'+Mon+'-'+
                          Year+'-quota-'+Quota).text

    soup = BeautifulSoup(source , 'lxml')
    time.sleep(2)
    print('Fetching data.......')
    print('Please Wait !')
    info = soup.find('div', class_='card-header').text
    print(info)
                #Order of information being parsed
    outline = soup.find('thead')
    line = outline.tr.text

    print(line)
                #Extracting data from website
    time.sleep(1)
    data = soup.find('tbody').text
    print(data)
    print('\nThank you for using our service :) ')
    print("Have a great day ahead")

    RailMenu()

def Divert():
    ''' This function will show you how many trains are diverted from their
        respective routes '''
    source = requests.get('https://runningstatus.in/divertedtrains').text
    soup = BeautifulSoup(source , 'lxml')
    print('------------ Welcome to Indian Railways System -----------\n')
    info = soup.find('div', class_='card-header').text
    print(info)

    outline = soup.find('thead').text
    time.sleep(2)
    print(outline)
    print('The following trains are diverted :- ')
    print('\n-----------------------------')
    time.sleep(1)
    data = soup.find('tbody').text
    print(data)
    print('\nThank you for using our service :) ')
    print("Have a great day ahead")

    RailMenu()

def Quit():
    print('Thank you for visiting ! ')
    print("We hope you had a good experience with our services")
    print('Closing system !!!! ')



# Movie Enquiry System

def MovieMenu():
    print("================== Welcome to Movie Enquiry System ======================")
    print("1. Get Movie Shows")
    print("2. Movie Details ")
    print("3. Cast & Crew ")
    print("4. Storyline ")
    print("5. Exit ")
    choice = int(input("\nEnter your choice : "))
    if choice == 1:
        GetShows()
    elif choice == 2:
        Details()
    elif choice == 3:
        Crew()
    elif choice == 4:
        Story()
    elif choice == 5:
        Exit()
    else:
        print('Please enter valid choice ! ')


def GetShows():
    ''' This function will tell about available shows for specified movie '''
    print('------------- Welcome to Movie Booking System -------------- ')
    #change the executable path according to your chrome drivers directory
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\driver\chromedriver.exe', options=options)

    #executable_path=C:\Program Files (x86)\Google\Chrome\driver\chromedriver.exe
    #Set your own chrome driver executable path
    driver.get('https://in.bookmyshow.com/vizag-visakhapatnam')

    #Mention name of the movie with first letter capital
    movie = input("\nEnter name of the movie : ")
    s =driver.find_element_by_xpath("//input[@type='text'][@placeholder='Search for Movies, Events, Plays, Sports and Activities']")

    #sleep is required so that the webpage loads all the elements and our information
    #is parsed properly
    time.sleep(3)
    s.send_keys(movie)
    time.sleep(2)
    s.send_keys(Keys.ENTER) #Keys.ENTER acts as Enter key of our keyboard

    html_list = driver.find_elements_by_id("venuelist")
    if len(html_list) == 0:
        print('No shows are available')
    else:
        print("\nThe following shows are available in respective theaters")
        time.sleep(3)
        html_lists = driver.find_element_by_id("venuelist")
        items = html_lists.find_elements_by_tag_name("li")
        for item in items:
            text = item.text
            print (text)
        time.sleep(2)
    print("\nWe hope you are satisfied with our services")
    print("Thank you and have a great day")

    MovieMenu()

#movie details
def Details():
    ''' This function will provide with details of movie including Box Office Collection '''

    print('------------- Welcome to Movie Booking System -------------- ')
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\driver\chromedriver.exe', options=options)
    driver.get("https://www.imdb.com")

#Mention name of the movie with first letter capital
    movie = input("\nEnter name of the movie : ")
    #Enter first letter of string capital

    s =driver.find_element_by_xpath("//input[@type='text'][@placeholder='Find Movies, TV shows, Celebrities and more...']")
    time.sleep(3)
    s.send_keys(movie)
    time.sleep(2)
    s.send_keys(Keys.ENTER)
    driver.find_element_by_link_text(movie).click()
    time.sleep(3)
     #printing details
    box = driver.find_element_by_id("titleDetails").text
    print(box)
    time.sleep(2)
    print("\nWe hope you are satisfied with our services")
    print("Thank you and have a great day")

    MovieMenu()

#crew details
def Crew():
    ''' This function will list out crew members of movie '''

    print('------------- Welcome to Movie Booking System -------------- ')
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\driver\chromedriver.exe', options=options)

    driver.get('https://in.bookmyshow.com/vizag-visakhapatnam')
    movie = input("Enter name of the movie : ")
    s =driver.find_element_by_xpath("//input[@type='text'][@placeholder='Search for Movies, Events, Plays, Sports and Activities']")
    time.sleep(3)
    s.send_keys(movie)
    time.sleep(2)
    s.send_keys(Keys.ENTER)
    driver.find_element_by_link_text(movie).click()
    time.sleep(5)

    crew=driver.find_element_by_id("cast-carousel").text #parsing crew details
    print(crew)
    time.sleep(1)
    crew2 = driver.find_element_by_xpath('//*[@id="cast-carousel"]/div/button[2]').click()
    time.sleep(3)
    crew_new=driver.find_element_by_id("cast-carousel").text #parsing crew details
    print(crew_new)
    time.sleep(2)
    print("\nWe hope you are satisfied with our services")
    print("Thank you and have a great day")
    MovieMenu()

#story line
def Story():
    ''' This function will provide you with storyline of the movie'''

    print('------------- Welcome to Movie Booking System -------------- ')
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\driver\chromedriver.exe', options=options)

    driver.get("https://www.imdb.com")
    #Mention name of the movie with first letter capital
    movie = input("Enter name of the movie : ")
    st = movie.capitalize()
    s =driver.find_element_by_xpath("//input[@type='text'][@placeholder='Find Movies, TV shows, Celebrities and more...']")
    time.sleep(5)
    s.send_keys(movie)
    time.sleep(5)
    s.send_keys(Keys.ENTER)

    driver.find_element_by_link_text(movie).click()
    time.sleep(5)

    story = driver.find_element_by_xpath("//div[@class='inline canwrap']/p ").text
    print(story)
    time.sleep(2)
    print("\nWe hope you are satisfied with our services")
    print("Thank you and have a great day")

    MovieMenu()

def Exit():
    print("\nIt was great to have you here.")
    print("We Hope you had a good experience with us.")
    print("Thank you for using our services :)")
    print("Exiting program...........")


#__main__
print('_____Welcome_____')
print("\n1- Railway Enquiry System")
print("2- Movie Enquiry System")
ch = int(input("\nWhich system do you want to access (1 or 2)? "))
if ch == 1:
    time.sleep(2)
    print("Accessing Railway Enquiry System......")
    print("Please wait")
    time.sleep(1)
    RailMenu()
elif ch == 2:
    time.sleep(2)
    print("Accessing Movie Enquiry System.......")
    print("Please Wait")
    time.sleep(1)
    MovieMenu()
else:
    print('Invalid Choice !')
    print("Kindly enter valid choice ")













