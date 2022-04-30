import tkinter as tk

import mysql.connector
from mysql.connector import Error
from tkinter import ttk
from functools import partial

from tkinter import messagebox


class Pharma:
    def __init__(self, cursors):
        self.cursor = cursors
        self.totals=[]


        self.idx = 0
        self.password = 0

    def add(self, name, s):
        x2 = s.get()
        name2 = name
        query111 = "UPDATE bigtable SET Available=Available-1 WHERE ProductName=(%s) AND PharmaName=(%s)"
        self.cursor.execute(query111, (name2, x2))
        arr = []
        query2 = "SELECT price FROM bigtable WHERE ProductName=(%s) AND PharmaName=(%s)"
        self.cursor.execute(query2, (name2, x2))
        arr3 = []
        thistuple6 = ()
        myresultp2 = self.cursor.fetchall()
        for got in myresultp2:
            thistuple6 = (got[0],)
        priceAdd = thistuple6[0]

        adder=self.prices(priceAdd)
        print("returns prices function")
    def done(self):
        print(sum(self.totals))
        zi=sum(self.totals)
        messagebox.showinfo("your total",zi)


    def remove(self, name2, s2):
        x2 = s2.get()
        name2 = name2
        query112 = "UPDATE bigtable SET Available=Available+1 WHERE ProductName=(%s) AND PharmaName=(%s)"
        self.cursor.execute(query112, (name2, x2))
        arr = []
        query22 = "SELECT price FROM bigtable WHERE ProductName=(%s) AND PharmaName=(%s)"
        self.cursor.execute(query22, (name2, x2))
        arr3 = []
        thistuple7 = ()
        myresultp3= self.cursor.fetchall()
        for got2 in myresultp3:
            thistuple7 = (got2[0],)
        priceAdd2 = thistuple7[0]

        adder2 = self.prices2(priceAdd2)
        print(adder2)

    def prices(self, total):
        self.totals.append(total)

        x=sum(self.totals)
        return x

    def prices2(self,tots):
        self.totals.pop(-1)
        y=self.totals
        return y


    def login(self):
        root2 = tk.Tk()
        root2.title('Login')
        name_var = tk.StringVar()
        passw_var = tk.StringVar()

        lblfrstrow = tk.Label(root2, text="Username -")
        lblfrstrow.place(x=50, y=20)

        e = tk.Entry(root2, width=35, textvariable=name_var)
        e.pack()
        e.place(x=150, y=20, width=100)

        lblsecrow = tk.Label(root2, text="Password -")
        lblsecrow.place(x=50, y=50)
        p = tk.Entry(root2, width=35, textvariable=passw_var)
        p.pack()
        p.place(x=150, y=50, width=100)

        buttonCal = tk.Button(root2, text="login", command=partial(self.login2, e, p))
        print("takes in logininfo")
        buttonCal.grid(row=3, column=0)
        root2.mainloop()

    def login2(self, e, p):
        ep = e.get()
        pe = p.get()

        query7 = "SELECT * FROM login_info WHERE Password=(%s)"
        self.cursor.execute(query7, (pe,))

        myresult2 = self.cursor.fetchall()

        for row2 in myresult2:
            if (row2[0] == ep):
                if (row2[1] == pe):
                    self.buttons()
                    print("y")
                else:
                    print("wrong")
            else:
                print("wrong")



    def buttons(self):
        root3 = tk.Tk()
        root3.geometry("600x400")

        Search_var = tk.StringVar()
        # creating a label for
        # name using widget Label

        s = tk.Entry(root3, width=35, textvariable=Search_var)
        s.pack()
        s.place(x=150, y=20, width=100)
        search2 = tk.Button(root3, text='Search', command=partial(self.search, s))
        print("takes button to search")

        # placing the label and entry in
        # the required position using grid
        # method

        search2.grid(row=0, column=1)
        root3.mainloop()

    def search(self, s):
        ep2 = s.get()
        ws = tk.Tk()

        query1 = "SELECT * FROM bigTable WHERE productName=(%s)"

        self.cursor.execute(query1, (ep2,))
        myresultx = self.cursor.fetchall()
        thistuple = ()
        thistuple2 = ()
        dictio = []
        dictio2 = []
        thistuple = myresultx

        for row in myresultx:
            thistuple2= (row[0], row[1], row[2], row[3], row[4])

            dictio.append(thistuple2[0])
            dictio.append(thistuple2[1])
            dictio.append(thistuple2[2])
            dictio.append(thistuple2[3])
            dictio.append(thistuple2[4])

        ws.title(ep2)
        tv = ttk.Treeview(
            ws,
            columns=(1, 2, 3, 4, 5),
            show='headings',
            height=5
        )

        tv.pack()

        tv.heading(1, text='productname')
        tv.heading(2, text='pharmaname')
        tv.heading(3, text='available')
        tv.heading(4, text='price')
        tv.heading(5, text='address')

        print(dictio)

        tv.insert(parent='', index=0, iid=0, text='',
                  values=(dictio[0:1], dictio[1:2], dictio[2:3], dictio[3:4], dictio[4:5]))

        tv.insert(parent='', index=1, iid=1, text='',
                  values=(dictio[5:6], dictio[6:7], dictio[7:8], dictio[8:9], dictio[9:]))
        tv.insert(parent='', index=2, iid=2, text='',
                  values=(dictio[0:1], dictio[1:2], dictio[2:3], dictio[3:4], dictio[4:]))
        tv.insert(parent='', index=3, iid=3, text='',
                  values=(dictio[0:1], dictio[1:2], dictio[2:3], dictio[3:4], dictio[4:]))
        tv.insert(parent='', index=4, iid=5, text='',
                  values=(dictio[0:1], dictio[1:2], dictio[2:3], dictio[3:4], dictio[4:]))
        # selected = tv.selection()

        # these lines are binding mouse
        # buttons with the Frame widget

        add_frame = ttk.Frame(ws)
        add_frame.pack(pady=20)
        t1 = ttk.Label(ws, text="enter selection")
        t1.pack(pady=20)
        select = ttk.Entry(add_frame)
        select.grid(row=6, column=5)

        add_but1 = ttk.Button(ws, text="add", command=partial(self.add, ep2, select))

        add_but2 = ttk.Button(ws, text="remove", command=partial(self.remove, ep2, select))

        add_but3 = ttk.Button(ws, text="done", command=partial(self.done))
        print("search works")
        add_but1.pack(pady=20)
        add_but2.pack(pady=20)
        add_but3.pack(pady=20)

        # buttonCal65 = tk.Button(ws, text="add", command=partial(self.add, s,select))
        # buttonCal66 = tk.Button(ws, text="login", command=partial(self.remove, s, select))
        # buttonCal65.grid(row=10, column=5)
        # buttonCal66.grid(row=3, column=0)'''

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        ws.mainloop()


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
        pharma = Pharma(cursor2)
        pharma.login()

except Error as f:
    print("Error while connecting to MySQL", f)
