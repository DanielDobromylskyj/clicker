import pygame
import ctypes
import math

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
sx, sy = screensize
screen_middle = (sx / 2, sy / 2)

win = pygame.display.set_mode((screensize))
pygame.display.set_caption("Clicker")

pygame.init()

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
        self.total_autos = 0
        self.autos = []
        self.auto_data = []
        print("Auto Class Made")

    def New_Auto(self, Name, Cost, NSPps): # image files must be 50 x 50 pixels and JUST say the image name aka Clicker.png
        global sx
        y_coord = self.total_autos * 50
        x_coord = sx - 100
        self.autos.append((Name, Cost, x_coord, y_coord))
        self.auto_data.append((Name, NSPps))
        print("Generated New Auto Named '" + Name + "', Costing: " + str(Cost) + " Silver Spoons")


    def BLIT(self):
        for auto in self.autos:
            N, C, x, y = auto
            if N == "test":
                win.blit(auto_test_img, (x, y))



auto = Autos([("test", 1)])
auto.New_Auto("test", 10, 1)

def save():
    # Save Money
    global balance
    encoded = encode(str(balance), code)
    f = open("Data/money.txt", "w")
    f.write(encoded)
    f.close()
    # Save Autos





# Getting All Needed Data For Game.

# Get / Decode Money
money_file = open("Data/money.txt", "r")
balance_encoded = money_file.read()
money_file.close()
balance = decode(balance_encoded, code)



# Tests Before Game Loads
save()


run = True

while run:
    win.blit(background,(0, 0))
    win.blit(nana_bek, nana_bek_rect)

    auto.BLIT()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Detect If nana Is Clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                x, y = pygame.mouse.get_pos()
                if nana_bek_rect.collidepoint(x, y):
                    print("clicked")

    pygame.display.flip()

pygame.quit()