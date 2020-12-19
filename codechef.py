import requests
import sys
from bs4 import BeautifulSoup
username= input("Enter Username :  ")
try:
    response = requests.get("https://www.codechef.com/users/%s" % username)
    if int(response.status_code) != 200:
        print("Response Code : %s"%response.status_code)
        sys.exit(0)
    data = response.text 
    soup = BeautifulSoup(data,'html.parser')
    rating = soup.find_all(class_="rating-number")
    if len(rating) < 1:
        print("User doesn't exist")
        sys.exit(0)
    rating = rating[0]
    problems=soup.find_all(class_="rating-data-section problems-solved")[0]
    rating_star = soup.find_all(class_="rating-star")[0]
    print("User Ranking : ",rating.get_text())
    print("User Star : ",rating_star.get_text())
    full_q = int(str(problems.find_all('h5')[0].get_text()).split(" ")[2].split("(")[1].split(")")[0])
    part_q = int(str(problems.find_all('h5')[1].get_text()).split(" ")[2].split("(")[1].split(")")[0])
    print("Total Questions : ", full_q+part_q)
    print("Fully Solved Questions : ",full_q)
    print("Partially Solved Questions : ",part_q)
except Exception as err:
    print("Error : %s" % err)
    print("Might be issue with the username (Try Again)")
