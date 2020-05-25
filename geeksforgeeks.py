import requests
from bs4 import BeautifulSoup
username= input("Enter Username :  ")
try:
	data = requests.get("https://auth.geeksforgeeks.org/user/"+str(username)).text
	soup = BeautifulSoup(data,'html.parser')
	name = soup.find_all(class_="mdl-cell mdl-cell--9-col mdl-cell--12-col-phone textBold medText")[0]
	institute = soup.find_all(class_="mdl-cell mdl-cell--9-col mdl-cell--12-col-phone textBold")[0]
	det = soup.find_all(class_="mdl-cell mdl-cell--5-col mdl-cell--12-col-phone whiteBgColor mdl-shadow--2dp")[0]
	lang = soup.find_all(class_="mdl-cell mdl-cell--5-col mdl-cell--12-col-phone whiteBgColor mdl-shadow--2dp")[1]
	print("Name : ",str(name.get_text()))	
	print("Institute : ",str(institute.get_text()))
	count=0
	print()
	for i in str(det.get_text()).split(" "):
		count+=1
		if(count==128):
			print("\nTotal Questions Solved : ",i.split("'")[0])
		if(count==1393):
			cat= list(i.split("[")[1].split(","))
			print("\nCategories Wised Questions: ")
			print("School : ",cat[0])
			print("Basic : ",cat[1])
			print("Easy : ",cat[2])
			print("Medium : ",cat[3])
			print("Hard : ",cat[4].split("]")[0])
	print("\nLanguage Wise Categories")
	count=1
	data=[]
	languages=[]
	for j in list(lang.get_text().split(" ")):
		if(count==907):
			data.append(list(j.split("[")[1].split(",")))
			break
		if(count==713):
			languages.append(list(j.split("[")[1].split(",")))
		count += 1
	for (dt,lg) in zip(data[0][:-1],languages[0][:-1]):
		print(dt.split("]")[0]," : " ,lg.split("]")[0])
except Exception as e:
	print(e)
	print("Might be issue with the username (Try Again)")