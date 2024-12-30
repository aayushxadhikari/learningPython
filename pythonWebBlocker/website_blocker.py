import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"/etc/hosts "
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com", "www.twitter.com"]

while True:
    if dt(dt.now().year, dt.now().month,dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working Hours....")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in website_list:
                    if website in content:
                        pass 
                    else:
                        file.write(redirect+""+website+"\n")
    else: 
        print("Fun hours.....")
    print(1)
    time.sleep(5)