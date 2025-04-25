
#------------[ AUTO CREATE FACEBOOK. ]--------------#
#------------[ ORIGINAL WRITTTEN BY Reborn]--------------#
#------------[ Reborn Bëb]--------------#

import os, sys, re, time, json
import requests, bs4, random
from faker import Faker
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# Define missing variables
status_color = "\033[1;32m"  # Green color
random_status = random.choice(["Running", "Stable", "Under Test"])
run_count = 1

#------------[ WARNA-COLOR ]--------------#
BLUE = '\x1b[38;5;196m'
WHITE = '\x1b[37m'
P = '\x1b[1;97m'
M = '\x1b[38;5;196m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[38;5;196m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m'
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'
asu = random.choice([m,k,h,u,b])

Z = "\x1b[0;90m"
M = "\x1b[38;5;196m"
H = "\x1b[38;5;46m"
K = "\x1b[38;5;226m"
B = "\x1b[38;5;44m"
U = "\x1b[0;95m"
O = "\x1b[0;96m"
P = "\x1b[38;5;231m"
J = "\x1b[38;5;208m"
A = "\x1b[38;5;248m"

COLOR_BLACK="\033[0;30m"
COLOR_RED="\033[0;31m"
COLOR_GREEN="\033[0;32m"
COLOR_BROWN="\033[0;33m"
COLOR_BLUE="\033[0;34m"
COLOR_PURPLE="\033[0;35m"
COLOR_CYAN="\033[0;36m"
COLOR_LIGHT_GRAY="\033[0;37m"
COLOR_DARK_GRAY="\033[1;30m"
COLOR_LIGHT_RED="\033[1;31m"
COLOR_LIGHT_GREEN="\033[1;32m"
COLOR_YELLOW="\033[1;33m"
COLOR_LIGHT_BLUE="\033[1;34m"
COLOR_LIGHT_PURPLE="\033[1;35m"
COLOR_LIGHT_CYAN="\033[1;36m"
COLOR_LIGHT_WHITE="\033[1;37m"
COLOR_BOLD="\033[1m"
COLOR_FAINT="\033[2m"
COLOR_ITALIC="\033[3m"
COLOR_UNDERLINE="\033[4m"
COLOR_BLINK="\033[5m"
COLOR_NEGATIVE="\033[7m"
COLOR_CROSSED="\033[9m"

ua = UserAgent()

# Use a predefined list of user agents (instead of generating random ones each time)
user_agents = [
    "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Infinix X682C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.107 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.112 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX2185) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6280.78 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; TECNO KG5j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3938 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX5000 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3938 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3938 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3938 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; 24053PY09C ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.92 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; 21121210C ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.92 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; 2405CRPFDG ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.100 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; M2006C3LII ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; M2006C3LII ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; M2006C3LII ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6943.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2006C3LII ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2006C3LII ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11.1.1; Redmi 9I ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K7AI ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K7AI ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K7AI ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K7AG ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K7AG ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 4.2.2; uk-ua; GT-I8200 ) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 4.2.2; pt-pt; GT-I8200N ) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 4.2.2; pt-pt; GT-I8200N ) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 13; SM-G980F ) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/130.0.6723.24 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G980F ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G980F ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G980F ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.162 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G980F ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G980F ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G980F ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G980F ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G980F ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G980F ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G980F ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1923 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.261 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1923 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1923 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.122 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1923 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.103 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2104 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2104 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2104 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2104 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2104 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2104 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2104 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2104 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2104 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2104 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; V2104 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3372 ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36 T7/15.0 SP-engine/3.27.0 baiduboxapp/15.0.0.10 (Baidu; P1 13) NABar/1.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2503.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.13 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4043.US Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 LBBROWSER",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.1000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; ASJB; ASJB; MAAU; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; BOIE9;ENUSSEM; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; MDDRJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
    "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; MASMJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.6.2000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (X11; CrOS x86_64 6457.107.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS x86_64 7077.95.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.90 Safari/537.36"
    
]

# List of proxies (you can extend this list with your proxy pool)
proxies = [
    "http://123.45.67.89:8080",
    "http://98.76.54.32:1080",
    "http://54.23.12.67:3128",
    "http://203.112.68.1:80",
]

