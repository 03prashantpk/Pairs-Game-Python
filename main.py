#-------------- All imported files and libraries -----------------------------
from tkinter import *
import random
from tkinter import messagebox
import time
# For Audio
import pygame
#For  Menu bar and open files
from tkinter.filedialog import askopenfilename
#For Screenshot
import pyscreenshot
#For Background Image
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter as tk
#to run file directory
import os
#Read content using url
import urllib.request
#open url in brower for feedback
import webbrowser

# ------------------------------ Change Color and Logo here -----------------
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
success_background = "#82e0aa"
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
footer_label = "#f9e79f"
footer_fg = "#000"
footer_label_W = "#f9e79f"
footer_label_f = "#194049"

# record total chance remaining and total matches
chance_file = "assets/chance.txt"

#menu_background color

menu_background = "#41C4C0"

# Font size and Family
menu_font_size = ("Arial 12")

#All popup window color (Menu bar)
pop_window_color_Menu_bar = "#B7C5D5"

# bg color for auto update features
auto_update_popup_bg_color = "#0B1E51"

# ------------------------------ Change Color and Logo Ends here --------------------------------


#------------------------------- initialization and function of - pygame for audio Here ---------------
pygame.mixer.init()

# Change Music track (using menubar)
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
#------------------------------- initialization and function of - pygame ends Here ------------


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

# Read Update text
remote_url  = urllib.request.urlopen('https://notes-k20bn.000webhostapp.com/PairGame/WhatsNew.txt')
WhatsNewInUpdate = remote_url.read()

# Read Version Number
Current_version_no  = urllib.request.urlopen('https://notes-k20bn.000webhostapp.com/PairGame/CurrentVersion.txt')
Current_version_number = Current_version_no.read()

#Version Info File and it use to confirm updates (using count function here...)
remote_url_version_info  = urllib.request.urlopen('https://notes-k20bn.000webhostapp.com/PairGame/versioninfo.txt')
Version_info_remote = remote_url_version_info.read()

# Reading Local files data to match and print it on GUI

# whats New in Update
WhatsNew = open("assets/routes/WhatsNew.txt", "r")
WhatsNew_Message = WhatsNew.readline()

# Pair Game Version v.N.N
CurrentVersionNumber = open("assets/routes/CurrentVersion.txt", "r")
CurrentVersionNumber_V = WhatsNew.readline()

# To match files on every update
version_info_file = open("assets/routes/versioninfo.txt", "r")
Version_info_local = version_info_file.readline()

# print("Local Data",Version_info_local)
# print("Remote data ",Version_info_remote)

# Fatching online and offline data length to prompt update features.
Version_info_remote_len = len(Version_info_remote)
CurrentVersionNumber_Len = len(Version_info_local)

print("Local Data:",CurrentVersionNumber_Len)
print("Remote data: ",Version_info_remote_len)


# print(count_remote_version,count_local_version)
# print(version_info)
# print(Version_info_tester)

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
    wall_now= "assets/images/bg8.png"
    tile_background = "#5499c7"
    tile_foreground = "#F0F6FB"

    def opening():
        pygame.mixer.music.load("assets/music/titanic_bgm.mp3")
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

# Background image setup
window_background = PhotoImage(file=wall_now)
l = Label(window , image= window_background)
l.place(x = 0 , y = 20 , relwidth = 1 , relheight = 1)

# Screenshot and save screenshot function starts here -------------------------------------------
def screen_shot():
    image = pyscreenshot.grab()
    image.save("assets/screenshots/Pair_Game.png")

def open_ss():
    image = pyscreenshot.grab()
    image.save("assets/screenshots/Pair_Game.png")
    image.show()
# Screenshot and save screenshot function Ends here ---------------------------------------------

#app Version
def app_version():
    window4 = Tk()
    window4.title('App Version')
    window4.geometry("500x300")
    window4.config(background=pop_window_color_Menu_bar)
    window4.iconbitmap(logo)

    def viewAppversion():
            button = Button(window4, text='Close', width="55", height="28", command=Close_about,background=footer_label,foreground=footer_fg)
            button.pack(pady=80, padx=190)
        
    # Update Window Header Text
    appversion_info_win = Label(window4,text="Game Version",font= ('Times New Roman' , 20 , 'bold'),background=pop_window_color_Menu_bar, foreground="#242424")
    appversion_info_win.pack(pady=10)

    #Update Window What's New In update text
    version_info_text_win = Label(window4,background=pop_window_color_Menu_bar,text=Current_version_number, justify= 'center', font=(10))
    version_info_text_win.pack(pady=10,padx=20)

    def Close_about():
        window4.destroy()

    #fatching Download Button
    viewAppversion()
    window.mainloop()

