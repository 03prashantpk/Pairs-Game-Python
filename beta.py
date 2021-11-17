from tkinter import *
import random
from tkinter import messagebox

# Tkinter Defining
root = Tk()
root.title('Pair Game')
root.geometry("500x550")

# Field Events
matches = [1,1,2,2,3,3,4,4,5,5,6,6]

# Randamizer
random.shuffle(matches)

# Defining the Label
my_label = Label(root, text=' ',)
my_label.pack(pady=20)

# Creating Our Buttonm Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Defing Some Variable
count = 0
answer_list = []
answer_dist = {}

# Defing The Function Of the Button
def button_click(b, number):
    global count, answer_list, answer_dist
    
    if b["text"] == ' ' and count < 2:
        b["text"] == matches[number]
        # Add Number to Answer_list
        answer_list.append(number)
        # Button and Number to Answer_Dist
        answer_dist[b] = matches[number]
        # Increment the Counter
        count += 1
        # Just To Check The Function Is Working or not 
        # print(answer_dist)

# Right Or Wrong
if len(answer_list) == 2:
    if matches[answer_list[0]] == matches[answer_list[1]]:
        my_label.config(text="Paired!!")
        for key in answer_dist:
            key["state"] = "disable"
        count = 0
        answer_dist = []
        answer_dist = {}
    else:
        my_label.config(text="DHAA!!!")
        count = 0
        answer_list = []
        # Pop Up Massages 
        messagebox.showinfo("Incorrect!",  "Incorrect")
        
        # Reset The Buttons
        for key in answer_dist:
            key["text"] = " "
            
        answer_dist = {}


# Defning Our Buttons
b0 = Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b0, 0))
b1 = Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b1, 1))
b2 = Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b2, 2))
b3 = Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b3, 3))
b4 = Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b4, 4))
b5 = Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b5, 5))
b6 = Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b6, 6))
b7 = Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b7, 7))
b8 = Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b8, 8))
b9 = Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b9, 9))
b10= Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b10, 10))
b11= Button(my_frame, text=' ', height=5, width=8, command=lambda: button_click(b11, 11))

# Grading Our Buttons
b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

root.mainloop()