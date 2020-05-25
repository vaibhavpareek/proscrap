import requests
from bs4 import BeautifulSoup
username= input("Enter Username :  ")
try:
	data = requests.get("https://codeforces.com/profile/"+str(username)).text
	soup = BeautifulSoup(data,'html.parser')
	lilen = len(soup.find_all('li'))
	print(lilen)
	padding = lilen-48;
	rank=soup.find_all(class_="user-rank")[0]
	print("User Ranking : ",str(rank.get_text()).split("\n")[1])
	rating = soup.find_all('li')[41+padding]
	rating = str(rating.get_text()).split("\r")[4].split("\n")[1]
	contrib = soup.find_all('li')[42+padding]
	contrib = str(contrib.get_text()).split("\r")[4].split("\n")[1]
	print("Contest Rating : ",str(rating).strip(" "))
	print("Contribution : ",contrib.strip(" "))
except Exception as e:
	print(e)
	print("Might be issue with the username (Try Again)")