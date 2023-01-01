import tkinter as tk
import tkinter.messagebox
ans=1
font_style1=("Castellar",22)


def exitm(w):
    w.destroy()

def inc_a():
    a+=1


root=tk.Tk()
# root.geometry("350x350")
root.title("I <3 U")
root.config(bg="black")

def yay():
    root2=tk.Tk()
    root2.title("I LOVE MY AASTHA SO MUCH!")
    root2.config(bg="black")
    wr1=tk.Label(root2, text="Thank you for giving me a chance, Aastha!\nI LOVE YOU SO SO SO SO SO MUCH\n\nYou will be my valentine for forever\nIf I was there, I would have taken you on such a beautiful date today, \nbut the distance man \n*crying intensifies*\n\nI owe you a beautiful date now.\nWe will definitely go on a beautiful date, when we meet the next time ", font=font_style1)
    wr1.config(bg="black", fg="white")
    wr1.grid(row=0, column=0, padx=40, pady=30)

def repair_app2():
    # root.destroy()
    root1=tk.Tk()
    # root.geometry("350x350")
    root1.title("*crying* Why not?")
    root1.config(bg="black")

    wr1=tk.Label(root1, text="Please be my Valentine *sobbing* ??", font=font_style1)
    wr1.config(bg="black", fg="white")
    wr1.grid(row=0, column=0, columnspan=2, padx=40, pady=30)

    wb2=tk.Button(root1, text="OKAY", font=font_style1, command=lambda:[yay(), root1.destroy()])
    wb2.grid(row=1, column=0, padx=50, pady=(0,30))

    wb3=tk.Button(root1, text="NO", font=font_style1, command=lambda:[repair_app2(), root1.destroy()])
    wb3.grid(row=1, column=1, padx=50, pady=(0,30))


def repair_app():
    root.destroy()
    root1=tk.Tk()
    # root.geometry("350x350")
    root1.title("Please")
    root1.config(bg="black")

    wr1=tk.Label(root1, text="Aastha, will you be my Valentine ??", font=font_style1)
    wr1.config(bg="black", fg="white")
    wr1.grid(row=0, column=0, columnspan=2, padx=40, pady=30)

    wb2=tk.Button(root1, text="YES", font=font_style1, command=lambda:[yay(), root1.destroy()])
    wb2.grid(row=1, column=0, padx=50, pady=(0,30))

    wb3=tk.Button(root1, text="NO", font=font_style1, command=lambda:[repair_app2(), root1.destroy()])
    wb3.grid(row=1, column=1, padx=50, pady=(0,30))

    # root1.mainloop()



w=tk.Label(root, text= "WARNING!!!\nYOUR PC HAS BEEN HACKED!!", font=font_style1, padx= 20, pady= 20)
w.config(bg="black", fg="white")
w.grid(row=0, column=0)

wb2=tk.Button(root, text="Resolve the issue with your PC", font=font_style1, command=lambda:[repair_app()])
wb2.grid(row=2, column=0, padx=30, pady=(0, 30))


root.mainloop()