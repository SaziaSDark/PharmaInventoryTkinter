import unittest
from main2 import Pharma
#import tkinter as tk

import mysql.connector
from mysql.connector import Error
from tkinter import ttk
#from functools import partial

#from tkinter import messagebox

class MyTestCase(unittest.TestCase):
    def logintest(self):
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="",
                                                 database="pharmaproject")
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor2 = connection.cursor()
                cursor2.execute("select database();")
                record = cursor2.fetchone()
                print("You're connected to database: ", record)


                c=Pharma(cursor2)
                c.login()
                self.assertEqual(c.login(),"takes in logininfo")
        except Error as f:
            print("Error while connecting to MySQL", f)
    def addTest(self):
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="",
                                                 database="pharmaproject")
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor2 = connection.cursor()
                cursor2.execute("select database();")
                record = cursor2.fetchone()
                print("You're connected to database: ", record)


                c=Pharma(cursor2)

                print(c.add("BEXOVID",ttk))
        except Error as f:
            print("Error while connecting to MySQL", f)



    def removeTest(self):
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="",
                                                 database="pharmaproject")
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor2 = connection.cursor()
                cursor2.execute("select database();")
                record = cursor2.fetchone()
                print("You're connected to database: ", record)


                c=Pharma(cursor2)

                print(c.remove("BEXOVID", ttk))
        except Error as f:
            print("Error while connecting to MySQL", f)


    def buttonTest(self):
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="",
                                                 database="pharmaproject")
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor2 = connection.cursor()
                cursor2.execute("select database();")
                record = cursor2.fetchone()
                print("You're connected to database: ", record)


                c=Pharma(cursor2)
                c.login()
                self.assertEqual(c.login(),"takes button to search")
        except Error as f:
            print("Error while connecting to MySQL", f)


    def login2Test(self):
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="",
                                                 database="pharmaproject")
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor2 = connection.cursor()
                cursor2.execute("select database();")
                record = cursor2.fetchone()
                print("You're connected to database: ", record)


                c=Pharma(cursor2)
                c.login()
                print(c.login2("sazia","password"))
        except Error as f:
            print("Error while connecting to MySQL", f)


    def prices3Test(self):
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="",
                                                 database="pharmaproject")
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor2 = connection.cursor()
                cursor2.execute("select database();")
                record = cursor2.fetchone()
                print("You're connected to database: ", record)


                c=Pharma(cursor2)
                c.login()
                self.assertEqual(c.prices2(12),12)
        except Error as f:
            print("Error while connecting to MySQL", f)


    def searcht(self):
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="",
                                                 database="pharmaproject")
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor2 = connection.cursor()
                cursor2.execute("select database();")
                record = cursor2.fetchone()
                print("You're connected to database: ", record)


                c=Pharma(cursor2)
                c.login()
                print(c.search("BEXOVID"))
        except Error as f:
            print("Error while connecting to MySQL", f)





if __name__ == '__main__':
    unittest.main()
