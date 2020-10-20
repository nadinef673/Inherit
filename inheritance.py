from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Group 4")
window.configure()
window.geometry("1000x800")
window.grid()

num_1 = IntVar()
num_2 = IntVar()
num_3 = IntVar()
num_4 = IntVar()
option = StringVar()

def reset():
    top = Toplevel(padx=50, pady=50)
    top.grid(row=13, column=2)
    message = Label(top, text="Reset Complete")
    button = Button(top, text="OK", command=top.destroy)

class sick:
    pass

class cancer:
    def __init__(self, window):
        myFrame = Frame(window)
        myFrame.grid(row=15, column=1)
        self.myButton = Button(window, text="Calculate", command=self.calculate)
        self.myButton.grid(padx=50, pady=80)

    def calculate(self):
        if self.medication > 600:
            messagebox.showinfo("Showinfo", "Sorry we cannot treat you")
        else:

            messagebox.showinfo("Showinfo", "We can treat you")
            self.treatment = self.medication + self.scanfree
            print("The treatment for the patient is", self.treatment)

p1 = cancer(window)
p1.medication = 400
p1.scanfee = 200

class influenza(sick):
    def treatment(self):
        if self.scanfee < 600:
            print("We can not treat you")
        else:
            self.answer = self.medication + self.scanfee
            print(self.answer)

p2 = influenza()
p2.medication = 400
p2.scanfee = int(input("Enter scanfee amount:"))
p2.treatment()

main_class_label = Label(window, text="Sickness Code")
main_class_label.grid(row=1, column=1)

main_class_entry = Entry(window, textvariable = num_1)
main_class_entry.grid(row=1, column=2)

duration_label = Label(window, text="Duration of Treatment")
duration_label.grid(row=3, column=1)

duration_entry = Entry(window, textvariable = num_2)
duration_entry.grid(row=3, column=2)

days_label = Label(window, text="Weeks/Months")
days_label.grid(row=3, column=3)

dpn_label = Label(window, text="Doctor Practice Number")
dpn_label.grid(row=5, column=1)

dpn_entry = Entry(window, textvariable = num_3)
dpn_entry.grid(row=5, column=2)

fee_label = Label(window, text="Scan/Consultant Fee")
fee_label.grid(row=7, column=1)

fee_entry = Entry(window, textvariable = num_4)
fee_entry.grid(row=7, column=2)

R1 = Radiobutton(window, text="Cancer", value="cancer", var=option)
R1.grid(row=9, column=1)
R2 = Radiobutton(window, text="Influenza", value="influenza", var=option)
R2.grid(row=11, column=1)

amount_label = Label(window, text="Amount Paid For Treatment")
amount_label.grid(row=13, column=1)

calculate_button = Button(window, text="Calculate")

resetButton = Button(window, text="Clear", font=("Arial", 12, "bold"), relief=RAISED, bd=5, justify=CENTER,
                     highlightbackground="red", overrelief=GROOVE, activebackground="green", activeforeground="blue",
                     command=reset)
resetButton.grid(row=13, column=5, ipady=8, ipadx=12, pady=5, sticky=NW, padx=55)


window.mainloop()