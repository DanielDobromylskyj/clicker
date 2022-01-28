import os
import shutil
import time
from distutils.dir_util import copy_tree


there = os.path.exists("new_game_files/clicker-main/Files/Data/version.txt")

if there == True:
    v1 = open("new_game_files/clicker-main/Files/Data/version.txt", "r")
    v1_r = v1.read()
    v1.close()

    v2 = open("Files/Data/version.txt")
    v2_r = v2.read()
    v2.close()

    if float(v1_r) > float(v2_r):
        user_input = input("Valid Update Detected! (" + v1_r + ") Input 0 to Cancel, Input 1 to Update")

        if user_input == "1":

            ui = input("Are you sure? (y/n)")

            if ui == "y":
                f = open("new_game_files/clicker-main/Files/Data/install.txt", "r") # All Current Possible Stuff Is: 0 = main, 1 = image, 2 = data, 3 = Updater
                install_data = f.read()
                f.close()

                test = install_data

                for element in range(0, len(test)):
                    chunk = test[element]

                    if chunk == "0":
                        shutil.copy("new_game_files/clicker-main/Files/Clicker.py", "Files/Clicker.py")

                    if chunk == "1":
                        copy_tree("new_game_files/clicker-main/Files/images", "Files/images")

                    if chunk == "3":
                        shutil.copy("new_game_files/clicker-main/Update.py", "Update.py")

                print("Update Complete! Cleaning Up")

                shutil.rmtree('new_game_files/clicker-main')

                print("Clean Up Complete. Exiting")
                time.sleep(3)
            elif ui == "n":
                print("Stopped Update.")
                time.sleep(3)

            else:
                print("Failed / Bad Input")
                time.sleep(3)



    elif float(v1_r) == float(v2_r):
        print("Both Versions Are The Same.")


    elif float(v1_r) < float(v2_r):
        print("Out-Dated Version. Exiting")
        time.sleep(3)
else:
    print("No Downloaded Update Detected. Is It In The Folder?")
    time.sleep(3)

