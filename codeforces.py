import requests
import sys
from bs4 import BeautifulSoup
username = input("Enter Username :  ")
try:
    response = requests.get("https://codeforces.com/profile/"+str(username))
    status_code = response.status_code
    if int(status_code) != 200:
        print("Response Status code : %s"%status_code)
        sys.exit(0)
    data = response.text
    soup = BeautifulSoup(data,'html.parser')
    lilen = len(soup.find_all('li'))
    padding = lilen-48;
    rank=soup.find_all(class_="user-rank")
    if len(rank) < 1:
        print("User doesn't exist")
        sys.exit(0)
    rank=soup.find_all(class_="user-rank")[0]
    print("User Ranking : ", rank.get_text().split("\n")[1])
    rating = soup.find_all('li')[41+padding]
    rating = rating.get_text().split("\r")[4].split("\n")[1]
    contrib = soup.find_all('li')[42+padding]
    contrib = contrib.get_text().split("\r")[4].split("\n")[1]
    print("Contest Rating : ", rating.strip(" "))
    print("Contribution : ", contrib.strip(" "))
except Exception as err:
    print("Error : %s" % err)
    print("Might be issue with the username (Try Again)")
