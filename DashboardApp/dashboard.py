from tkinter import *
from tkinter import ttk

def search():
	#display the appropriate frame based on the category
	main.pack_forget()
	hotel_frame.pack(side=BOTTOM, fill=BOTH, expand=False)

root = Tk()
root.title("Dashboard App")
root.geometry("1600x900")
root.resizable(True, True)


header = Frame(root, height=150, bg = 'white')
header.pack(side=TOP, fill=BOTH, expand=False)

main = Frame(root, height = 2000, bg = 'lavender')
main.pack(side=BOTTOM, fill=BOTH, expand=False)

label = Label(header, text='Website', width=25, font="Arial, 60", bg="white", fg="black")
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

hotel_frame = Frame(root, height = 2000, bg = 'lavender')
hotel_name_label = Label(hotel_frame, text = 'Hotel Name', bg = 'lavender', font = "Arial, 20")
hotel_name_label.place(x = 500, y = 50, anchor=CENTER)
hotel_price_label = Label(hotel_frame, text = 'Price (per night)', bg = 'lavender', font = "Arial, 20")
hotel_price_label.place(x = 1100, y = 50, anchor=CENTER)

restaurant_frame = Frame(root, height = 2000, bg = 'lavender')
restaurant_name_label = Label(restaurant_frame, text = 'Restaurant Name')
restaurant_rating_label = Label(restaurant_frame, text = 'Rating')
restaurant_review_count_label = Label(restaurant_frame, text = 'Number of Reviews')
avg_spending_pp_label = Label(restaurant_frame, text = 'Average spending (per person)')
#restaurant_frame.pack(side=BOTTOM, fill=BOTH, expand=False)

attractions_frame = Frame(root, height = 2000, bg = 'lavender')
attractions_name_label = Label(attractions_frame, text = 'Attraction Name')
attractions_rating_label = Label(attractions_frame, text = 'Rating')
attractions_review_count_label = Label(attractions_frame, text = 'Number of Reviews')
attraction_price_label = Label(attractions_frame, text = 'Admission fee')
#attractions_frame.pack(side=BOTTOM, fill=BOTH, expand=False)

root.mainloop()