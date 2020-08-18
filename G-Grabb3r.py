import requests
import re
import os
from time import sleep
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)
from  colorama import Fore, Style, init
init(autoreset=True)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
try:
    os.makedirs('result', exist_ok=True)
except:
    pass


def check(url):
    url = url.lstrip('http')
    if ' ' not in url or '<br>' not in url:
        return True
    else:
        return False




def google_url_scrap(data):
    valid_urls = []
    urls = re.findall('<div class="r"><a href="(.*?)" ping="/url', data)

    for url in urls:
        validity = check(url)
        if validity:
            valid_urls.append(url)
    with open('result/google-grabbed-urls.txt', 'a') as w:
        for valid_url in valid_urls:
            valid_url = valid_url.replace('amp;', '')
            print(f'{Fore.GREEN}[Google-Grabb3r]{Style.RESET_ALL}', valid_url)
            w.write(valid_url+'\n')


def query_submit(query):
    while True:
        try:
            r = requests.get(query, headers=headers, verify=False, timeout=15)
        except:
                print(f"{Fore.RED}[Connection]{Style.RESET_ALL} Connection Problem - Please Change Your Proxy")
                sleep(10)
                continue
        else:
            if '<div id="recaptcha"' in r.text:
                print(f"{Fore.RED}[Re-Captcha]{Style.RESET_ALL} Recaptcha Comes - Please Change Your Proxy")
                sleep(10)
                continue

            else:
                google_url_scrap(r.text)
                break



def google_grabber(search_value):
    start_range = ['0', '100', '200']
    for srange in start_range:
        query = "http://www.google.co.uk/search?q="+search_value+"&num=100&start="+srange+"&filter=1"
        query_submit(query)



def main():
    print(f"""
   ██████╗        ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
  ██╔════╝       ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚════██╗██╔══██╗
  ██║  ███╗█████╗██║  ███╗██████╔╝███████║██████╔╝██████╔╝ █████╔╝██████╔╝
  ██║   ██║╚════╝██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗ ╚═══██╗██╔══██╗
  ╚██████╔╝      ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝██████╔╝██║  ██║
   ╚═════╝        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝
                                                                        
                                 {Fore.GREEN}Github{Style.RESET_ALL}: github.com/Hun73rCL4W/G-Grabb3r
""")
    filename = input('  Enter list of dork => ')
    dorks = open(filename).read().splitlines()
    for dork in dorks:
        google_grabber(dork)


if __name__ == '__main__':
    main()
