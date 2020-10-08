import requests
import wget
import os
import sys

print("*******************************")
print("****BDIX tester by shantanu****")
print("*******************************\n")

file =  os.path.join(sys.path[0], "bdix_url_local.txt")
if os.path.exists(file) == False:
    url = "https://raw.githubusercontent.com/Shantanu2645/BDIX_Tester_py/main/BDIX_url.txt"
    wget.download(url,file)
url_list = open(os.path.join(sys.path[0], "bdix_url_local.txt"),'r+')


timer = int(input("Enter timeout based on your internet speed (second): "))

bdix_list = url_list.read().split()

url_list.close()

count = len(bdix_list)
print("\nSearching from",len(bdix_list),"sites\n")
print("\nThis BDIX servers will work for your ISP:-\n")
bdix_list_final = []

for i in bdix_list:
    count = count - 1
    try:
        request_response = requests.head(i,timeout=timer)
        
        if request_response.status_code == 200 :
            bdix_list_final.append(i)
            out = i + "   ("+str(count)+" remaining)"
            print(out)
            
    except requests.exceptions.Timeout: 
        pass
    except requests.exceptions.ConnectionError:
        pass
    except KeyboardInterrupt:
        print("\nexit")
        break

final_urls = open(os.path.join(sys.path[0], "data.txt"),"w+")



final_urls.write

for i in bdix_list_final:
    
    final_urls.write(i+"\n")

final_urls.close()

print("\nFetched",len(bdix_list_final),"sites\n")
print("\nCheck 'data.txt' file for working URLS\nEnjoy!! \nCreated and Maintained By Shantanu Dey Anik")
print("\nFacebook: www.facebook.com/shantanu.anik.dey ")

