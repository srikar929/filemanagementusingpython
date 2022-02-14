# This module has the server code and by using functions
import fileinput
from Functions import Functions
import os
# importing the functions

async def login_code(getting, putting):
    """using async def for defining login_code to logging in.
    """
    matter = """login format
    please Enter LoginID   : """
    putting.write(matter.encode())
    msggg = await getting.read(100)
    userid = msggg.decode().strip()
    matter = "    Enter Password : "
    putting.write(matter.encode())
    msggg = await getting.read(100)
    password = msggg.decode().strip()
    p = os.getcwd()
    p = p + "\\root\\admin\\Register.txt"
    filepath = f"{p}"
    z = 0
    y = True
    with open(filepath, 'r') as p:
        for line in p:
            if userid in line:
                if password in line:
                    z = 1
                    if "logged" in line:
                        matter = "You have logged in already\nAccess Denied"
                        putting.write(matter.encode())
                        y = False
                        break

    if y:
        for line in fileinput.FileInput(filepath, inplace=1):
            if userid in line:
                if password in line:
                    line = line.rstrip()
                    line = line.replace(line, line + "logged\n")
            print(line, end='')
    if z != 1:
        matter = "The entered are Invalid Username or Password"
        putting.write(matter.encode())
    elif z == 1 and y:
        try:
            matter = """
            You have logged in.
            NAMASTE
            the following commands:
            1.creation of a folder
            2.writing in a file
            3.Reading what is in a file
            4.all the folders list
            5.changing the name of the folder
            0.signout"""
            putting.write(matter.encode())
            user = Functions(userid)
            while True:
                msggg = await getting.read(100)
                cmndch = msggg.decode().strip()
                """creation of a folder
                """
                if cmndch == '1':
                    msggg = await getting.read(100)
                    fname = msggg.decode().strip()
                    z = user.creating_the_folder(fname)
                    if z:
                        matter = "The Folder is created!"
                        putting.write(matter.encode())
                    else:
                        matter = "This Folder already exists"
                        putting.write(matter.encode())
                elif cmndch == '2':
                    """enter the folder name
                    """
                    matter = "Enter the folder name : "
                    putting.write(matter.encode())
                    msggg = await getting.read(50)
                    folname = msggg.decode().strip()
                    matter = "Enter the file name : "
                    putting.write(matter.encode())
                    msggg = await getting.read(50)
                    filename = msggg.decode().strip()
                    matter = "Enter the msg : "
                    putting.write(matter.encode())
                    msggg = await getting.read(50)
                    imsggg = msggg.decode().strip()
                    i = user.writing_the_file(folname, filename, imsggg)
                    if i:
                        matter = "File Created"
                        putting.write(matter.encode())
                elif cmndch == '3':
                    """reading what is in a file
                    """
                    matter = "Enter the folder name : "
                    putting.write(matter.encode())
                    msggg = await getting.read(100)
                    folder_name = msggg.decode().strip()
                    matter = "Enter the file name : "
                    putting.write(matter.encode())
                    msggg = await getting.read(100)
                    filename = msggg.decode().strip()
                    k = str(user.reading_the_file(folder_name, filename))
                    putting.write(k.encode())
                elif cmndch == '4':
                    """list of all the folders
                    """
                    lname, lsize, lcr, lmod = user.list_of()
                    matter = "Name      Size         Created          Modified"
                    putting.write(matter.encode())
                    msggg = await getting.read(100)
                    matter = msggg.decode().strip()
                    sname = str(" ".join(lname))
                    putting.write(sname.encode())
                    msggg = await getting.read(100)
                    matter = msggg.decode().strip()
                    ssize = str(" ".join(map(str, lsize)))
                    putting.write(ssize.encode())
                    msggg = await getting.read(100)
                    matter = msggg.decode().strip()
                    scr = str("  ".join(map(str, lcr)))
                    putting.write(scr.encode())
                    msggg = await getting.read(100)
                    matter = msggg.decode().strip()
                    smod = str("  ".join(map(str, lmod)))
                    putting.write(smod.encode())
                    msggg = await getting.read(100)
                    matter = msggg.decode().strip()
                elif cmndch == '5':
                    """changing the path of the folder
                    """
                    matter = "Enter Folder path : "
                    putting.write(matter.encode())
                    msggg = await getting.read(100)
                    nname = msggg.decode().strip()
                    m = user.change_the_folder_path(nname)
                    if m:
                        matter = "Changed successfully"
                    else:
                        matter = "No such file exists"
                    putting.write(matter.encode())

                elif cmndch == '0':
                    break
        except Exception as e:
            print(e)
        finally:
            """  signout successfully
            """
            for line in fileinput.FileInput(filepath, inplace=1):
                if userid in line:
                    if password in line:
                        line = line.rstrip()
                        line = line.replace(line, f"{userid}:{password},\n")
                print(line, end='')
            matter = "Log Out Successfull"
            putting.write(matter.encode())
