from tkinter import *
from tkinter import ttk

def search():
	main_page.pack_forget()
	#display the appropriate frame based on the category
	

root = Tk()
root.title("Dashboard App")
root.geometry("1600x900")
root.resizable(False, False)


header = Frame(root, height=150, bg = 'white')
header.pack(side=TOP, fill=BOTH, expand=False)

label = Label(header, text='App', width=25, font="Arial, 60", bg="white", fg="black")
label.place(x = 200, y = 75, anchor = CENTER)

location_text = Label(header, text='Choose a location: ', font='Arial, 20', bg='white')
location_text.place(x = 650, y = 75, anchor = CENTER)

location = StringVar()
chosen_location = ttk.Combobox(header, width = 15, textvariable = location, font = "Arial, 20")
chosen_location['values'] = ('Durham', 'London', 'Manchester')
chosen_location.place(x=900, y=75, anchor = CENTER)

category_text = Label(header, text='Category: ', font='Arial, 20', bg='white')
category_text.place(x = 1100, y = 75, anchor = CENTER)

category = StringVar()
chosen_category = ttk.Combobox(header, width = 15, textvariable = category, font = "Arial, 20")
chosen_category['values'] = ('Hotels', 'Food', 'Things to do')
chosen_category.place(x=1300, y=75, anchor = CENTER)

search_button = Button(header, text = 'Search', font = "Arial, 20", command = search)
search_button.place(x=1500, y=75, anchor = CENTER)

main_page = Frame(root, height = 2000, bg = 'lavender')
main_page.pack(side=BOTTOM, fill=BOTH, expand=False)

welcome_text = Label(main_page, text = 'Welcome to our application!', bg = 'lavender', font = "Arial, 30")
welcome_text.place(x = 800, y = 200, anchor = CENTER)

instruction_text = Label(main_page, text = 'Please choose a location and category above.', bg = 'lavender', font = "Arial, 20")
instruction_text.place(x = 800, y = 250, anchor = CENTER)



hotel_frame = Frame(root, height = 2000, bg = 'lavender')
hotel_name_label = Label(hotel_frame, text = 'Hotel Name', bg = 'lavender', font = "Arial, 20")
hotel_name_label.place(x = 500, y = 50, anchor=CENTER)
hotel_price_label = Label(hotel_frame, text = 'Price (per night)', bg = 'lavender', font = "Arial, 20")
hotel_price_label.place(x = 1100, y = 50, anchor=CENTER)
#hotel_frame.pack(side=BOTTOM, fill=BOTH, expand=False)

restaurant_frame = Frame(root, height = 2000, bg = 'lavender')
restaurant_name_label = Label(restaurant_frame, text = 'Restaurant Name', bg = 'lavender', font = "Arial, 20")
restaurant_name_label.place(x = 200, y = 50, anchor=CENTER)
restaurant_rating_label = Label(restaurant_frame, text = 'Rating', bg = 'lavender', font = "Arial, 20")
restaurant_rating_label.place(x = 550, y = 50, anchor=CENTER)
restaurant_review_count_label = Label(restaurant_frame, text = 'Number of Reviews', bg = 'lavender', font = "Arial, 20")
restaurant_review_count_label.place(x = 900, y = 50, anchor=CENTER)
restaurant_review_quote_label = Label(restaurant_frame, text = 'Average spending (per person)', bg = 'lavender', font = "Arial, 20")
restaurant_review_quote_label.place(x = 1300, y = 50, anchor=CENTER)
#restaurant_frame.pack(side=BOTTOM, fill=BOTH, expand=False)

attractions_frame = Frame(root, height = 2000, bg = 'lavender')
attractions_name_label = Label(attractions_frame, text = 'Attraction Name', bg = 'lavender', font = "Arial, 20")
attractions_name_label.place(x = 200, y = 50, anchor=CENTER)
attractions_rating_label = Label(attractions_frame, text = 'Rating', bg = 'lavender', font = "Arial, 20")
attractions_rating_label.place(x = 600, y = 50, anchor=CENTER)
attractions_review_count_label = Label(attractions_frame, text = 'Number of Reviews', bg = 'lavender', font = "Arial, 20")
attractions_review_count_label.place(x = 1000, y = 50, anchor=CENTER)
attraction_price_label = Label(attractions_frame, text = 'Admission fee', bg = 'lavender', font = "Arial, 20")
attraction_price_label.place(x = 1400, y = 50, anchor=CENTER)

root.mainloop()