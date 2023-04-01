from tkinter import *

root = Tk()
root.title('Konversi Bilangan jy')


# Set window size to 800x600 pixels
root.geometry("450x450")

# Disable maximize button
root.resizable(False, False)


def convert():
    if var.get() == 1:
        angka = int(entry.get())
        bineri = bin(angka).replace("0b","")
        oktal = oct(angka).replace("0o","")
        heks = hex(angka).replace("0x","")
        hasil.config(text=f'Biner : {bineri}\nOktal : {oktal}\nHexa  : {heks}')
        
    elif var.get() == 2:
        angka = int(entry.get(), 2)
        oktal = oct(angka).replace("0o","")
        heks = hex(angka).replace("0x","")
        hasil.config(text=f'Decimal : {angka}\nOktal   : {oktal}\nHexa    : {heks}')
        
    elif var.get() == 3:
        angka = int(entry.get(), 8)
        biner = bin(angka).replace("0b","")
        heks = hex(angka).replace("0x","")
        hasil.config(text=f'Decimal : {angka}\nBiner   : {biner}\nHexa    : {heks}')
        
    elif var.get() == 4:
        angka = int(entry.get(), 16)
        biner = bin(angka).replace("0b","")
        oktal = oct(angka).replace("0o","")
        hasil.config(text=f'Decimal : {angka}\nBiner   : {biner}\nOktal   : {oktal}')
        
    elif var.get() == 5:
        text = entry.get()
        ascii_values = [ord(character) for character in text]
        hasil.config(text=f'Ascii : {ascii_values}')

def clear():
    entry.delete(0, END)
    hasil.config(text='')

def exit_app():
    root.destroy()

# Create widgets
judul = Label(root, text='Konversi Bilangan jy', font='Helvetica 16 bold')
judul.pack(pady=10)

var = IntVar()
Radiobutton(root, text='Desimal', variable=var, value=1).pack()
Radiobutton(root, text='Biner', variable=var, value=2).pack()
Radiobutton(root, text='Oktal', variable=var, value=3).pack()
Radiobutton(root, text='Hexadecimal', variable=var, value=4).pack()
Radiobutton(root, text='ASCII', variable=var, value=5).pack()

label = Label(root, text='Masukkan Bilangan/Text :')
label.pack(pady=5)

entry = Entry(root)
entry.pack(pady=5)

convert_btn = Button(root, text='Konversi', command=convert)
convert_btn.pack(pady=5)

clear_btn = Button(root, text='Clear', command=clear)
clear_btn.pack(pady=5)

hasil = Label(root, text='', font='Helvetica 12')
hasil.pack(pady=10)

exit_btn = Button(root, text='Keluar', command=exit_app)
exit_btn.pack(pady=10)

root.mainloop()


