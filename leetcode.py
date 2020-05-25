import requests
from bs4 import BeautifulSoup
username= input("Enter Username :  ")
try:
	data = requests.get("https://leetcode.com/"+str(username)).text
	soup = BeautifulSoup(data,'html.parser')
	problems = soup.find_all(class_="badge progress-bar-success")[1]
	accept = soup.find_all(class_="badge progress-bar-info")[0]
	points = soup.find_all(class_="badge progress-bar-success")[3]
	username = soup.find_all(class_="username")[0]
	problems = str(problems.get_text()).split("\n")[1].split(" ")[-3:]	
	accept = str(accept.get_text()).split("\n")[1].split(" ")[-2:]
	points = str(points.get_text()).split("\n")[1].split(" ")[-2:]
	username = str(username.get_text()).split("\n")[1].split(" ")[-1:][0]
	accept = ''.join(accept)
	problems = ''.join(problems)
	points = ''.join(points)
	print("Name : ", str(username))
	print("Total Questions : ",str(problems))
	print("Acceptance Rate : ",str(accept))
	print("Points : " , str(points))
except:
	print("Might be issue with the username (Try Again)")