from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
import csvPandas as cv
from pandastable import Table, TableModel
import time
import googlemapsLinkGen as gmaps

def close_menus():
	...

def show_menus():
	...


resources = []

def cleanup_resources():
	global resources
	for resource in resources:
		resource.destroy()

def create_hotel_frame():
	cleanup_resources()
	hotel_frame = Frame(root, height = 2000, bg = 'lavender')
	hotel_tag = Label(hotel_frame, text =  'Selected location: ', bg = 'lavender', font = "Arial, 20")
	hotel_tag.place(x = 30, y = 30, anchor = W)
	hotel_name_label = Label(hotel_frame, text = 'Hotel Name', bg = 'lavender', font = "Arial, 20")
	hotel_name_label.place(x = 200, y = 100, anchor=CENTER)
	hotel_rating_label = Label(hotel_frame, text = 'Rating', bg = 'lavender', font = "Arial, 20")
	hotel_rating_label.place(x = 400, y = 100, anchor=CENTER)
	hotel_price_label = Label(hotel_frame, text = 'Price (per night)', bg = 'lavender', font = "Arial, 20")
	hotel_price_label.place(x = 1400, y = 100, anchor=CENTER)
	hotel_frame.pack(side=TOP, fill=BOTH, expand=False)
	resources.append(hotel_frame)
	resources.append(hotel_tag)
	return hotel_frame, hotel_tag

def create_restaurant_frame():
	cleanup_resources()
	restaurant_frame = Frame(root, height = 2000, bg = 'lavender')
	restaurant_tag = Label(restaurant_frame, text =  'Selected location: ', bg = 'lavender', font = "Arial, 20")
	restaurant_tag.place(x = 30, y = 30, anchor = W)
	restaurant_name_label = Label(restaurant_frame, text = 'Restaurant Name', bg = 'lavender', font = "Arial, 20")
	restaurant_name_label.place(x = 200, y = 100, anchor=CENTER)
	restaurant_rating_label = Label(restaurant_frame, text = 'Rating', bg = 'lavender', font = "Arial, 20")
	restaurant_rating_label.place(x = 550, y = 100, anchor=CENTER)
	restaurant_review_count_label = Label(restaurant_frame, text = 'Number of Reviews', bg = 'lavender', font = "Arial, 20")
	restaurant_review_count_label.place(x = 900, y = 100, anchor=CENTER)
	restaurant_review_quote_label = Label(restaurant_frame, text = 'Average spending (per person)', bg = 'lavender', font = "Arial, 20")
	restaurant_review_quote_label.place(x = 1300, y = 100, anchor=CENTER)
	restaurant_frame.pack(side=TOP, fill=BOTH, expand=False)
	resources.append(restaurant_frame)
	resources.append(restaurant_tag)
	return restaurant_frame, restaurant_tag

def create_attractions_frame():
	cleanup_resources()
	attractions_frame = Frame(root, height = 2000, bg = 'lavender')
	attractions_tag = Label(attractions_frame, text =  'Selected location: ', bg = 'lavender', font = "Arial, 20")
	attractions_tag.place(x = 30, y = 30, anchor = W)
	attractions_name_label = Label(attractions_frame, text = 'Attraction Name', bg = 'lavender', font = "Arial, 20")
	attractions_name_label.place(x = 200, y = 100, anchor=CENTER)
	attractions_rating_label = Label(attractions_frame, text = 'Rating', bg = 'lavender', font = "Arial, 20")
	attractions_rating_label.place(x = 600, y = 100, anchor=CENTER)
	attractions_review_count_label = Label(attractions_frame, text = 'Number of Reviews', bg = 'lavender', font = "Arial, 20")
	attractions_review_count_label.place(x = 1000, y = 100, anchor=CENTER)
	attractions_price_label = Label(attractions_frame, text = 'Attraction Type', bg = 'lavender', font = "Arial, 20")
	attractions_price_label.place(x = 1400, y = 100, anchor=CENTER)
	attractions_frame.pack(side=TOP, fill=BOTH, expand=False)
	resources.append(attractions_frame)
	resources.append(attractions_tag)
	return attractions_frame, attractions_tag

