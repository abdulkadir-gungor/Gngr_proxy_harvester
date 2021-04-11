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
from  Get_Proxies_List import save_all_proxies
from  Find_Trusted_Proxies import save_checked_proxies
import os

# Ekranı Temizlemek için
def screenClear():
    print("\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n") # Konsol dışı kullanımda ekranı temizlemek için
    # clear screen
    # ********************
    # Windows
    if os.name=='nt':
        os.system('cls')
    # Linux or MAC
    elif os.name=='posix':
        os.system('clear')
    # ********************
    print("")

def screenWrite():
    print()
    print('\t#####################################################')
    print('\t#/*************************************************\#')
    print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||         Gngr Proxy Harvester v1.0         ||**#')
    print('\t#**||                04/2021                    ||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||       Developer: Abdulkadir GÜNGÖR        ||**#')
    print('\t#**||       (abdulkadir_gungor@outlook.com)     ||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
    print('\t#\*************************************************/#')
    print('\t#####################################################')
    print()
    print()


if __name__ == '__main__':
    screenClear()
    screenWrite()
    save_all_proxies()
    save_checked_proxies()
