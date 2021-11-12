#-------------- All imported files and libraries -----------------------------
from tkinter import *
import random
from tkinter import messagebox
import tkinter as tk
import time
# For Audio
import pygame
#For  Menu bar
from tkinter.filedialog import askopenfilename
#For Screenshot
import pyscreenshot
#For Background Image
from tkinter import ttk
from PIL import Image,ImageTk

#to run file directory
import os

#Read content using url
import urllib.request

# ------------------------------ Change Color and Logo here ---------------
#Window Icon or logo
logo = "assets/images/enally.ico"

#main background
bg = '#DBE9F7'
fg = '#fff'
fg2 = "#000"

#tiles colors
tile_background = "#4530A2"
tile_foreground = "#F0F6FB"

#Matched
success_background = "#B8EB4E"
success_foreground = "yellow"

#matched_mesage
message_background = "#513EC0"
message_foreground = "#fff"

#Not_Matched
failed_background = "light red"
failed_foreground = "yellow"

#Not_matched
No_match_message_background = "#F79553"
No_match_message_foreground = "#242424"

# Defoult font background
default_text_bg = bg

#input_textarea
text_area = "#B7C5D5"

#heading color
heading = "#0B1E51"

#player name colors
player_name_background = "#FAEBD7"
player_name_foreground = "#000000"

#name Submit button
button_bg = "#F5DEB3"

#footer lable win and Alert color
footer_label = "#FFD800"
footer_fg = "#000"
footer_label_W = "#FFD700"
footer_label_f = "#194049"

# record total chance remaining and total matches
chance_file = "assets/chance.txt"

#menu_background color

menu_background = "#41C4C0"

# Font size and Family
menu_font_size = ("Arial 12")


#ScreenShot dimension

# ------------------------------ Change Color and Logo Ends here ---------------


#------------------------------- initialization and function of - pygame for audio Here ---------------
pygame.mixer.init()

# Music track
def change_music(music_next):
    if music_next == 1:
        def opening():
            pygame.mixer.music.load("assets/music/MrBean_piano.mp3")
            pygame.mixer.music.play(loops=3)
        opening()
    
    elif music_next == 2:
        def opening():
            pygame.mixer.music.load("assets/music/noddymusci.mp3")
            pygame.mixer.music.play(loops=3)
        opening()

    elif music_next == 3:
        def opening():
            pygame.mixer.music.load("assets/music/soha.mp3")
            pygame.mixer.music.play(loops=3)
        opening()

def fail():
    pygame.mixer.music.load("assets/music/Fail.mp3")
    pygame.mixer.music.play(loops=0)
    messagebox.showinfo("Incorrect!", "Oh! No missed try again")
#fail()

def win():
    pygame.mixer.music.load("assets/music/win.mp3")
    pygame.mixer.music.play(loops=0)
    status_label.config(text=" Its A Match! ", bg=message_background, fg=message_foreground ,font=("Arial 18"))
#win()

def cheers():
    pygame.mixer.music.load("assets/music/Cheers.mp3")
    pygame.mixer.music.play(loops=0)
#cheers()

def clicked_pop():
    pygame.mixer.music.load("assets/music/pop.mp3")
    pygame.mixer.music.play(loops=0)
#clicked_pop()
#------------------------------- initialization and function of - pygame ends Here ---------------


#---------------------------------------- File Handling -------------------------------------
# total number of chance assigned through list (In Pair)
total_chance = ['1','2','3','4','5','6']

# Opening file with create and write mode
with open("assets/routes/chance.xml", 'w+') as f:

    # write elements of list
    for items in total_chance:
        f.write('%s\n' %items)
    print("Game Started Successfully")
  
# close the file
f.close()


# Counting Total Match and Total Chance
def remaining_chances():
    with open(r"assets/routes/chance.xml", 'r') as fp:
        for count, line in enumerate(fp):
            pass
    
    # Count value will be used for remaining chance
    total_chance_remaining = count

    # total chances - remaining values are total matches
    total_match = (6 - total_chance_remaining)

    #printing on console and POP up
    print(total_chance_remaining)
    if total_chance_remaining == 0:
        print("Game Over")
        messagebox.showinfo("Game Over!", "Hurrey! You won")
    remaining_chance_label.config(text=total_match, bg=message_background, fg=message_foreground ,font=("Arial 22"))


