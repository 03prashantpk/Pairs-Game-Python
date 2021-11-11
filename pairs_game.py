from tkinter import *
import random
from tkinter import messagebox

window = Tk()
window.title("Pairs Game - Prashant Kumar")
window.iconbitmap("assets/images/enally.ico")
window.geometry("800x700")
window.configure(bg="light green")

#Create Matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6]

#Shuffle Matches
random.shuffle(matches)
print(matches)

# Creating Button Frame
bcontainer = Frame(window)
bcontainer.config(width=200, height=200,background="grey")
bcontainer.config(bd=1)
bcontainer.pack(pady=100,padx=0)


# Few Variables
count = 0
answer_list = []
answer_dict = {}

#function for button_click
def button_click(b, number):
    global count, answer_list, answer_dict

    if b['text'] == " " and count <2:
        b['text'] = matches[number]

        # Add selected number to answer list (tells us address)
        answer_list.append(number)
        
        # Add button number and name in dict
        answer_dict[b] = matches[number]

        #INCREMENT counter
        count +=1

        print(answer_list)
        #print(answer_dict)
    
    # Correct or not?
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            new_label.config(text="Its A Match!", bg="green" ,font=("Arial 18"))

            for key in answer_dict:
                key["state"] = "disabled"

            count = 0
            answer_list = []
            answer_dict = {}
        else:
            new_label.config(text="No Match! Try Again",bg="red",font=("Arial 18"))
            count = 0
            answer_list = []

            #Pop Message
            messagebox.showinfo("Incorrect!", "Incorrect")

            for key in answer_dict:
                key["text"] = " "
            
            answer_dict = {}
        



#Creating Buttons
b0 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b0, 0))
b1 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b1, 1))
b2 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b2, 2))
b3 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b3, 3))

b4 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b4, 4))
b5 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b5, 5))
b6 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b6, 6))
b7 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b7, 7))

b8 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b8, 8))
b9 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b9, 9))
b10 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b10, 10))
b11 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b11, 11))

#grid buttons
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

new_label = Label(window, text="Game Status: ")
new_label.pack(pady=20)

hint_text = (answer_list)

# Define hint button and function
def hint():
    hint_label = Label(window, text="Hint")
    hint_label.pack(pady=1)
    hint_label.config(text=hint_text)

#reset = Button(bg="red", text="hint", font=("Helvetica",14), command = hint)
#reset.pack(pady=2)

credit_label = Label(window, text="Simple Pairs Game")
credit_label.pack(pady=6,padx=0)

window.mainloop()