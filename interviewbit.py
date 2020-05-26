import requests
from bs4 import BeautifulSoup
username= input("Enter Username :  ")
try:
	data = requests.get("https://www.interviewbit.com/profile/"+str(username)).text
	soup = BeautifulSoup(data,'html.parser')
	name = soup.find_all(class_="name")[0]
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