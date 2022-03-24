import tkinter.ttk
from tkinter import *
import threading
import ctypes
import time, random, sys, ast
from PIL import ImageTk, Image

# Get Screen Size and store it
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
screen_x, screen_y = screensize

# Get Functions Such As Encoding

def encode(raw):
    lA = random.choice(["a","b","c","d","e","f","g","h","i","j","k"])
    lB = random.choice(["a","b","c","d","e","f","g","h","i","j","k"])
    code = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_"]
    raw_redo = raw
    t = code.index(lA) + code.index(lB)
    data = raw
    for i in range(t):
        c = ''
        for i in data:
            if (i == ' '):
                c += ' '
            else:
                c += (chr(ord(i) + 3))
        data = c
    try:
        if random.randint(0,2) == 1:
            return lA.upper() + lB.upper() + c
        elif random.randint(0,2 == 1):
            return lA + lB.upper() + c
        else:
            return lA + lB + c
    except UnboundLocalError:
        return "None"


def decode(enc):
    code = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_"]
    no1 = enc[:1]
    no2 = enc[1:2]
    data = enc[2:]
    iterations = code.index(no1.lower()) + code.index(no2.lower())
    message = data
    for i in range(iterations):
        c = ''
        for i in message:
            if (i == ' '):
                c += ' '
            else:
                c += (chr(ord(i) - 3))
        message = c
    return c

def collide(click, rect):
    try:
        rx, ry, rw, rh = rect
        cx, cy = click
        Output = False
        for x in range(rx, rx + rw):
            if x == cx:
                for y in range(ry, ry + rh):
                    if y == cy:
                        Output = True

    except Exception as e:
        Output = e
        print("ERROR IS: ", rect)

    return Output



class Autos():
    def __init__(self, datalist):
        global ALLAUTOS
        total,  autos_all, name = datalist
        self.total_autos = int(total)
        self.tautos = 0
        self.autos = autos_all
        ALLAUTOS = self.autos
        self.autos_xy = []
        self.auto_data = []

        global AUTODATA
        AUTODATA = self.autos_xy

        # Set all upgrades to 1
        self.up_spoon_tree = 1
        self.up_spoon_draw = 1
        self.up_spoon_cave = 1
        self.up_spoon_church = 1



        self.auto_rects = []
        self.username = name

        print("Auto Class Made")

    def New_Auto(self, Name, Cost, NSPps): # image files must be 50 x 50 pixels and JUST say the image name aka Clicker.png
        global screen_x
        y_coord = self.tautos * 50
        x_coord = screen_x - 250
        self.autos_xy.append((Name, Cost, x_coord, y_coord))
        self.auto_data.append((Name, NSPps, Cost))
        self.tautos += 1
        x_pos = x_coord
        y_pos = y_coord
        width = 250
        height = 50

        # make the rectangle variable
        rectangle = (x_pos, y_pos, width, height)
        self.auto_rects.append(rectangle)
        print("Generated New Auto Named '" + Name + "', Costing: " + str(Cost) + " Silver Spoons")




    def check_click(self):
        global clicked_Check
        global CLICK
        global nana_bek_rect
        global balance

        max_x, max_y = screensize
        if clicked_Check == True:
            clicked_Check = False
            x, y = CLICK

            if collide((x,y), nana_bek_rect): #nana_bek_rect.collidepoint(x, y): # quickly check they are not just clicking for spoons to save some time.
                balance += 1

            elif collide((x,y), nana_bek_rect) == False:
                i = 0
                for button in self.auto_rects:
                    if collide((x, y), button):
                        Clicked = i

                    i += 1
                try:
                    i += Clicked # Test if Anything Is clicked
                    name, NSSps, Cost = self.auto_data[Clicked]
                    if name == "spoon_draw":
                        if balance >= Cost:
                            balance -= Cost
                            self.autos.append("spoon_draw")
                            self.total_autos += 1
                    if name == "spoon_tree":
                        if balance >= Cost:
                            balance -= Cost
                            self.autos.append("spoon_tree")
                            self.total_autos += 1
                    if name == "spoon_cave":
                        if balance >= Cost:
                            balance -= Cost
                            self.autos.append("spoon_cave")
                            self.total_autos += 1
                    if name == "spoon_church":
                        if balance >= Cost:
                            balance -= Cost
                            self.autos.append("spoon_church")
                            self.total_autos += 1




                except Exception as e:
                    #print(e)
                    pass
            else:
                print(collide((x,y), nana_bek_rect))

    def Get_autos(self):
        return self.autos

    def Get_Data(self):
        data_list = [self.total_autos, self.autos, self.username]
        return data_list

    def Tick(self, tickrate = 60):
        global balance
        if tickrate == 0:
            a = 2
            for i in range(40):
                a = a * i
        else:
            for auto in self.autos:
                if auto == "spoon_draw":
                    balance += (0.2 * self.up_spoon_draw) / tickrate

                if auto == "spoon_tree":
                    balance += (1 * self.up_spoon_tree) / tickrate

                if auto == "spoon_cave":
                    balance += (10 * self.up_spoon_cave) / tickrate

                if auto == "spoon_church":
                    balance += (65 * self.up_spoon_church) / tickrate



    def Check_Other(self):
        # check for milestones
        self.milestones = ["1000spoon", "1234"]




