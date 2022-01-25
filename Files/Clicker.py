import pygame
import ctypes
import math

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
sx, sy = screensize
screen_middle = (sx / 2, sy / 2)
# pygame stuff
win = pygame.display.set_mode((screensize))
pygame.display.set_caption("Clicker")

pygame.init()

clock = pygame.time.Clock()


# Load Start Up
background_small = pygame.image.load("images/background.png")
background = pygame.transform.scale(background_small, screensize)
win.blit(background,(0, 0))
pygame.display.update()

# Load Images
nana_bek_small = pygame.image.load("images/Nana_bek.png")
nana_bek = pygame.transform.scale(nana_bek_small, (462, 561))
nana_bek_rect = nana_bek.get_rect()
x, y = screen_middle
nana_bek_rect.move_ip(x - 231, y - 280.5)


# Load Auto Images
auto_test_img = pygame.image.load("images/Autos/test.png")





# Encoding and Decoding for money and other stored Data
code = [10, "abcdefghijklmnopqrstuvwxyz0123456789+-. _*/\[](){},':;!@$฿%^&<>?=~`"] # character code

def encode(val, charset):
    encoded = ""
    for idx in range(len(str(val))):
        tempEnc = encoded
        encoded = tempEnc + str(charset[0] + charset[1].index(str(val[idx])))
    return encoded

def decode(val, charset):
    charNum = 0
    decoded = ""
    for index in range(math.ceil(len(str(val)) / 2)):
        idy = str(val)[charNum] + str(val)[charNum + 1]
        charNum += 2
        tempDc = decoded
        decoded = tempDc + charset[1][int(idy) - 10]
    return decoded



# Define Autos / Buildings / do clicking for you
class Autos():
    def __init__(self, datalist):
        name = datalist[1]
        self.total_autos = 0
        self.autos = []
        self.auto_data = []
        self.auto_rects = []
        self.username = name
        print("Auto Class Made")

    def New_Auto(self, Name, Cost, NSPps): # image files must be 50 x 50 pixels and JUST say the image name aka Clicker.png
        global sx
        y_coord = self.total_autos * 50
        x_coord = sx - 100
        self.autos.append((Name, Cost, x_coord, y_coord))
        self.auto_data.append((Name, NSPps))
        x_pos = x_coord
        y_pos = y_coord
        width = 100
        height = 50

        # make the rectangle variable
        rectangle = pygame.Rect(x_pos, y_pos, width, height)
        self.auto_rects.append(rectangle)
        print("Generated New Auto Named '" + Name + "', Costing: " + str(Cost) + " Silver Spoons")


    def BLIT(self):
        for auto in self.autos:
            N, C, x, y = auto
            if N == "test":
                win.blit(auto_test_img, (x, y))


    def check_click(self, x, y):
        max_x, max_y = screensize
        if nana_bek_rect.collidepoint(x, y): # quickly check they are not just clicking for spoons to save some time.
            pass
        else:

            i = 0
            for button in self.auto_rects:
                if button.collidepoint(x, y):
                    Clicked = i

                i += 1
            try:
                i += Clicked # Test if Anything Is clicked
                name, amount = self.auto_data[Clicked]
                if name == "test":
                    pass
            except:
                pass

    def Get_Data(self):
        data_tuple = (self.total_autos, self.autos, self.username)



def save():
    # Save Money
    global balance
    encoded = encode(str(balance), code)
    f = open("Data/money.txt", "w")
    f.write(encoded)
    f.close()




def set_text(string, coordx, coordy, fontSize): #Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize)
    text = font.render(string, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)


def display_info(balance):
    global screen_middle
    x = screen_middle[0]
    if balance <= 1:
        bal = str(balance) + " Nana's Silver Spoon"
    else:
        bal = str(balance) + " Nana's Silver Spoons"
    s = set_text(bal, x, 100, 20)
    win.blit(s[0], s[1])

# Getting All Needed Data For Game. - MAIN BRANCH

# Get / Decode Money - SUB BRANCH
money_file = open("Data/money.txt", "r")
balance_encoded = money_file.read()
money_file.close()
balance = decode(balance_encoded, code)
balance = int(balance)

data_f = open("Data/datalist.txt")
data = data_f.read()
data_f.close()
datafile = decode(data, code)


# Init Autos
auto = Autos(datafile)

# Generate Autos - They Will Appear top to bottom in the order that they are here.
auto.New_Auto("test", 10, 1)

# Tests Before Game Loads


save()


run = True
TICKS = 0
while run:
    win.blit(background,(0, 0))
    win.blit(nana_bek, nana_bek_rect)
    auto.BLIT()
    display_info(balance)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Detect If nana Is Clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                x, y = pygame.mouse.get_pos()
                if nana_bek_rect.collidepoint(x, y):
                    balance += 1
                auto.check_click(x, y)

    pygame.display.flip()
    clock.tick(20) # finsih tick
    TICKS += 1
    if TICKS >= 100:
        save()
        TICKS = 0

pygame.quit()