#app Update Message (Not in use anymore)
def app_Update():
    messagebox.showinfo("App Update", "You are currently up to date.\n Please Run update.bat to update in future.")

#App developer and Project info
def App_developer():
    window5 = Tk()
    window5.geometry("500x300")
    window5.title('Our Other Projects')
    window5.config(background=pop_window_color_Menu_bar)
    window5.iconbitmap(logo)

    def viewAppversion():
            button = Button(window5, text='Close', width="55", height="28", command=Close_about,background=footer_label,foreground=footer_fg)
            button.pack(pady=50, padx=190)
        
    # Update Window Header Text
    appversion_info_win = Label(window5,text="App Developers",font= ('Times New Roman' , 20 , 'bold'),background=pop_window_color_Menu_bar, foreground="#242424")
    appversion_info_win.pack(pady=10)

    #Update Window What's New In update text
    version_info_text_win = Label(window5,background=pop_window_color_Menu_bar,text="This is a project work. Given by University\nInstructor Name: Sir. Moin Hasan\n\n More Information will be updated soon", justify= 'left',font=('Times New Roman' , 12 , ))
    version_info_text_win.pack(pady=10,padx=20)

    def Close_about():
        window5.destroy()

    #fatching Download Button
    viewAppversion()
    
    window.mainloop()

#Project info  
def Project():
    window5 = Tk()
    window5.geometry("500x300")
    window5.title('Our Other Projects')
    window5.config(background=pop_window_color_Menu_bar)
    window5.iconbitmap(logo)

    def viewAppversion():
            button = Button(window5, text='Close', width="55", height="28", command=Close_about,background=footer_label,foreground=footer_fg)
            button.pack(pady=50, padx=190)
        
    # Update Window Header Text
    appversion_info_win = Label(window5,text="More Projects",font= ('Times New Roman' , 20 , 'bold'),background=pop_window_color_Menu_bar, foreground="#242424")
    appversion_info_win.pack(pady=10)

    #Update Window What's New In update text
    version_info_text_win = Label(window5,background=pop_window_color_Menu_bar,text="Our Other App\n 1. Multi Image Downloader - Using Python \n 2. Pair Game - Python \n 3. Music App - Python", justify= 'left',font=('Times New Roman' , 13 , ))
    version_info_text_win.pack(pady=10,padx=20)

    def Close_about():
        window5.destroy()

    #fatching Download Button
    viewAppversion()
    
    window.mainloop()

#Contact Details
def contact():
    window5 = Tk()
    window5.iconbitmap(logo)
    window5.geometry("500x300")
    window5.title('Contact Info')
    window5.config(background=pop_window_color_Menu_bar)
    

    def viewAppversion():
            button = Button(window5, text='Close', width="55", height="28", command=Close_about,background=footer_label,foreground=footer_fg)
            button.pack(pady=60, padx=190)
        
    # Update Window Header Text
    appversion_info_win = Label(window5,text="Reach Us At",font= ('Times New Roman' , 20 , 'bold'),background=pop_window_color_Menu_bar, foreground="#242424")
    appversion_info_win.pack(pady=10)

    #Update Window What's New In update text
    version_info_text_win = Label(window5,background=pop_window_color_Menu_bar,text="Our (Team) Contact information are:\nEmail: admin@flevar.in\nPhone: 961209XXXX", justify= 'left' ,font=('Times New Roman' , 13 , ))
    version_info_text_win.pack(pady=10,padx=20)

    def Close_about():
        window5.destroy()

    #fatching Download Button
    viewAppversion()
    
    window.mainloop()

