import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui
from PIL import Image
import math
import ast
import threading
import ctypes
import time
import random


user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
scrx, scry = screensize

code = [10, "abcdefghijklmnopqrstuvwxyz0123456789+-. _*/\[](){},':;!@$฿%^&<>?=~`"] # character code

CLICK = (0, 0)
clicked_Check = False
ALLAUTOS = []

# Display Current Problems That MAY Be Fixed
f = open("config.txt", "r")
config = f.read()
f.close()

if config == "config_warnings = True":
    config_warning = True
elif config == "config_warnings = False":
    config_warning = False
else:
    print("CONFIG FILE TAMPERED OR INCORRECT SPELLING")


if config_warning == True:
    print("= = = = = Problems = = = = =")
    print("")
    print("- No Click Animation")
    print(" -Bal Still Increased")
    print("")
    print("- ")
    print("")
    print("")
    print(" *** change 'warnings=True' to False in the config.txt file to remove this warning ***")
    print("")
    time.sleep(5)



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

def GetData(): # anti tamper
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
        return balance, datafile
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




class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Nana B Clicker'
        self.left = 0
        self.top = 0

        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        x, y = screensize
        mx = x // 2
        my = y // 2
        self.middle_screen = (mx, my)

        self.screensize = screensize

        self.width = x
        self.height = y
        self.initUI()
        self.auto_data = AUTODATA
        self.i = 0

    def initUI(self):
        global balance
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap("images/background.png")
        x, y = self.screensize
        mx, my = self.middle_screen
        self.resize(x, y)
        label.setPixmap(pixmap)

        x = x - 250

        global nana_bek_rect
        nana_bek_rect = self.Blit_Image(self.middle_screen, "images/Nana_bek.png", center=True, Return=True)
        self.nana_bek_rect = nana_bek_rect
        self.Blit_Image((x, 0), "images/Autos/Title.png") # All Images
        rect_spoon_draw = self.Blit_Image((x, 50), "images/Autos/spoon_draw.png")
        rect_spoon_tree = self.Blit_Image((x, 100), "images/Autos/spoon_tree.png")
        rect_spoon_cave = self.Blit_Image((x, 150), "images/Autos/spoon_cave.png")
        rect_spoon_church = self.Blit_Image((x, 200), "images/Autos/spoon_church.png")

        self.spoondraw1 = QLabel(self)
        self.spoondraw2 = QLabel(self)

        self.spoontree1 = QLabel(self)
        self.spoontree2 = QLabel(self)

        self.spooncave1 = QLabel(self)
        self.spooncave2 = QLabel(self)

        self.spoonchurch1 = QLabel(self)
        self.spoonchurch2 = QLabel(self)


        self.Blit_Image((x, 50), "images/Autos/lines.png") # For Every auto add a new one off these
        self.Blit_Image((x, 100), "images/Autos/lines.png")
        self.Blit_Image((x, 150), "images/Autos/lines.png")
        self.Blit_Image((x, 200), "images/Autos/lines.png")


        self.display_bal = QLabel(self)
        self.display_bal.setText(str(round(balance)) + " Nanas Silver Spoons")
        self.display_bal_size = self.display_bal.size().width()
        self.display_bal.move(mx - (self.display_bal_size // 2), 50)


        # Set Fonts
        app.setStyleSheet("QLabel{font-size: 18pt;}")


        # blit images


    def Blit_Image(self, xy, location, center = False, Return = False):
        label = QLabel(self)
        pixmap = QPixmap(location)
        label.setPixmap(pixmap)
        x, y = xy
        if center == True:
            im = Image.open(location)
            width, height = im.size
            new_x = x - (width // 2)
            new_y = y - (height // 2)
            label.move(new_x, new_y)
        else:
            label.move(x, y)

        if Return == True:
            return (new_x, new_y, width ,height)

    def mouseReleaseEvent(self, QMouseEvent):
        global clicked_Check
        global CLICK
        cursor = QtGui.QCursor()
        cursor = cursor.pos()
        cursor = str(cursor).split("(")
        cursor = cursor[1].split(")")
        cursor = cursor[0].split(", ")
        CLICK = (int(cursor[0]), int(cursor[1]))
        clicked_Check = True
        if collide(CLICK, self.nana_bek_rect):
            C = threading.Thread(target=self.click_handler, args=[CLICK])
            C.start()

    def display(self, ALL):
        self.i += 1
        mx, my = self.middle_screen
        self.display_bal.setText(str(round(balance)) + " Nanas Silver Spoons")
        self.display_bal_size = self.display_bal.size().width()
        self.display_bal.move(mx - (self.display_bal_size // 2), 50)

        # Display Numbers
        if self.i >= 10:
            self.i = 0
            # Get x pos
            x, y = self.screensize
            x1 = x - 164
            x2 = x - 80

            # Set Vars
            spoon_draws = 0
            spoon_trees = 0
            spoon_caves = 0
            spoon_churchs = 0

            # Run Check
            for AUTO in ALL:
                if AUTO == "spoon_draw":
                    spoon_draws += 1
                if AUTO == "spoon_tree":
                    spoon_trees += 1
                if AUTO == "spoon_cave":
                    spoon_caves += 1
                if AUTO == "spoon_church":
                    spoon_churchs += 1


            self.spoondraw1.setText("10")
            self.spoondraw1.move(x1, 50 + 13)
            self.spoondraw1.adjustSize()

            self.spoondraw2.setText(str(spoon_draws))
            self.spoondraw2.move(x2, 50 + 13)
            self.spoondraw2.adjustSize()

            self.spoontree1.setText("100")
            self.spoontree1.move(x1, 100 + 13)
            self.spoontree1.adjustSize()

            self.spoontree2.setText(str(spoon_trees))
            self.spoontree2.move(x2, 100 + 13)
            self.spoontree2.adjustSize()

            self.spooncave1.setText("1500")
            self.spooncave1.move(x1, 150 + 13)
            self.spooncave1.adjustSize()

            self.spooncave2.setText(str(spoon_caves))
            self.spooncave2.move(x2, 150 + 13)
            self.spooncave2.adjustSize()

            self.spoonchurch1.setText("11500")
            self.spoonchurch1.move(x1, 200 + 13)
            self.spoonchurch1.adjustSize()

            self.spoonchurch2.setText(str(spoon_churchs))
            self.spoonchurch2.move(x2, 200 + 13)
            self.spoonchurch2.adjustSize()







    def click_handler(self, xy):
        pass


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

        self.check_click()


        self.auto_rects = []
        self.username = name

        print("Auto Class Made")

    def New_Auto(self, Name, Cost, NSPps): # image files must be 50 x 50 pixels and JUST say the image name aka Clicker.png
        global scrx
        y_coord = self.tautos * 50
        x_coord = scrx - 250
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


balance, datafile = GetData()

app = QApplication(sys.argv)

# Init Autos

auto = Autos(datafile)

auto.New_Auto("title", 0, 0)
auto.New_Auto("spoon_draw", 10, 0.1)
auto.New_Auto("spoon_tree", 100, 1)
auto.New_Auto("spoon_cave", 1500, 10)
auto.New_Auto("spoon_church", 11500, 65)



ex = App()
i = 0


def save(auto):
    # Save Money
    global balance
    cbalance = round(balance)
    encoded = encode(str(cbalance))
    f = open("Data/money.txt", "w", encoding="utf-8")
    f.write(encoded)
    f.close()

    # Save Data On Autos
    data = auto.Get_Data()
    encoded = encode(str(data))
    f = open("Data/datalist.txt", "w", encoding="utf-8")
    f.write(encoded)
    f.close()



FPS = 60
MSPF = 1000 / FPS
last_frame = time.perf_counter() * 1000

def GameLoop():
    TICK = 0
    while True:
        now = time.perf_counter() * 1000

        ex.display(auto.Get_autos())
        auto.check_click()
        auto.Tick()

        last_frame = time.perf_counter() * 1000
        elapsed = now - last_frame
        time.sleep(max(0, (now + MSPF) / 1000.0 - time.perf_counter()))


        TICK += 1 # wait 5s then Save
        if TICK >= (5 * FPS):
            TICK = 0
            save(auto)
        try:
            if stop_threads == True:
                break
        except:
            pass

t = threading.Thread(target=GameLoop)
t.start()


ex.show()
app.exec_()

# Close The Program If Window Is Closed
stop_threads = True
sys.exit("Window Closed And Script Attached Errored")
