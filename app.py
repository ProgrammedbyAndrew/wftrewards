import tkinter as tk
import qrcode
from PIL import Image, ImageTk
import io

# Function to generate QR code from the entered amount
def generate_qr(amount):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,  # Removing border
    )
    qr.add_data(amount)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Function to handle the enter button click
def on_enter():
    dollars = entry_dollars.get()
    cents = entry_cents.get()
    amount = f"{dollars}.{cents}"
    qr_img = generate_qr(amount)
    with io.BytesIO() as output:
        qr_img.save(output, format="PNG")
        qr_png = output.getvalue()
    qr_photo = ImageTk.PhotoImage(image=Image.open(io.BytesIO(qr_png)))
    label.config(image=qr_photo)
    label.image = qr_photo  # Keep a reference!

# Create the main window
root = tk.Tk()
root.title("World Food Trucks Reward Points Redemption")

# Americana theme: red background with white letters
root.configure(bg='red')

# Add a heading label for "World Food Trucks"
world_food_trucks_label = tk.Label(root, text="World Food Trucks", font=('Arial', 28, 'bold'), bg='red', fg='white')
world_food_trucks_label.pack(pady=5)

# Add a sub-heading label for "Reward Points Redemption"
heading_label = tk.Label(root, text="Reward Points Redemption", font=('Arial', 20), bg='red', fg='white')
heading_label.pack(pady=5)

# Create labels and entry widget for dollars
label_dollars = tk.Label(root, text="Dollars", font=('Arial', 16), bg='red', fg='white')
label_dollars.pack(pady=5)
entry_dollars = tk.Entry(root, font=('Arial', 20), width=7)
entry_dollars.pack(pady=5)

# Create labels and entry widget for cents
label_cents = tk.Label(root, text="Cents", font=('Arial', 16), bg='red', fg='white')
label_cents.pack(pady=5)
entry_cents = tk.Entry(root, font=('Arial', 20), width=7)
entry_cents.pack(pady=5)

# Create enter button
button = tk.Button(root, text="Generate QR Rewards Code", font=('Arial', 18, 'bold'), command=on_enter, bg='white', fg='red')
button.pack(pady=10)

# Label to display QR code
label = tk.Label(root)
label.pack(pady=20)

root.mainloop()