#about us
def about():
    window3 = Tk()
    window3.title('About')
    window3.iconbitmap(logo)
    window3.geometry("500x300")
    window3.config(background=pop_window_color_Menu_bar)
    

    def fatch_download_button():
            button = Button(window3, text='Close', width="55", height="28", command=Close_about,background=footer_label,foreground=footer_fg)
            button.pack(pady=55, padx=190)
        
    # Update Window Header Text
    about_title_win = Label(window3,text="About",font= ('Times New Roman' , 20 , 'bold'),background=pop_window_color_Menu_bar, foreground="#242424")
    about_title_win.pack(pady=10)

    #Update Window What's New In update text
    features = Label(window3,background=pop_window_color_Menu_bar,text="Pair Game. \nDeveloped for Childern above 3+ years. \nCan help to improve memory power. \n \nIt has exciting background music to keep children engaged.", justify= 'left')
    features.pack(pady=10,padx=20)

    def Close_about():
        window3.destroy()

    #fatching Download Button
    fatch_download_button()
    
    window.mainloop()

#function on clicking update buttons
#app Update Message
def Want_to_update():
    window2 = Tk()
    window2.iconbitmap(logo)
    window2.geometry("500x300")
    window2.title('Update Window')
    window2.config(background=pop_window_color_Menu_bar)

    def fatch_download_button():
            button = Button(window2, text='Download Update', width="55", height="28", command=app_Update_now,background=footer_label,foreground=footer_fg)
            button.pack(pady=30, padx=150)

    def fatch_no_update_button():
            button = Button(window2, text='Cose', width="55", height="28", command=Close_btn,background=footer_label,foreground=footer_fg)
            button.pack(pady=30, padx=190)
    
    if Version_info_remote_len != CurrentVersionNumber_Len:
        header_message = "Update Available"
        
    else:
        header_message = "You're Update to date"
        
    # Update Window Header Text
    update_available = Label(window2,text=header_message,font= ('Times New Roman' , 20 , 'bold'),background=pop_window_color_Menu_bar, foreground="#242424")
    update_available.pack(pady=10)

    #Update Window What's New In update text
    features = Label(window2,background=pop_window_color_Menu_bar,text=WhatsNewInUpdate, justify= 'left', font=('Times New Roman', 11,))
    features.pack(pady=9,padx=20)

    def app_Update_now():
        messagebox.showinfo("Update Now", "Your Game Will Restart")
        time.sleep(1)
        os.startfile("C:\Games\Download_update.bat")
        window.destroy()
        window2.destroy()
    
    def Close_btn():
        window2.destroy()

    #fatching Download Button
    if Version_info_remote_len != CurrentVersionNumber_Len:
        fatch_download_button()
    else:
        fatch_no_update_button()
    
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
help_.add_command(label ='About', command = about,font=menu_font_size,background=menu_background)

#Help Version Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_ , background=menu_background)
# help_.add_command(label ='Check Update', command =lambda: app_Update(),font=menu_font_size, background=menu_background)
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
player_name = Label(window, text="Enter Your Name" ,font=('Arial Rounded MT Bold', 14,), width = 23 ,background=bg , foreground=fg2)
player_name.pack(pady=10)

#Player Name input area
inputtxt = tk.Text(window,bd=3, height = 1, font=('Arial Rounded MT Bold', 14,), width = 25, background=text_area,)
inputtxt.pack(pady=2)

#Player Name input submit button
printButton = Button(window,text= "Submit", font=('Arial Rounded MT Bold', 14,), background=button_bg, width=12, command = print_player_name)
printButton.pack(pady=4)

#Player name assigning
playing = tk.Label(window, text = "", width=0, height=0, background=default_text_bg)
playing.pack(pady=20)

# ---------------------------------- windows Icons and buttons functions assigned Ends here -----------


#---------------------------------  Main logic Starts here   -----------------------------------------

#Create Matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6]

#Shuffle Matches
random.shuffle(matches)
print("Pair List\n",matches)

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

        print("Echo click tile:",answer_list)
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

# Creating Buttons with var (bn)
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

# Grid buttons
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


# if count_remote_version != count_local_version:
#     print("Not Updated")
# else:
#     print("Updated")

def Play_again_fn():
    os.startfile("C:\Games\Pairs-Game-Python\StartGame.bat")
    window.destroy()

def feed_back():
    #open feedback url.
    url = "http:/enally.in/contact.php"
    webbrowser.open_new(url)


