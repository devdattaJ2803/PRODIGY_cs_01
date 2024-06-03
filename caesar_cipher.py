import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char
    return result

def encrypt_text():
    try:
        shift = int(shift_entry.get())
        text = input_text.get("1.0", tk.END).strip()
        encrypted_text = caesar_cipher(text, shift, True)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the shift value.")

def decrypt_text():
    try:
        shift = int(shift_entry.get())
        text = input_text.get("1.0", tk.END).strip()
        decrypted_text = caesar_cipher(text, shift, False)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the shift value.")

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create and place the input text widget
tk.Label(root, text="Input Text").grid(row=0, column=0, padx=10, pady=10)
input_text = tk.Text(root, height=5, width=50)
input_text.grid(row=0, column=1, padx=10, pady=10)

# Create and place the shift value widget
tk.Label(root, text="Shift Value").grid(row=1, column=0, padx=10, pady=10)
shift_entry = tk.Entry(root)
shift_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the output text widget
tk.Label(root, text="Output Text").grid(row=2, column=0, padx=10, pady=10)
output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=2, column=1, padx=10, pady=10)

# Create and place the encrypt and decrypt buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=3, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=3, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()
