import tkinter as tk
from tkinter import messagebox as m

# ساخت صفحه و خواندن تصاویر
app = tk.Tk()
three_line = tk.PhotoImage(file="3line.png")

# تعریف متغیرهای مورد نیاز
f_phrase = tk.StringVar(app)
first_b_phrase = ""
second_b_phrase = ""
last_Letter = ""
side = 1

# نوشتن توابع
def menu():  # تابع منو
    m.showinfo("درباره من", "نرم افزار حل معادله\nساخته شده توسط رضا زنده دل جشنواره خوارزمی")

def click(t):  # تابع دکمه ها
    global first_b_phrase, second_b_phrase, last_Letter
    last_Letter = t
    f_phrase.set(f_phrase.get() + t)
    if side == 1:
        first_b_phrase += t
    elif side == 2:
        second_b_phrase += t

def x():  # تابع دکمه x
    global first_b_phrase, second_b_phrase, last_Letter
    if last_Letter in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        f_phrase.set(f_phrase.get() + "x")
        if side == 1:
            first_b_phrase += "*x"
        elif side == 2:
            second_b_phrase += "*x"
    elif last_Letter == "+" or last_Letter == "-" or last_Letter == "=" or last_Letter == "":
        f_phrase.set(f_phrase.get() + "x")
        if side == 1:
            first_b_phrase += "x"
        elif side == 2:
            second_b_phrase += "x"
    elif last_Letter == "x":
        pass
    last_Letter = "x"

def equal():  # تابع مساوی
    global side, last_Letter
    if side == 1:
        side = 2
        f_phrase.set(f_phrase.get() + "=")
        last_Letter = "="
    elif side == 2:
        m.showerror("خطا", "طرفین معادله دوتا است.")

def do():  # تابع حل معادله
    global first_b_phrase, second_b_phrase, last_Letter, side
    x = -1000.00  # شروع از -1000
    found_solution = False
    while x <= 1000:  # پایان در 1000
        try:
            # محاسبه اختلاف دو طرف معادله
            diff = abs(eval(first_b_phrase) - eval(second_b_phrase))
            if diff < 0.0001:
                m.showinfo("!حل شد", f"x = {round(x, 2)}")  # نمایش جواب با دو رقم اعشار
                f_phrase.set("")
                first_b_phrase, second_b_phrase, last_Letter, side = "", "", "", 1
                found_solution = True
                break
            x += 0.01  # افزایش گام به اندازه 0.01
        except:
            x += 0.01  # در صورت خطا، به جلو حرکت کن
    if not found_solution:
        m.showerror("خطا", "معادله قابل حل نیست")

# هدرز و لیبل های صفحه
tk.Label(app, bg="#212121").place(relx=0, rely=0, relwidth=1, relheight=1)
tk.Label(app, bg="#0D7377").place(x=0, y=0, height=50, width=300)
tk.Button(app, bg="#0D7377", image=three_line, border=0, command=menu).place(x=10, y=10, width=30, height=30)
tk.Label(app, fg="white", text="Equation", font=("arial", (18)), bg="#0D7377").place(x=45, y=5, width=100, height=40)

# لیبل متن اصلی
tk.Label(app, bg="#212121", fg="white", textvariable=f_phrase, font=("arial", (14)), border=0).place(x=10, y=55, height=80, width=280)

# اضافه کردن دکمه ها
tk.Button(app, bg="#323232", border=0, text="1", font=("arial", (14)), fg="white", command=lambda: click("1")).place(x=2, y=150, height=58, width=72)
tk.Button(app, bg="#323232", border=0, text="2", font=("arial", (14)), fg="white", command=lambda: click("2")).place(x=76, y=150, height=58, width=72)
tk.Button(app, bg="#323232", border=0, text="3", font=("arial", (14)), fg="white", command=lambda: click("3")).place(x=150, y=150, height=58, width=72)
tk.Button(app, bg="#323232", border=0, text="4", font=("arial", (14)), fg="white", command=lambda: click("4")).place(x=2, y=210, height=58, width=72)
tk.Button(app, bg="#323232", border=0, text="5", font=("arial", (14)), fg="white", command=lambda: click("5")).place(x=76, y=210, height=58, width=72)
tk.Button(app, bg="#323232", border=0, text="6", font=("arial", (14)), fg="white", command=lambda: click("6")).place(x=150, y=210, height=58, width=72)
tk.Button(app, bg="#323232", border=0, text="7", font=("arial", (14)), fg="white", command=lambda: click("7")).place(x=2, y=270, height=58, width=72)
tk.Button(app, bg="#323232", border=0, text="8", font=("arial", (14)), fg="white", command=lambda: click("8")).place(x=76, y=270, height=58, width=72)
tk.Button(app, bg="#323232", border=0, text="9", font=("arial", (14)), fg="white", command=lambda: click("9")).place(x=150, y=270, height=58, width=72)
tk.Button(app, bg="#323232", border=0, text="0", font=("arial", (14)), fg="white", command=lambda: click("0")).place(x=2, y=330, height=58, width=146)
tk.Button(app, bg="#323232", border=0, text="=", font=("arial", (14)), fg="white", command=equal).place(x=150, y=330, height=58, width=72)
tk.Button(app, bg="#FAA300", border=0, text="Do it!", font=("arial", (12)), fg="black", command=do).place(x=2, y=390, height=58, width=220)
tk.Button(app, bg="#0D7377", border=0, text="x", font=("Segoe print", (14)), fg="white", command=x).place(x=224, y=150, height=58, width=72)
tk.Button(app, bg="#0D7377", border=0, text="+", font=("arial", (14)), fg="white", command=lambda: click("+")).place(x=224, y=210, height=118, width=72)
tk.Button(app, bg="#0D7377", border=0, text="-", font=("arial", (14)), fg="white", command=lambda: click("-")).place(x=224, y=330, height=118, width=72)
# تنظیمات و اجرای صفحه
app.minsize(298, 450)
app.title("Equation")
app.maxsize(298, 450)
app.mainloop()