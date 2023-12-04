import tkinter as tk

x = 0
y = 0
z = 0
a = 0

def get1():
    x = inputBox1.get()
    inputBox1.delete(0, tk.END)
    inputBox1.focus()


def get2():
    y = inputBox2.get()
    inputBox2.delete(0, tk.END)
    inputBox2.focus()

def calculate():
    z = (x / 3) / 12
    a = z - y

    print("Your Maintenance Loan is £", x," \n Which per week is £", z)
    print("If your accommodation costs £", y," \n This means you have £", a," left over for other spending")

window = tk.Tk()

window.geometry("600x600")
window.title("University Cost Calculator")

inputBox1 = tk.Entry(text = 0)
btn1 = tk.Button(text = "Input Maintenance Loan", command = get1)
inputBox2 = tk.Entry(text = 0)
btn2 = tk.Button(text = "Input Weekly Accommodation Costs", command = get2)
btn3 = tk.Button(text = "Calculate", command = calculate)

inputBox1.grid(row =  1, column = 1)
btn1.grid(row =  1, column = 2)
inputBox2.grid(row =  2, column = 1)
btn2.grid(row =  2, column = 2)
btn3.grid(row =  3, column = 1)

window.mainloop()