import tkinter
import customtkinter as ctk
from PIL import ImageTk, Image
import qrcode

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
root_tk = ctk.CTk()
root_tk.geometry("380x500")
root_tk.title("QR Cute")

text_var=ctk.StringVar()
text = " "






def submit():
    text = text_var.get()
    print(text)
    text_var.set("")
    myqr = qrcode.make(text)
    myqr.save("myqr1.png", scale=24)
def slider_event(value):
    print(value)

img1 = ImageTk.PhotoImage(Image.open("front.png"))


def tab1():
    def tab2():
        def tab3():
            def tab4():
                def tab5():

                    button3.destroy()
                    label5.destroy()
                    label6 = ctk.CTkLabel(master=root_tk, text="Your QR code has been saved\nYou can now close the app",
                                          font=("Sans", 20), width=250, height=70, text_color=("white", "sky blue"),
                                          corner_radius=4)
                    label6.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
                button4.destroy()
                img2 = ImageTk.PhotoImage(Image.open("myqr1.png"))
                label5 = ctk.CTkLabel(master=root_tk, text=" ", width=250, height=250, image=img2)
                label5.place(relx=0.5, rely=0.34, anchor=tkinter.CENTER)
                button3 = ctk.CTkButton(master=root_tk, text="Save", corner_radius=7, command=tab5)
                button3.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)


            submit()

            button2.destroy()
            label3.destroy()
            label4.destroy()
            text_entry.destroy()
            slider1.destroy()
            button4 = ctk.CTkButton(master=root_tk, text="Generate QR Code", corner_radius=7, command=tab4)
            button4.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        button1.destroy()
        label1.destroy()
        label2.destroy()
        button2 = ctk.CTkButton(master=root_tk, text="Submit", corner_radius=7, command=tab3)
        button2.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        label3 = ctk.CTkLabel(master=root_tk, text="Enter text",
                              font=("Sans", 15), width=250, height=70, text_color=("white", "sky blue"),
                              corner_radius=4)
        label3.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        text_entry = ctk.CTkEntry(master=root_tk, textvariable=text_var, font=('calibre', 20, 'normal'),width=250,
                               height=70,
                               border_width=2)
        text_entry.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
        label4 = ctk.CTkLabel(master=root_tk, text="Enter size",
                              font=("Sans", 15), width=250, height=70, text_color=("white", "sky blue"),
                              corner_radius=4)
        label4.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
        slider1 = ctk.CTkSlider(master=root_tk, from_=8, to=24, command=slider_event)
        slider1.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

    button1 = ctk.CTkButton(master=root_tk, text="Start", corner_radius = 7, command=tab2)
    button1.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
    label1 = ctk.CTkLabel(master=root_tk,text = " ",width=250,height=250, image = img1, corner_radius=50)
    label1.place(relx=0.5, rely=0.34, anchor=tkinter.CENTER)
    label2 = ctk.CTkLabel(master=root_tk, text = "Welcome to Qt QR\nYour personal QR code generator",font = ("Sans", 20), width=250, height=70, text_color=("white", "sky blue"), corner_radius=4)
    label2.place(relx=0.5, rely=0.67, anchor=tkinter.CENTER)

tab1()
root_tk.mainloop()