# Function to return a random user agent from the list
def ugenX():
    return random.choice(user_agents)

# Function to return a random proxy from the list

def fake_name():
    first = Faker().first_name()
    last = Faker().last_name()
    return first, last

def extractor(data):
    soup = BeautifulSoup(data, "html.parser")
    data = {}
    for inputs in soup.find_all("input"):
        name = inputs.get("name")
        value = inputs.get("value")
        if name:
            data[name] = value
    return data

logo = f"""
\033[1;37m
   _____      _                       
 |  __ \    | |                      
 | |__) |___| |__   ___  _ __ _ __   
 |  _  // _ \ '_ \ / _ \| '__| '_ \  
 | | \ \  __/ |_) | (_) | |  | | | | 
 |_|  \_\___|_.__/ \___/|_|  |_| |_|    \x1b[38;5;196mXD\x1b[37m
                                                                              
\033[1;37m=============================================
\033[1;37m [+]Owner   : \033[32mReborn\033[1;37m
\033[1;37m [+]Facebook: {status_color} Reborn Bëb{status_color}Uchida
\033[1;37m [+]STATUS  : {status_color}{random_status}\033[1;37m
\033[1;37m [+]Github  : \033[33mAuto Create\033[1;37m       
\033[1;37m [+]Version : 0.1
\033[1;37m [+]Run Count: {run_count}
\033[1;37m============================================="""

def linex():
    print('\033[1;37m=============================================')

def clear():
    os.system('clear')
    print(logo)

A = '\x1b[1;97m'
B = '\x1b[1;96m'
C = '\x1b[1;91m'
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'
E = '\x1b[1;93m'
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

X = '\033[1;37m'
R = '\033[1;31m'

oks = []
cps = []

def main():
    clear()
    xd = input(f"{X} 1. auto create: ")
    if xd == '1':
        print(linex())
    else:
        print('Put valid number ')
    
    for make in range(100):
        ses = requests.Session()
        
        # Set proxy for the session
        try:
            response = ses.get("https://x.facebook.com/reg", timeout=10)
        except requests.exceptions.RequestException as e:
            continue

        form = extractor(response.text)
        firstname, lastname = fake_name()
        email2 = f"{firstname.lower()}{random.randint(1000,9999)}@gmail.com"
        print(f"{X} NAME  - {G}{firstname} {lastname}")
        print(f"{X} EMAIL - {G}{email2}")

        payload = {
            'ccp': "2",
            'reg_instance': form.get("reg_instance", ""),
            'submission_request': "true",
            'reg_impression_id': form.get("reg_impression_id", ""),
            'ns': "1",
            'logger_id': form.get("logger_id", ""),
            'firstname': firstname,
            'lastname': lastname,
            'birthday_day': str(random.randint(1, 28)),
            'birthday_month': str(random.randint(1, 12)),
            'birthday_year': str(random.randint(1992, 2009)),
            'reg_email__': email2,
            'sex': "2",
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0], "Reborn@123"),
            'submit': "Sign Up",
            'fb_dtsg': form.get("fb_dtsg", ""),
            'jazoest': form.get("jazoest", ""),
            'lsd': form.get("lsd", "")
        }

        headers = {
            "Host": "m.facebook.com",
            "Connection": "keep-alive",
            "User-Agent": ugenX(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9"
        }

        reg_url = "https://www.facebook.com/reg/submit/"
        reg_submit = ses.post(reg_url, data=payload, headers=headers)

        if "c_user" in ses.cookies.get_dict():
            uid = ses.cookies.get_dict()["c_user"]
            cookie = ";".join([f"{key}={val}" for key, val in ses.cookies.get_dict().items()])
            print(f"{X} SUCCESS - {G}{uid}|Reborn@123|{cookie}")
            open("/sdcard/SUCCESS-OK-ID.txt", "a").write(uid+"|Reborn@123|"+cookie+"\n")
        else:
            print(f"{X} {R}CHECKPOINT OR FAILED")
        linex()

if __name__ == "__main__":
    main()
