import requests
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# API Credentials
token = "cl5skhiclpnv07ntttiunpal9i"
project_id = "67395"
model = "Pavlo_Hruznov_IRDfu-22"
headers = {"X-Auth-token": token, "Content-Type": "application/octet-stream"}

# Main Application Window
app = ttk.Window(themename="cyborg")  # Choose from: cosmo, cyborg, flatly, litera, etc.
app.title("🧠 Smart Image Detector")
app.geometry("600x700")
app.resizable(False, False)

# Frame Layout
main_frame = ttk.Frame(app, padding=20)
main_frame.pack(fill=BOTH, expand=True)

# Title Label
title_label = ttk.Label(main_frame, text="📷 Upload Image for Prediction", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

# Image Display Area
image_label = ttk.Label(main_frame)
image_label.pack(pady=10)

# Result Label
result_label = ttk.Label(main_frame, text="Prediction will appear here", font=("Helvetica", 12))
result_label.pack(pady=15)

# Upload Button Function
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("JPG Files", "*.jpg")])
    if not file_path:
        return

    # Display the image
    img = Image.open(file_path)
    img.thumbnail((500, 400))
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

    result_label.config(text="🔎 Predicting...")

    # API Request
    with open(file_path, 'rb') as handle:
        r = requests.post(f'https://platform.sentisight.ai/api/predict/{project_id}/{model}/',
                          headers=headers, data=handle)

    if r.status_code == 200:
        result_label.config(text=f"✅ Prediction: {r.text}")
    else:
        result_label.config(text=f"❌ Error {r.status_code}:\n{r.text}")

# Upload Button
upload_button = ttk.Button(main_frame, text="Upload Image", bootstyle=PRIMARY, command=upload_image)
upload_button.pack(pady=10)

# Start GUI Loop
app.mainloop()