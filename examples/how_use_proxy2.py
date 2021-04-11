############################################################################
#
#   how_use_proxy2.py
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import requests, random

if __name__ == '__main__':
    #
    ###
    with open('trusted_proxy_list.txt', 'r') as rfile:
        proxy_txt = rfile.read()
        tmp_list = proxy_txt.split(sep='\n')
        proxies = tmp_list[3:-1]
    #
    ###
    proxy = random.choice(proxies)
    proxy_input = { 'http': proxy,
                    'https': proxy}
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0"
    }
    http_host = "http://httpbin.org/anything"
    timeout = 3
    #
    #
    try:
        response_https = requests.get(url=http_host, headers=headers, proxies=proxy_input, timeout=timeout)
        if response_https.status_code == 200:
            print('\n')
            print(response_https.text)
    except:
        print(f"\t[https] '{proxy}' problemli olabilir!" )
