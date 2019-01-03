from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()
class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)


        self.grid()

        mLabel = Label(master, text="Select Month", justify=RIGHT, font=("Arial", 20))
        mLabel.grid(row=1, column=0)

        rLabel = Label(master, text="Rent", justify=RIGHT, font=("Arial", 20))
        rLabel.grid(row=2, column=0, sticky=E)

        iLabel = Label(master, text="Income", justify=RIGHT, font=("Arial", 20))
        iLabel.grid(row=3, column=0, sticky=E)

        rDollar = Label(master, text="$", font=("Arial", 20))
        rDollar.grid(row=2, column=1, sticky=E)

        iDollar = Label(master, text="$", font=("Arial", 20))
        iDollar.grid(row=3, column=1, sticky=E)

        self.month = ttk.Combobox(master,
                                  values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                                  font=("Arial", 16), width=12, justify=RIGHT)
        self.month.grid(row=1, column=1, columnspan=2)

        self.rent = Text(master, font=("Arial", 16), width=8, height=1)
        self.rent.grid(row=2, column=2, sticky=W + E)

        self.income = Text(master, font=("Arial", 16), width=8, height=1)
        self.income.grid(row=3, column=2, sticky=W + E)

        remainder = Label(master, text="Remainder", justify=CENTER, font=("Arial", 20))
        remainder.grid(columnspan=3, row=4)

        remDollar = Label(master, text="$", font=("Arial", 20))
        remDollar.grid(row=4)

        self.remainderText = Text(master, font=("Arial", 22), width=14, height=1)
        self.remainderText.grid(columnspan=3, row=5)

        calculate = Button(master, text="Calculate", command=self.calcClick, font=("Arial", 20))
        calculate.grid(columnspan=3, row=6)

        menubar = Menu(root)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.saveClick)
        filemenu.add_command(label="Save As", command=self.saveasClick)
        filemenu.add_command(label="Open", command=self.openClick)
        menubar.add_cascade(label="File", menu=filemenu)

        windowmenu = Menu(menubar, tearoff=0)
        windowmenu.add_command(label="GPA Calculator", command=self.create_gpa)
        menubar.add_cascade(label="Window", menu=windowmenu)


        root.config(menu=menubar)




    def create_gpa(self):
        t = Toplevel(self)
        t.wm_title("GPA Calculator")


    def calcClick(self):

        #self.rent.insert(END, 0)
        #self.income.insert(END, 0)

        self.i = float(self.income.get("1.0", END))
        self.r = float(self.rent.get("1.0", END))

        self.remainderText.delete("1.0", END)
        self.remainderText.insert(END, round(self.i-self.r,2))

    def openClick(self):

        if self.month.get() != "":
            self.month.set("")

        if self.rent.get("1.0", END):
            self.rent.delete("1.0", END)

        if self.income.get("1.0", END):
            self.income.delete("1.0", END)

        if self.remainderText.get("1.0", END):
            self.remainderText.delete("1.0", END)



        openFile = filedialog.askopenfile()

        title = openFile.name
        title = title[23:]
        title = title.replace("_Budget.txt", "")

        lines = openFile.readlines()

        oMonth = lines[0]
        oRent = lines[1].replace("Rent:\t\t$", "")
        oIncome = lines[2].replace("Income:\t\t$", "")
        oRemainder = lines[4].replace("Remainder:\t$", "")

        self.month.insert(END, oMonth)
        self.rent.insert(END, oRent)
        self.income.insert(END, oIncome)
        self.remainderText.insert(END, oRemainder)

    def saveClick(self):
        if self.month.get() == "":
            print("No Month")

        else:
            m = "C:\\Users\\brian\\Budgets\\" + self.month.get() + "_Budget.txt"
            f = open(m, "w+")
            fileRent = "Rent:\t\t$" + str(float(self.rent.get("1.0", "8.0")))
            fileIncome = "Income:\t\t$" + str(float(self.income.get("1.0", "8.0")))
            month = self.month.get()

            f.write(month + "\n")
            f.write(fileRent + "\n")
            f.write(fileIncome + "\n")
            f.write("-------------------------\n")
            f.write("Remainder:\t$" + self.remainderText.get("1.0", END))

    def saveasClick(self):
        if self.month.get() == "":
            print("No Month")

        else:

            my_filetypes = [('text files', '.txt')]
            saveas = filedialog.asksaveasfile(mode="w", defaultextension=".txt", title="Testingdefault='.txt", filetypes=my_filetypes)

            fileMonth = str(self.month.get())
            fileRent = "Rent:\t\t$" + str(self.r)
            fileIncome = "Income:\t\t$" + str(self.i)
            fileRemainder = "Remainder:\t$" + self.remainderText.get("1.0", END)

            self.saved = fileMonth + "\n" + fileRent +"\n" + fileIncome + "\n" + "-------------------------\n" + fileRemainder

            saveas.write(self.saved)
            saveas.close()




def hello():
    print("hello")




if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()



