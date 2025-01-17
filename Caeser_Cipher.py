from tkinter import *

window = Tk()
window.config(padx=100, pady=200)
def islower(c):
    if 97 <= ord(c) <= 122:
        return True
    else:
        return False


def isupper(c):
    if 65 <= ord(c) <= 90:
        return True
    else:
        return False

def encrypt():
    result = ""
    st = accept_string.get()
    shift = int(accept_shift.get())

    for char in st:
        if islower(char):
            result = result + chr(((ord(char) + shift - 97) % 26) + 97)
        elif isupper(char):
            result = result + chr(((ord(char) + shift - 65) % 26) + 65)
        else:
            result = result + char

    output["text"] = f"\nCipher Text: {result}"

window.title("Caesar Cipher")
window.minsize(800, 500)

#heading
heading = Label(text="Enter the text to encode", font=("poppins", 16, ""), padx=20, pady=20)
heading.pack()

#text input
accept_string = Entry(width=40)
accept_string.pack()

#shift value input
heading2 = Label(text="Enter the shift amount", font=("poppins", 16, ""), padx=20, pady=20)
heading2.pack()

accept_shift = Spinbox(from_=0, to=100, width=20)
accept_shift.pack()

label1 = Label(text="\n")
label1.pack()

cipher = Button(text="Cipher", height=2, width=20, command = encrypt, padx=5, pady=5)
cipher.pack()

#output label
output = Label(text="", font=("poppins", 16, ""), padx=20, pady=20)
output.pack()

window.mainloop()