# Deleting total chance list one by one on each pair of matches
def dec_chance():

    # Storing file in a list
    lines = []

    # File Read mode
    with open(r"assets/routes/chance.xml", 'r') as fp:
        # read an store all lines into list
        lines = fp.readlines()

    # Writing changes by deleting list item
    with open(r"assets/routes/chance.xml", 'w') as fp:

        # iterate each line
        for number, line in enumerate(lines):
            # delete line 0
            if number not in [0]:
                fp.write(line)



#To access and read txt file from url
remote_url  = urllib.request.urlopen('https://www.enally.in/author.txt')
update_checker_text = remote_url.read()
#print(update_checker_text)

remote_url_version_info  = urllib.request.urlopen('https://www.enally.in/author.txt')
Version_info_tester = remote_url_version_info.read()

version_info_file = open("assets/routes/versioninfo.xml", "r")
version_info = version_info_file.readline()

count_remote_version = len(Version_info_tester)
count_local_version = len(version_info)
# print(count_remote_version,count_local_version)

# print(version_info)
# print(Version_info_tester)


# # Decrease 1 line from update_cheker.xml
# def update_update_cheker():
    
#     # Storing file in a list
#     lines = []

#     # File Read mode
#     with open(r"assets/routes/versioninfo.xml", 'r') as fp:
#         # read an store all lines into list
#         lines = fp.readlines()

#     # Writing changes by deleting list item
#     with open(r"assets/routes/versioninfo.xml", 'w') as fp:

#         # iterate each line
#         for number, line in enumerate(lines):
#             # delete line 0
#             if number not in [0]:
#                 fp.write(line)

#---------------------------------------- File Handling Ends Here-------------------------------------


# ---------------------------------- windows Icons and buttons functions assigned here --------------
#Main window, Icons and title variables 
window = Tk()
window.title("Pairs Game - Prashant Kumar")
window.iconbitmap(logo)
window.geometry("1350x800")
#window['background'] = bg 

#random wallpaper Choice
wallpaper_no = random.randint(0, 3)

#--- Choice 1
if wallpaper_no == 0:
    wall_now= "assets/images/bg4.png"
    tile_background = "#FFB6C1"
    tile_foreground = "#F0F6FB"
    def opening():
        pygame.mixer.music.load("assets/music/Mrbean_bg1.mp3")
        pygame.mixer.music.play(loops=3)
    opening()

#--- Choice 2
elif wallpaper_no == 1:
    wall_now= "assets/images/bg1.png"
    tile_background = "#89CEEF"
    tile_foreground = "#F0F6FB"
    def opening():
        pygame.mixer.music.load("assets/music/Mrbean_bg1.mp3")
        pygame.mixer.music.play(loops=3)
    opening()

#--- Choice 3
elif wallpaper_no == 2:
    wall_now= "assets/images/bg2.png"
    tile_background = "#00693E"
    tile_foreground = "#F0F6FB"
    def opening():
        pygame.mixer.music.load("assets/music/jungle.mp3")
        pygame.mixer.music.play(loops=3)
    opening()

#--- Choice 4
elif wallpaper_no == 3:
    wall_now= "assets/images/bg5.png"
    tile_background = "#00693E"
    tile_foreground = "#F0F6FB"
    def opening():
        pygame.mixer.music.load("assets/music/Ninjabg2.mp3")
        pygame.mixer.music.play(loops=3)
    opening()

window_background = PhotoImage(file=wall_now)
l = Label(window , image= window_background)
l.place(x = 0 , y = 20 , relwidth = 1 , relheight = 1)

#screenshot
def screen_shot():
    image = pyscreenshot.grab()
    image.save("assets/screenshots/Pair_Game.png")

def open_ss():
    image = pyscreenshot.grab()
    image.save("assets/screenshots/Pair_Game.png")
    image.show()

#app Version
def app_version():
    messagebox.showinfo("App Version", "Pair Game v.2.1")

#app Update Message
def app_Update():
    messagebox.showinfo("App Update", "You are currently up to date.\n Please Run update.bat to update in future.")

#App developer and Project info
def App_developer():
    messagebox.showinfo("App Developer", "This App is developed for Project.\n Work Given by - Moin Hasan\n Please Run update.bat to update in future.")

