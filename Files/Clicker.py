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
# Load others


code = [10, "abcdefghijklmnopqrstuvwxyz0123456789+-. _*/\[](){},':;!@$฿%^&<>?=~`"]


def encode(val, charset):
    encoded = ""
    for idx in range(len(str(val))):
        tempEnc = encoded
        encoded = tempEnc + str(charset[0] + charset[1].index(str(val[idx])))
    print(encoded)
    return encoded


def decode(val, charset):
    charNum = 0
    decoded = ""
    for index in range(math.ceil(len(str(val)) / 2)):
        idy = str(val)[charNum] + str(val)[charNum + 1]
        charNum += 2
        tempDc = decoded
        decoded = tempDc + charset[1][int(idy) - 10]
    print(decoded)
    return decoded



def save():
    global balance
    encoded = encode(str(balance), code)
    f = open("Data/money.txt", "w")
    f.write(encoded)
    f.close()





money_file = open("Data/money.txt", "r")
balance_encoded = money_file.read()
money_file.close()

balance = decode(balance_encoded, code)
print("balnce: ", balance)
save()


run = True

while run:
    win.blit(background,(0, 0))
    win.blit(nana_bek, nana_bek_rect)#(sx/ 2-231, sy/ 2-280.5)




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