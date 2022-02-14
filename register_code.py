# this module is about registering and logging
import os
async def register_code(getting, putting):
    """defining register_code function  with async def
    """
    matter = "what is your name :"
    putting.write(matter.encode())
    msggg = await getting.read(100)
    matter = "creation of user name : "
    putting.write(matter.encode())
    msggg = await getting.read(100)
    userid = msggg.decode().strip()
    matter = "your password should be entered :"
    putting.write(matter.encode())
    msggg = await getting.read(100)
    password = msggg.decode().strip()
    outplit = False
    p = os.getcwd()
    p = p + "\\root\\admin\\Register.txt"
    with open(f"{p}", 'r') as read:
        for line in read:
            if userid in line:
                if password in line:
                    outplit = True
                    break
    if not outplit:
        with open(f"{p}", 'a') as write:
            write.write(userid + ':')
            write.write(password + ', \n')
        matter = "The User has been Registered:-)."
        putting.write(matter.encode())
    else:
        matter = """The Request has been Denied\n
                    You are already Registered and you can login."""
        putting.write(matter.encode())
