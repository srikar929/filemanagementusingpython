# importing asyncio for this module of client_code
import asyncio
import time
from builtins import print as printdata
#  importing time etc.

#  using async def for defing the client code function
async def client_code():
    """the client code function is defined and an open connection to 9974 is given."""
    getting, putting = await asyncio.open_connection('127.0.0.1', 9974)
    matter = await getting.read(100)
    data = matter.decode().strip()
    printdata(data)
    choice = input()
    putting.write(choice.encode())
    if choice == '1':
        """creation of a folder
        """
        matter = await getting.read(100)
        incomdata = matter.decode().strip()
        name = input(incomdata)
        putting.write(name.encode())
        matter = await getting.read(100)
        incomdata = matter.decode().strip()
        userid = input(incomdata)
        putting.write(userid.encode())
        matter = await getting.read(100)
        incomdata = matter.decode().strip()
        password = input(incomdata)
        putting.write(password.encode())
        matter = await getting.read(100)
        incomdata = matter.decode().strip()
        print(incomdata)
    if choice != '1':
        matter = await getting.read(100)
        incomdata = matter.decode().strip()
        userid = input(incomdata)
        putting.write(userid.encode())
        matter = await getting.read(100)
        incomdata = matter.decode()
        password = input(incomdata)
        putting.write(password.encode())
        matter = await getting.read(10000)
        incomdata = matter.decode().strip()
        print(incomdata)
        if incomdata == "You have logged in already\nAccess Denied" or incomdata == "The entered are Invalid Username or Password":
            exit()
        while True:
            commandchoosed = input("Enter your choice : ")
            putting.write(commandchoosed.encode())
            if commandchoosed == '1':
                """creation of a folder
                """
                name = input("Enter folder name : ")
                putting.write(name.encode())
                matter = await getting.read(100)
                incomdata = matter.decode().strip()
                printdata(incomdata)
            elif commandchoosed == "2":
                """writing in a file
                """
                matter = await getting.read(50)
                incomdata = matter.decode().strip()
                folder_name = input(incomdata)
                putting.write(folder_name.encode())
                matter = await getting.read(50)
                incomdata = matter.decode().strip()
                filename = input(incomdata)
                putting.write(filename.encode())
                matter = await getting.read(50)
                incomdata = matter.decode().strip()
                imatter = input(incomdata)
                putting.write(imatter.encode())
                matter = await getting.read(100)
                incomdata = matter.decode().strip()
                printdata(incomdata)
            elif commandchoosed == "3":
                """reading in a file
                """
                matter = await getting.read(100)
                incomdata = matter.decode().strip()
                folname = input(incomdata)
                putting.write(folname.encode())
                matter = await getting.read(100)
                incomdata = matter.decode().strip()
                filename = input(incomdata)
                putting.write(filename.encode())
                matter = await getting.read(100)
                incomdata = matter.decode().strip()
                printdata(incomdata)
            elif commandchoosed == "4":
                """list all folders
                """
                matter = await getting.read(100)
                incomdata = matter.decode().strip()
                printdata(incomdata)
                putting.write("hi".encode())
                matter = await getting.read(100)
                sname = matter.decode().strip()
                name = list(sname.split(" "))
                putting.write("hello".encode())
                matter = await getting.read(20)
                ssize = matter.decode().strip()
                size = list(ssize.split(" "))
                putting.write("hello".encode())
                matter = await getting.read(90)
                scr = matter.decode().strip()
                cr = list(scr.split("  "))
                putting.write("hello".encode())
                matter = await getting.read(90)
                smod = matter.decode().strip()
                mod = list(smod.split("  "))
                putting.write("hello".encode())
                for fol in range(len(name)):
                    printdata(f"{name[fol]}  {size[fol]}   {cr[fol]}  {mod[fol]}")
            elif commandchoosed == '5':
                """changing the name of the file
                """
                valss = await getting.read(100)
                incomdata = valss.decode().strip()
                str1 = input(incomdata)
                putting.write(str1.encode())
                valss = await getting.read(100)
                incomdata = valss.decode().strip()
                printdata(incomdata)
            elif commandchoosed == "0":
                break
        valssa = await getting.read(100)
        incomdata = valssa.decode().strip()
        printdata(incomdata)
    putting.close()
asyncio.run(client_code())
