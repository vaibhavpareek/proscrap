import requests
import sys
from bs4 import BeautifulSoup
username= input("Enter Username :  ")
try:
    response = requests.get("https://www.interviewbit.com/profile/"+username)
    if int(response.status_code) != 200:
        print("Response Status code : %s" % response.status_code)
        sys.exit(0)
    soup = BeautifulSoup(data,'html.parser')
    name_list = soup.find_all(class_="name")
    if len(name_list) < 1:
        print("User doesn't exist")
        sys.exit(0)
    name = name_list[0]
    print("Name : ",name.get_text())
    stats = soup.find_all(class_="user-stats")[0]
    stats = list(stats.get_text().split("\n"))
    print("Rank : ",stats[2])
    print("Score : ",stats[6])
    print("Streak : ",stats[10])
    print("Mastered Branhes")
    master = soup.find_all(class_="timeline")[0]
    master = list(master.get_text().split("\n\n"))
    for i in range(2,len(master)):
    	print(master[i])
except Exception as e:
    print(e)
    print("Might be issue with the username (Try Again)")