#Project info  
def Project():
    messagebox.showinfo("Other Projects", "Our Other App\n 1. Multi Image Downloader - Using Python \n 2. Pair Game - Python \n 3. Music App - Python")

#Contact Details
def contact():
    messagebox.showinfo("Contact", "You can contact us at.\n Email: admin@enally.in \n Phone: 96120xxxxx.")

#about us
def about():
    messagebox.showinfo("About Game", "Pair Game\n This a a pair game where you have to select and match 2 tiles to win the game.\n It also has some music track and sound effects to make it more fun.")


#function on clicking update buttons

#app Update Message
def Want_to_update():
    window2 = Tk()
    window2.title('Update Available')
    window2.geometry("500x300")
    window2.config(background="#B7C5D5")
    window2.iconbitmap(logo)

    update_available = Label(window2,text="Update Available",font= ('Times New Roman' , 20 , 'bold'),background="#B7C5D5", foreground="#242424")
    update_available.pack(pady=10)

    features = Label(window2,background="#B7C5D5",text=update_checker_text, justify= 'left')
    features.pack(pady=10,padx=20)
    def app_Update_now():
        messagebox.showinfo("Update Now", "You need to close the Game to Start Update.\n Press Yes to Continue\nPress No to Leave")
        os.startfile("C:\Games\Download_update.bat")
        time.sleep(1)
        window.destroy()
        window2.destroy()

    button = Button(window2, text='Download Update', width="55", height="28", command=app_Update_now)
    button.pack(pady=70, padx=150)
    window.mainloop()



# Menu_bar Extension
menubar = Menu(window)

# Adding File Menu save and more
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file,font=menu_font_size)
file.add_command(label ='Open...', command = lambda: open_ss(),font=menu_font_size , background=menu_background)
file.add_command(label ='Save', command = lambda: screen_shot(), font=menu_font_size, background=menu_background)
file.add_separator(background=menu_background)
file.add_command(label ='Exit', command = window.destroy, font=menu_font_size, background=menu_background)

#Adding Music
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Music', menu = edit,font=menu_font_size)
edit.add_command(label ='Mr. Bean Pino Music', command = lambda: change_music(1),font=menu_font_size, background=menu_background)
edit.add_command(label ='Noddy Music', command = lambda: change_music(2),font=menu_font_size, background=menu_background)
edit.add_command(label ='SOUHILA - Trap Oriental Beat x Balkan Oriental', command = lambda: change_music(3),font=menu_font_size, background=menu_background)

#More Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='More', menu = help_ , background=menu_background)
help_.add_command(label ='Project', command = lambda: Project(),font=menu_font_size, background=menu_background)
help_.add_command(label ='Contact', command = lambda: contact(),font=menu_font_size,background=menu_background)
help_.add_separator(background=menu_background)
help_.add_command(label ='About', command = lambda: about(),font=menu_font_size,background=menu_background)

#Help Version Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_ , background=menu_background)
help_.add_command(label ='Check Update', command =lambda: app_Update(),font=menu_font_size, background=menu_background)
help_.add_command(label ='App Version', command =lambda: app_version(),font=menu_font_size,background=menu_background)
help_.add_command(label ='Update Now', command = Want_to_update,font=menu_font_size,background=menu_background)
help_.add_separator(background=menu_background)
help_.add_command(label ='Developer', command = lambda: App_developer(),font=menu_font_size,background=menu_background)

#Heading (Game Name)
credit_label = Label(window, width=100, text="Pairs Game - K20BN (G2)" ,font=("'Helvetica 28") ,background=heading , foreground=fg)
credit_label.pack(pady=0)


#Players function and Variables
#Printing Player Name
def print_player_name():
    global print_player_name
    print_player_name = inputtxt.get(1.0, "end-1c")
    playing.config( bg=player_name_background, width=28, fg=player_name_foreground,font=('Times New Roman',22),text = "Player - "+ print_player_name)

    #Hiding widgets using pack_forget()
    player_name.pack_forget()
    inputtxt.pack_forget()
    printButton.pack_forget()

    cheers()
    time.sleep(2)
    opening()


#Player Name input
player_name = Label(window, text="Enter Your Name" ,font=("'Helvetica 11") ,background=bg , foreground=fg2)
player_name.pack(pady=10)

