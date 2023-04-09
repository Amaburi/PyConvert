from tkinter import *

root = Tk()
root.title('Konversi Bilangan jy')


# Set window size to 800x600 pixels
root.geometry("450x500")

# Disable maximize button
root.resizable(False, False)


def convert():
    if var.get() == 1:
        angka = int(entry.get())
        angka_str = str(angka)
        bineri = bin(angka).replace("0b","")
        oktal = oct(angka).replace("0o","")
        heks = hex(angka).replace("0x","")
        ascii_values = [ord(character) for character in angka_str]
        hasil.config(text=f'Biner : {bineri}\nOktal : {oktal}\nHexa  : {heks}\nAscii  : {ascii_values}')
        
    elif var.get() == 2:
        angka = int(entry.get(), 2)
        angka_str = str(angka)
        oktal = oct(angka).replace("0o","")
        heks = hex(angka).replace("0x","")
        ascii_values = [ord(character) for character in angka_str]
        hasil.config(text=f'Decimal : {angka}\nOktal   : {oktal}\nHexa    : {heks}\nAscii  : {ascii_values}')
        
    elif var.get() == 3:
        angka = int(entry.get(), 8)
        angka_str = str(angka)
        biner = bin(angka).replace("0b","")
        heks = hex(angka).replace("0x","")
        ascii_values = [ord(character) for character in angka_str]
        hasil.config(text=f'Decimal : {angka}\nBiner   : {biner}\nHexa    : {heks}\nAscii  : {ascii_values}')
        
    elif var.get() == 4:
        angka = int(entry.get(), 16)
        angka_str = str(angka)
        biner = bin(angka).replace("0b","")
        oktal = oct(angka).replace("0o","")
        ascii_values = [ord(character) for character in angka_str]
        hasil.config(text=f'Decimal : {angka}\nBiner   : {biner}\nOktal   : {oktal}\nAscii  : {ascii_values}')
        
    elif var.get() == 5:
        text = entry.get()
        decimal_values = [ord(character) for character in text]
        decimal = int(''.join(map(str, decimal_values)))
        
        biner = bin(decimal).replace("0b", "")
        oktal = oct(decimal).replace("0o", "")
        heks = hex(decimal).replace("0x", "").upper()
        hasil.config(text=f'Decimal : {decimal}\nBiner   : {biner}\nOktal   : {oktal}\nHexa    : {heks}\nASCII  : {decimal_values}')






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