win = Tk()


def click():
    print("Click")

def RunGame(balance, datafile):
    for widget in win.winfo_children():
        widget.destroy()

    win.geometry(str(screen_x) + "x" + str(screen_y) + "+-10+0")
    win.title("The Game Title. Please Work This Time.")

    win.update()

    frame = Frame(win, width=screen_x, height=screen_y)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    win.update()

    #img_background = ImageTk.PhotoImage(Image.open("images/menu_background.png"))

    game_back = Label(frame, image=img_background)
    game_back.pack(anchor="center")
    win.update()


    #img_click = ImageTk.PhotoImage(Image.open("images/Nana_bek.png"))
    nana_click = Button(frame, text="", command=click, image=img_click, borderwidth=0, activebackground="#9ad9ea", background="#9ad9ea")
    nana_click.place(anchor="center", x=screen_x / 2 , y=screen_y / 2)
    global spdraw
    global sptree

    img_sptree = Label(frame, image=spdraw)
    img_sptree.place(x=screen_x - 150, y=75 + 50)

    img_sptree = Label(frame, image=sptree)
    img_sptree.place(x=screen_x - 150, y=75 + 100)








def LoadGame():
    pb1 = tkinter.ttk.Progressbar(win, orient=HORIZONTAL, length=100, mode='determinate')
    pb1.place(anchor='center', x=250, y=125,)
    win.update()

    try:
        money_file = open("Data/money.txt", encoding="utf8")
        balance_encoded = money_file.read()
        money_file.close()
        balance = decode(balance_encoded)
        balance = float(balance).__round__()
        balance = int(balance)
        data_f = open("Data/datalist.txt", encoding="utf8")
        data = data_f.read()
        data_f.close()
        datafile = decode(data)
        datafile = ast.literal_eval(datafile)

        # Update Progress Bar
        pb1['value'] += 25
        win.update()
    except:
        print("The Anti-Tamper System Has Detected A Incorrect Encoding Method Used...")
        Answered = False
        while Answered == False:
            user = input("Do you want for us to reset the damaged files? (y/n)")
            if user == "y":
                Answered = True # Reset Data
                print("Replacing Files. A Reset Is Needed...")
                time.sleep(1)
                dataA = "ACa62ac2 -tutk-c"
                dataB = "ekZ"
                f = open("Data/money.txt", "w")
                f.write(dataB)
                f.close()
                f = open("Data/datalist.txt", "w")
                f.write(dataA)
                f.close()

            elif user == "n":
                Answered = True
                print("Proceeding With Damaged Files The Game Will Most Likely Crash...")
                time.sleep(2)
            else:
                print("Invalide Input! | (y/n) | no caps")

    # Generates All Autos

    auto = Autos(datafile)

    auto.New_Auto("title", 0, 0)
    auto.New_Auto("spoon_draw", 10, 0.1)
    auto.New_Auto("spoon_tree", 100, 1)
    auto.New_Auto("spoon_cave", 1500, 10)
    auto.New_Auto("spoon_church", 11500, 65)

    pb1['value'] += 25
    win.update()

    # Load All Auto Images
    global spdraw
    global sptree


    spdraw = ImageTk.PhotoImage(Image.open("images/Autos/spoon_draw.png"))
    sptree = ImageTk.PhotoImage(Image.open("images/Autos/spoon_tree.png"))
    spcave = ImageTk.PhotoImage(Image.open("images/Autos/spoon_cave.png"))
    spchurch = ImageTk.PhotoImage(Image.open("images/Autos/spoon_church.png"))

    pb1['value'] += 25
    win.update()

    # Sumin else
    global img_background
    global img_click

    img_background = ImageTk.PhotoImage(Image.open("images/background.png"))
    img_click = ImageTk.PhotoImage(Image.open("images/Nana_bek.png"))

    pb1['value'] += 25
    win.update()
    time.sleep(0.2)

    RunGame(balance, datafile)





win.geometry("500x200")
win.title("Game Loader")
frame = Frame(win, width=screen_x, height=screen_y)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("images/menu_background.png"))
# Create a Label Widget to display the text or Image

mainback = Label(frame, image = img)
mainback.pack()

StartButton =  Button(frame, text="Press To Start", command=LoadGame)
StartButton.place(x=250, y=100, anchor=CENTER)



win.mainloop()

# Make Window
