"""
importing the module for creating and defining function and commands
that work for this."""
import os
from os import mkdir as create
# importing os, time, builtins, testmode
import time
from builtins import print as printdata

"""creating a class with the name function
"""


class Functions:
    """This is main heart for the application.
    """
    def __init__(self, userid):
        """We create a user id for each person and save it into root file."""
        self.userid = userid
        self.pp = os.getcwd()
        self.p = f"{self.pp}\\root\\{self.userid}\\"
        self.fname = None
        self.bool = None
        self.fath = None
        self.filename = None
        self.fname = None
        self.input = None
        self.waste = None
        self.filename = None
        self.fname = None
        self.data = None
        self.fun = None
        self.samin = None
        self.name = None
        self.cool = None
        self.commander = None
        self.machine = None
        total_size = None
        self.pammi = None
        self.path =None
        self.fol = None
        try:
            create(self.p)
        except Exception:
            pass

    def creating_the_folder(self, name):
        """defining a function with bool
        """
        self.fname = name
        self.bool = False
        self.fath = os.path.join(self.p, self.fname)
        try:
            create(self.fath)
            self.bool = True
        except FileExistsError:
                printdata("File Exists")
        finally:
            return self.bool

    def writing_the_file(self, fname, name, inputid):
        """defining another function which  consists the inputs
        """
        self.filename = name
        self.fname = f"{fname}\\"
        self.input = inputid
        self.waste = False
        try:
            self.pammi = os.path.join(self.p, self.fname)
            self.path = os.path.join(self.pammi, self.filename)
            with open(self.path, 'w') as wr:
                wr.writelines(self.input)
                self.waste = True
        except Exception as exception:
            printdata(exception)
        finally:
            return self.waste

    def reading_the_file(self, fname, name):
        """ defining another file for reading
        """
        self.filename = name
        self.fname = f"{fname}\\"
        self.data = ''
        try:
            self.pammi = os.path.join(self.p, self.fname)
            self.path = os.path.join(self.pammi, self.filename)
            with open(self.path, 'r') as r:
                self.data = r.read()
        except Exception as exception:
            return printdata(exception)
        finally:
            return " ".join(self.data)

    def list_of(self):
        """defining another function which shows list of commands
        """
        self.fun = os.listdir(self.p)
        self.samin = []
        self.commander = []
        self.machine = []
        total_size = 0
        for firs in self.fun:
            self.fol = os.path.join(self.p, firs)
            self.machine.append(time.ctime(os.path.getmtime(f"{self.fol}")))
            self.commander.append(time.ctime(os.path.getctime(f"{self.fol}")))
            for path, dirs, files in os.walk(self.fol):
                for fun in files:
                    fatpar = os.path.join(path, fun)
                    total_size += os.path.getsize(fatpar)
            self.samin.append(total_size)
        return self.fun, self.samin, self.commander, self.machine

    def change_the_folder_path(self, name):
        """defining the_folder_path function to change the folder path
        """
        self.name = name
        self.cool = False
        os.chdir(self.p)
        try:
            os.chdir(name)
            self.cool = True
        except Exception:
            pass
        finally:
            return self.cool
