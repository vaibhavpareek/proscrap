import requests
from bs4 import BeautifulSoup
username= input("Enter Username :  ")
try:
	data = requests.get("https://www.codechef.com/users/"+str(username)).text
	soup = BeautifulSoup(data,'html.parser')
	problems=soup.find_all(class_="rating-data-section problems-solved")[0]
	rating = soup.find_all(class_="rating-number")[0]
	rating_star = soup.find_all(class_="rating-star")[0]
	print("User Ranking : ",rating.get_text())
	print("User Star : ",rating_star.get_text())
	full_q = int(str(problems.find_all('h5')[0].get_text()).split(" ")[2].split("(")[1].split(")")[0])
	part_q = int(str(problems.find_all('h5')[1].get_text()).split(" ")[2].split("(")[1].split(")")[0])
	print("Total Questions : ",str(full_q+part_q))
	print("Fully Solved Questions : ",full_q)
	print("Partially Solved Questions : ",part_q)
except:
	print("Might be issue with the username (Try Again)")