import json;
import requests;

num=0.1;
x=0;
usr_input=input("Enter the country name you had like to check: ")

res = requests.get('https://www.skillsafrica.org/json/countries.json');
data= res.json();

for x in range(len(data)):
    if(data[x]['name']==usr_input):
        print("The country name is "+data[x]['name']+" and the total population is "+str(data[x]['total_population'])+" million!")
        break
else:
    print("There is no country named "+usr_input+" in my list. Are you sure there is country in africa with this name?")

for i in range(len(data)):
    if float(data[i]['total_population'])>float(num):
        name= data[i]['name'];
        num= data[i]['total_population'];


print("The country with the biggest population is "+ name +" with "+str(num)+" million citizans!!!");