#Player Name input area
inputtxt = tk.Text(window,bd=3, height = 1, width = 28, background=text_area,)
inputtxt.pack(pady=2)

#Player Name input submit button
printButton = Button(window,text= "Submit", background=button_bg, width=12, command = print_player_name)
printButton.pack(pady=4)

#Player name assigning
playing = tk.Label(window, text = "", width=0, height=0, background=default_text_bg)
playing.pack(pady=20)

# ---------------------------------- windows Icons and buttons functions assigned Ends here --------


#---------------------------------  Main logic Starts here   -----------------------------------------

#Create Matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6]

#Shuffle Matches
random.shuffle(matches)
print(matches)

#Creating Button Frame
bcontainer = Frame(window)
bcontainer.config(width=200, height=200)
bcontainer.config(bd=3)
bcontainer.pack(pady=20,padx=0)


# Few Variables
count = 0
answer_list = []
answer_dict = {}

#function for button_click
def button_click(b, number):
    global count, answer_list, answer_dict,chance
    
    if b['text'] == " " and count <2:
        b['text'] = matches[number]
        clicked_pop()

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
            
            win()
            remaining_chances()
            time.sleep(2)
            opening()

            for key in answer_dict:
                key["state"] = "disabled"
                key["background"] = success_background
                key["foreground"] = success_foreground
                key["bd"] = "-8"

            count = 0
            answer_list = []
            answer_dict = {}
            dec_chance()
        

        else:
            status_label.config(text=" No Match! Try Again " ,fg=No_match_message_foreground,bg=No_match_message_background,font=("Arial 22"))
            count = 0
            answer_list = []

            #Pop Message
            fail()
            time.sleep(2)
            opening()


            for key in answer_dict:
                key["text"] = " "
            answer_dict = {}

#Creating Buttons
b0 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b0, 0) , state = "normal", background =tile_background , foreground=tile_foreground)
b1 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b1, 1) , state = "normal", background =tile_background , foreground=tile_foreground)
b2 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b2, 2) , state = "normal", background =tile_background , foreground=tile_foreground)
b3 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b3, 3) , state = "normal", background =tile_background , foreground=tile_foreground)

b4 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b4, 4) , state = "normal", background =tile_background , foreground=tile_foreground)
b5 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b5, 5) , state = "normal", background =tile_background , foreground=tile_foreground)
b6 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b6, 6) , state = "normal", background =tile_background , foreground=tile_foreground)
b7 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b7, 7) , state = "normal", background =tile_background , foreground=tile_foreground)

b8 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b8, 8) , state = "normal", background =tile_background , foreground=tile_foreground)
b9 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b9, 9) , state = "normal", background =tile_background , foreground=tile_foreground)
b10 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b10, 10) , state = "normal", background =tile_background , foreground=tile_foreground)
b11 = Button(bcontainer, text=" ",font=("Helvetica",20), height=3, width=6, command=lambda: button_click(b11, 11) , state = "normal", background =tile_background , foreground=tile_foreground)

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

remaining_chance_label = Label(window,font="18", text="Hey, You Can win this", background=footer_label_W,foreground=footer_label_f ,width='24')
remaining_chance_label.pack(pady=2)

status_label = Label(window, font="18", text="Game Status: Not Started Yet", background=footer_label,foreground=footer_fg ,width='24')
status_label.pack(pady=20)
def distroy():
    window.destroy()
    window2.destroy()

feedback  = Button(window , text= 'Feedback' , bg = "silver" , width=10, height=1, font="2", command= None,background=footer_label,foreground=footer_fg)
feedback.place(x= 1220 , y= 720)


# if count_remote_version != count_local_version:
#     print("Not Updated")
# else:
#     print("Updated")

if count_remote_version != count_local_version:
    Update_available  = Button(window , text= 'Update Available' , bg = "silver" , width=20, height=1, font="2", command= Want_to_update,background=footer_label,foreground=footer_fg)
    Update_available.place(x= 960 , y= 720)
else:
    Update_available  = Button(window , text= "Version: 2.1", bg = "silver" , width=20, height=1, font="2",background=footer_label,foreground=footer_fg)
    Update_available.place(x= 960 , y= 720)

#---------------------------------  Main logic Starts here   -----------------------------------------

#menu bar config
window.config(menu = menubar)
#loop Windows
window.mainloop()