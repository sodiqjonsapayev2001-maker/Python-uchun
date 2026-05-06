from tkinter import *
def bosish(belgi):
    #Entry-ga matn qo'shish
    hozirgi = txt.get()
    txt.delete(0, END)
    txt.insert(0, hozirgi + belgi)

def hisobla(event=None):
    #Ham tugma, ham Enter uchun
    try:
        natija = eval(txt.get())
        txt.delete(0, END)
        txt.insert(0, str(natija))
    except:
        txt.delete(0, END)
        txt.insert(0, "Xato")

def klaviaturadan(event):
    if event.char.isdigit() or event.char in "+-*/%.":
        bosish(event.char)
    elif event.keysym == "Return": #Enter bosilsa
        hisobla()
    elif event.keysym == "BackSpace": #O'chirish
        txt.delete(len(txt.get())-1, END)

kalkulyator = Tk()
kalkulyator.title("Kalkulyator sinovi 1.0")
kalkulyator.geometry("395x450")

#Ekran (Entry)
txt = Entry(kalkulyator, font+("Arial", 24), borderwidth=5, relief="flat", justify="right")
txt.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

#Tugmalar ro'yxati (Matin, Qator, Ustun)
tugmalar = [
    ('9', 1, 0), ('8', 1, 1), ('7', 1, 2), ('/', 1, 3),
    ('6', 2, 0), ('5', 2, 1), ('4', 2, 2), ('*', 2, 3),
    ('3', 3, 0), ('2', 3, 1), ('1', 3, 2), ('%', 3, 3),
    ('+', 4, 0), ('0', 4, 1), ('-', 4, 2), ('=', 4, 3)
]

#Tugmalarni sikl orqali yaratish
for (matn, r, c) in tugmalar:
    rang = "yellow" if matn.isdigit() else "orange"
    fg_rang = "blue" if matn.isdigit() else "red"

    # "=" tugmasi uchun alohida buyruq, qolganlari uchun (bosish)
    cmd = hisobla if matn == "=" else lambda m=matn: bosish(m)

    btn = Button(kalkulyator, text=matn, bg=rang, fg=fg_rang, font=("Times New Romar", 20),
                 width=5, height=2, command=cmd)
    btn.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")

#Klaviaturani boglash
kalkulyator.bind("<Key>", klaviaturadan)

kalkulyator.mainloop()