############################################################################
#
#   Get_Proxies_List.py
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import requests, time


### https://www.sslproxies.org/
def get_proxies_www_sslproxies_org():
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0"
    }
    response = requests.get('https://www.sslproxies.org', headers=headers)
    return  (response.text).split(sep='\n')[3:103]

### https://free-proxy-list.net/
def get_proxies_www_free_proxy_list_net():
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0"
    }
    response = requests.get('https://free-proxy-list.net/', headers=headers)
    return (response.text).split(sep='\n')[3:303]

### https://www.us-proxy.org/
def get_proxies_www_us_proxy_org():
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0"
    }
    response = requests.get('https://www.us-proxy.org/', headers=headers)
    return (response.text).split(sep='\n')[3:203]

### http://spys.me/proxy.txt
def get_proxies_spys_me():
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0"
    }
    response = requests.get('http://spys.me/proxy.txt', headers=headers)
    result_lines = response.text.split(sep='\n')[9:-2]
    proxies = []
    for line in result_lines:
        line_s = line.split(sep=' ')
        if len(line_s) == 4:
            proxies.append(line_s[0])
    return proxies

### https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all
def get_proxies_api_proxyscrape_com():
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0"
    }
    response = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all')
    return response.text.split(sep='\r\n')[:-1]

###
def get_all_proxies():
    proxies = []
    #
    tmp_proxies = get_proxies_www_sslproxies_org()
    print('\n\t{:<4} adet proxy bulundu. [https://www.sslproxies.org/]'.format(len(tmp_proxies)))
    proxies += tmp_proxies
    #
    tmp_proxies = get_proxies_www_free_proxy_list_net()
    print('\t{:<4} adet proxy bulundu. [https://free-proxy-list.net/]'.format(len(tmp_proxies)))
    proxies += tmp_proxies
    #
    tmp_proxies = get_proxies_www_us_proxy_org()
    print('\t{:<4} adet proxy bulundu. [https://www.us-proxy.org/]'.format(len(tmp_proxies)))
    proxies += tmp_proxies
    #
    tmp_proxies = get_proxies_spys_me()
    print('\t{:<4} adet proxy bulundu. [http://spys.me/proxy.txt]'.format(len(tmp_proxies)))
    proxies += tmp_proxies
    #
    tmp_proxies = get_proxies_api_proxyscrape_com()
    print('\t{:<4} adet proxy bulundu. [https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all]'.format(len(tmp_proxies)))
    proxies += tmp_proxies
    #
    print('\n\n\tBulunan Toplam Proxy Adedi : {}'.format(len(proxies)) )
    return  proxies


###
def save_all_proxies(filename='untrusted_proxy_list.txt'):
    proxies = []
    #
    tmp_proxies = get_proxies_www_sslproxies_org()
    print('\n\t{:<4} adet proxy bulundu. [https://www.sslproxies.org/]'.format(len(tmp_proxies)))
    proxies += tmp_proxies
    #
    tmp_proxies = get_proxies_www_free_proxy_list_net()
    print('\t{:<4} adet proxy bulundu. [https://free-proxy-list.net/]'.format(len(tmp_proxies)))
    proxies += tmp_proxies
    #
    tmp_proxies = get_proxies_www_us_proxy_org()
    print('\t{:<4} adet proxy bulundu. [https://www.us-proxy.org/]'.format(len(tmp_proxies)))
    proxies += tmp_proxies
    #
    tmp_proxies = get_proxies_spys_me()
    print('\t{:<4} adet proxy bulundu. [http://spys.me/proxy.txt]'.format(len(tmp_proxies)))
    proxies += tmp_proxies
    #
    tmp_proxies = get_proxies_api_proxyscrape_com()
    print('\t{:<4} adet proxy bulundu. [https://api.proxyscrape.com/?request=getproxies&proxytype=all&country=all&ssl=all&anonymity=all]'.format(len(tmp_proxies)))
    proxies += tmp_proxies
    #
    print('\n\n\tBulunan Toplam Proxy Adedi : {}'.format(len(proxies)) )
    #
    with open(file=filename, mode='w') as wfile:
        timestr = time.strftime("%d/%m/%Y %H:%M:%S")
        file_not = f"# '{timestr}' itibariyle {len(proxies)} adet proxy bulundu.\n"
        #
        wfile.write('#\n')
        wfile.write(file_not)
        wfile.write('#\n')
        #
        for proxy in  proxies:
            wfile.write(proxy)
            wfile.write('\n')
        wfile.flush()
    print('\tBulunan {} adet proxy "{}" dosyasına kaydedildi.'.format(len(proxies), filename) )
