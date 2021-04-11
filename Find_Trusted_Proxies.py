############################################################################
#
#   Find_Trusted_Proxies.py
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import requests, time


def get_checked_proxies(proxy_list, timeout=0.5, request_host='www.google.com' ):
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0"
    }
    checked_proxies = []
    total = 0
    #
    print('\n\n')
    #
    for proxy in proxy_list:
        http_result = False
        https_result = False
        #
        http_host = "http://{}".format(request_host)
        https_host = "https://{}".format(request_host)
        proxies = {'http': proxy,
                   'https': proxy}
        #
        try:
            response_http = requests.get(url=http_host, headers=headers, proxies=proxies, timeout=timeout)
            if response_http.status_code == 200:
                http_result = True
        except:
            pass
        #
        try:
            response_https = requests.get(url=https_host, headers=headers, proxies=proxies,  timeout=timeout)
            if response_https.status_code == 200:
                https_result = True
        except:
            pass
        #
        if http_result and https_result:
            if  proxy not in checked_proxies:
                checked_proxies.append(proxy)
                total += 1
                print('\n\t{} adet proxy doğrulandı.'.format(total))
                print("\t{} \t\t\t http:{} - https:{}\n".format(proxy, str(http_result), str(https_result)))
            else:
                print("\t{} \t\t\t http:{} - https:{}".format(proxy, str(http_result), str(https_result)))
        else:
            print("\t{} \t\t\t http:{} - https:{}".format(proxy, str(http_result), str(https_result)))
    #
    print('\tToplam {} adet proxy bulundu.'.format(total) )
    #
    return checked_proxies

#
def save_checked_proxies(read_filename = 'untrusted_proxy_list.txt',write_filename = 'trusted_proxy_list.txt' , timeout=0.5 ,request_host='www.google.com' ):
    #
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0"
    }
    checked_proxies = []
    total = 0
    #
    print('\n\n')
    #
    with open(file=read_filename, mode='r') as rfile:
        with open(file=write_filename, mode='w') as wfile:
            timestr = time.strftime("%d/%m/%Y %H:%M:%S")
            file_not = f"# '{timestr}' itibariyle proxyler taranmaya başlandı.\n"
            #
            wfile.write('#\n')
            wfile.write(file_not)
            wfile.write('#\n')
            #
            proxy_list = rfile.readlines()
            for proxy in proxy_list:
                proxy = proxy.strip()
                if proxy != '':
                    if proxy[0:1] != '#':
                        #
                        http_result = False
                        https_result = False
                        #
                        http_host = "http://{}".format(request_host)
                        https_host = "https://{}".format(request_host)
                        proxies = {'http': proxy,
                                   'https': proxy}
                            #
                        try:
                            response_http = requests.get(url=http_host, headers=headers, proxies=proxies, timeout=timeout)
                            if response_http.status_code == 200:
                                http_result = True
                        except:
                            pass
                        #
                        try:
                            response_https = requests.get(url=https_host, headers=headers, proxies=proxies,  timeout=timeout)
                            if response_https.status_code == 200:
                                https_result = True
                        except:
                            pass
                        #
                        if http_result and https_result:
                            if proxy not in checked_proxies:
                                checked_proxies.append(proxy)
                                #
                                wfile.write(proxy)
                                wfile.write('\n')
                                wfile.flush()
                                #
                                total += 1
                                print('\n\t{} adet proxy doğrulandı.'.format(total))
                                print("\t{} \t\t\t http:{} - https:{}\n".format(proxy, str(http_result), str(https_result)))
                            else:
                                print("\t{} \t\t\t http:{} - https:{}".format(proxy, str(http_result), str(https_result)))
                        else:
                            print("\t{} \t\t\t http:{} - https:{}".format(proxy, str(http_result), str(https_result)))
            #
            print('\tBulunan {} adet proxy "{}" dosyasına kaydedildi.'.format(total, write_filename))

