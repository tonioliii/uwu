from fileinput import close
from requests import post
from time import sleep
from colorama import init,Fore
from slow_write import slow_write
from someone import *
from random import randint
init()

consol_config = False
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSf_khA3zMidgvyivfIQEHVF_LX91Xs6lUgdE1Ggg-6zJPfvuA'

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

print(Fore.LIGHTRED_EX)
slow_write("uwu",0.25)
print(Fore.BLUE)
slow_write("Created By Someone.\n",0.05)
slow_write("Educational purpose only.\n",0.05)

if consol_config == False:
    delay = "60/120".split("/")
    mindelay = int(delay[0])
    maxdelay = int(delay[1])
    packets_number = 1000000
else:
    slow_write("How many sec do you want to add to the delay ? ('mindelay/maxdelay')", 0.02)
    try:
        delay = input("\n").split("/")
        mindelay = int(delay[0])
        maxdelay = int(delay[1])
    except:
        slow_write("This is not a number.",0.05)
        close()
    slow_write("How many do you want to send ?", 0.05)
    try:
        packets_number = int(input("\n"))
    except:
        slow_write("This is not a number.",0.05)
        close()

print(Fore.WHITE)

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

i=0
url = form_url + '/formResponse'
user_agent ={
	'Referer': form_url + '/viewform',
	'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"
	}

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #

for x in range(packets_number):
    chose_someone()
    get_class()
    if get_class() == "3EME1":
        classs = "3*1"
    if get_class() == "3EME2":
        classs = "3*2"
    if get_class() == "3EME3":
        classs = "3*3"
    if get_class() == "3EME4":
        classs = "3*4"
    if get_class() == "3EME5":
        classs = "3*5"
    if get_class() == "3EME6":
        classs = "3*6"
    form_data = {
	'entry.1209189870': get_last_name(),
	'entry.473617258': get_first_name(),
    'entry.380365974': classs,
    'entry.1618003438': 'je ne serai pas là😖😖'
    }
    i=i+1
    try:
        r = post(url, data=form_data, headers=user_agent)
        print(Fore.LIGHTRED_EX + "<3 " + Fore.YELLOW + str(r) + Fore.WHITE +'   Total Count = ' + Fore.LIGHTGREEN_EX + str(i) + Fore.CYAN + "   " + get_last_name() + " " + get_first_name() + Fore.WHITE + " From "+ Fore.CYAN + get_class() + Fore.RED + " Just send a packet..." + Fore.WHITE)

    except:
        slow_write("Somethings went wrong. You are probably not connected to the internet.\n",0.05)
    else:
        waiting_time = randint(mindelay,maxdelay)
        print ("Waiting " + str(randint(mindelay,maxdelay)) + "sec")
        sleep(waiting_time)

input("Done.")