def auto_update_pop_with_y_n():
    window_auto_up = Tk()
    window_auto_up.iconbitmap(logo)
    window_auto_up.geometry("570x70")
    window_auto_up.title('New Update Abailable')
    window_auto_up.config(background=auto_update_popup_bg_color)
    

    def viewAppversion():

            #printing on the right side
            button = Button(window_auto_up, text='Update Now', width=10,  command=download_the_update_now,background=footer_label,foreground=footer_fg)
            button.place(x=480,y=20)

            # printing on the left side of the update button
            button = Button(window_auto_up, text='Later', width=8,  command=Close_about,background=footer_label,foreground=footer_fg)
            button.place(x=405,y=20)
        
    '''
    This function only appears if the user has not updated the game.
    Improvement can be done that... it should not prompt on every time launching the game.
    Instead add a function the it should only appear few times (not again and again) on launching the game.

    **Note: Make sure that you do not change or update ('A newer version of Pairs Game is available.') this text
    written somewhere below as text='' otherwise it may break the code and the whole layout of the window
    will destroy.
    
    '''

    #Update Window What's New In update text (do not Update the text=" " message)
    version_info_text_win = Label(window_auto_up,background=auto_update_popup_bg_color,text="A newer version of Pairs Game is available.", foreground=fg, justify= 'left', font=('American Typewriter', 12, 'bold'))
    version_info_text_win.place(x=20,y=20)

    #funtion on cliking Update now placed on same code (function above) block above
    def download_the_update_now():
        messagebox.showinfo("Update Now", "Your Game Will Restart")
        time.sleep(1)
        os.startfile("C:\Games\Download_update.bat")
        window.destroy()
        window2.destroy()
    
    # close the update window
    def Close_about():
        window_auto_up.destroy()

    #fatching Download Button
    viewAppversion()
    window.mainloop()

# Version_info_remote_len = len(Version_info_remote)
# CurrentVersionNumber_Len = len(Version_info_local)

if Version_info_remote_len != CurrentVersionNumber_Len:
    #Update Available
    Update_available  = Button(window , text= 'Update Available' , width=20, height=1, font="2", command= Want_to_update,background=footer_label,foreground=footer_fg)
    Update_available.place(x= 960 , y= 720)
    auto_update_pop_with_y_n()

else:
    #If Update not available
    Update_available  = Button(window , text= Current_version_number , width=20, height=1, font="2",background=footer_label,foreground=footer_fg)
    Update_available.place(x= 960 , y= 720)

# Footer Buttons Codes Starts here....

#Exit Button
exit_the_game  = Button(window , text= "Exit", width=8, height=1, command=window.destroy, font="2",background=footer_label,foreground=footer_fg)
exit_the_game.place(x= 25 , y= 720)

#Play Again
Play_again  = Button(window , text= " Play Again ", width=8, height=1, command=Play_again_fn, font="2",background=footer_label,foreground=footer_fg)
Play_again.place(x= 1240 , y= 660)

#Developer website link
Developer_credit = Label(window, font=('Times New Roman' , 10 , 'bold'), text="https://enally.in", background=None,foreground=footer_fg ,width='18')
Developer_credit.place(x=144,y=735)

feedback  = Button(window , text= 'Feedback'  , width=10, height=1, font="2", command= feed_back,background=footer_label,foreground=footer_fg)
feedback.place(x= 1220 , y= 720)

if wallpaper_no == 0:
    current_themes = Label(window, text="Current Theme: Titanic",font= ('Times New Roman' , 10 , 'bold'))
    current_themes.place(x=144,y=710)

elif wallpaper_no == 1:
    current_themes = Label(window, text="Current Theme: Mr.Bean",font= ('Times New Roman' , 10 , 'bold'))
    current_themes.place(x=144,y=710)

elif wallpaper_no == 2:
    current_themes = Label(window, text="Current Theme: Jungle Book",font= ('Times New Roman' , 10 , 'bold'))
    current_themes.place(x=144,y=710)

elif wallpaper_no == 3:
    current_themes = Label(window, text="Current Theme: Hattori",font= ('Times New Roman' , 10 , 'bold'))
    current_themes.place(x=144,y=710)

# Footer Buttons Codes Starts here....

#---------------------------------  Main logic Ends here   ---------------------------------------------
#menu bar config
window.config(menu = menubar)
#loop Windows
window.mainloop()