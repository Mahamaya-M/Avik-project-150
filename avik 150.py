from tkinter import * 
import random 
root = Tk() 
root.geometry("600x600") 
root.title("Country and city game") 

Entry_country = Entry(root) 
Entry_country.place(relx=0.5,rely=0.2,anchor = CENTER) 

Entry_city = Entry(root) 
Entry_city.place(relx=0.5,rely=0.3,anchor = CENTER) 

country_list = Label(root) 
country_list.place(relx = 0.5,rely = 0.5,anchor = CENTER) 

city_list = Label(root) 
city_list.place(relx = 0.5,rely = 0.6,anchor = CENTER) 

country_list_random = Label(root) 
country_list_random.place(relx = 0.5,rely = 0.8,anchor = CENTER) 
city_list_random = Label(root) 
city_list_random.place(relx = 0.5,rely = 0.9,anchor = CENTER) 

country_list1 = [] 
city_list1 = []

def country_city_name(): 
	country_given_name = Entry_country.get() 
	country_list1.append(country_given_name) 
	country_list["text"]="Country Name : "+str(country_list1) 
	city_given_name = Entry_city.get() 
	city_list1.append(city_given_name) 
	city_list["text"]="City Name : "+str(city_list1) 
def random_city_country_name(): 
	n1 = len(country_list1) 
	random_n1 = random.randint(0, n1-1) 
	random_country = country_list1[random_n1] 
	country_list_random["text"]="random country: "+str(random_country) 
	n2 = len(city_list1)
	random_n2 = random.randint(0, n2-1) 
	random_city = city_list1[random_n2] 
	city_list_random["text"]="random city: "+str(random_city) 

btn = Button(root,text = "display country and city name" ,command = country_city_name) 
btn.place(relx = 0.5,rely = 0.4,anchor = CENTER) 
btn1 = Button(root,text = "display random country and city name" ,command = random_city_country_name) 
btn1.place(relx = 0.5,rely = 0.7,anchor = CENTER) 
root.mainloop()