last_pt = None
def search():
	global last_pt
	if last_pt is not None:
		last_pt.destroy()
		last_pt.close()

	selected_category = chosen_category.get()
	selected_location = chosen_location.get()

	if (selected_category == "" or selected_category == "--"):
		top = Toplevel(root)
		top.geometry("350x50")
		top.title("Error")
		Label(top, text= "Please select a category.", font=('Arial, 20')).place(x=175,y=25, anchor = CENTER)
		return

	if (selected_location == "" or selected_category == "--"):
		top = Toplevel(root)
		top.geometry("350x50")
		top.title("Error")
		Label(top, text= "Please select a location.", font=('Arial, 20')).place(x=175,y=25, anchor = CENTER)
		return

	main_page.pack_forget()

	df = cv.requestData(chosen_location.get(), chosen_category.get())
	if chosen_category.get() == "Hotels":
		hotel_frame, hotel_tag = create_hotel_frame()
		pt = Table(hotel_frame, dataframe=df)
	elif chosen_category.get() == "Restaurants":
		restaurant_frame, restaurant_tag = create_restaurant_frame()
		pt = Table(restaurant_frame, dataframe=df)
	elif chosen_category.get() == "Attractions":
		attractions_frame, attractions_tag = create_attractions_frame()
		pt = Table(attractions_frame, dataframe=df)
	
	pt.show()
	last_pt = pt
	if (selected_category == "Hotels"):
		hotel_tag.config(text = "Selected location: " + selected_location)
	elif (selected_category == "Restaurants"):
		restaurant_tag.config(text = "Selected location: " + selected_location)
	elif (selected_category == "Attractions") :
		attractions_tag.config(text = "Selected location: " + selected_location)

root = Tk()
root.title("Dashboard App")
root.geometry("1600x900")
root.resizable(False, False)

bigfont = tkFont.Font(family="Helvetica",size=20)
root.option_add("*TCombobox*Listbox*Font", bigfont)


header = Frame(root, height=150, bg = 'white')
header.pack(side=TOP, fill=BOTH, expand=False)

app_label = Label(header, text='UK City Tourist Spot Data Access Point', width=35, font="Arial, 15", bg="white", fg="black")
app_label.place(x = 200, y = 75, anchor = CENTER)

location_text = Label(header, text='City: ', font='Arial, 15', bg='white')
location_text.place(x = 750, y = 75, anchor = CENTER)

location = StringVar()
chosen_location = ttk.Combobox(header, state = 'readonly', values  = ('--', 'Durham', 'London', 'Manchester'), width = 15, textvariable = location, font = "Arial, 20")
chosen_location.place(x=900, y=75, anchor = CENTER)
chosen_location.set("--")

category_text = Label(header, text='Type of Spot: ', font='Arial, 15', bg='white')
category_text.place(x = 1100, y = 75, anchor = CENTER)

category = StringVar()
chosen_category = ttk.Combobox(header, state = 'readonly', values = ('--', 'Hotels', 'Restaurants', 'Attractions'), width = 15, textvariable = category, font = "Arial, 20")
chosen_category.place(x=1300, y=75, anchor = CENTER)
chosen_category.set("--")

search_button = Button(header, text = 'Search', font = "Arial, 20", command = search)
search_button.place(x=1500, y=75, anchor = CENTER)

main_page = Frame(root, height = 2000, bg = 'lavender')
main_page.pack(side=TOP, fill=BOTH, expand=False)

welcome_text = Label(main_page, text = 'Welcome to our application!', bg = 'lavender', font = "Arial, 30")
welcome_text.place(x = 800, y = 200, anchor = CENTER)

instruction_text = Label(main_page, text = 'Please choose a location and category above.', bg = 'lavender', font = "Arial, 20")
instruction_text.place(x = 800, y = 250, anchor = CENTER)

root.mainloop()

