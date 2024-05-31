import pyautogui
import tkinter as tk
from tkinter import Toplevel
import threading
import time

# Setze eine minimale Pause für eine noch hohe, aber kontrollierbare Klickgeschwindigkeit
pyautogui.PAUSE = 0.01

def auto_clicker(num_clicks, progress_label=None):
    """
    Einfacher Autoklicker, der 'num_clicks' mal klickt mit einer kleinen Pause von 0.01 Sekunden zwischen den Klicks.
    Aktualisiert das übergebene Label mit der Anzahl der ausgeführten Klicks.
    """
    for i in range(num_clicks):
        pyautogui.click()
        if progress_label:
            progress_label.config(text=f"Klicks ausgeführt: {i + 1}")
        time.sleep(pyautogui.PAUSE)
    if progress_label:
        progress_label.config(text="Autoklicker hat die geforderte Anzahl an Klicks ausgeführt.")

def start_clicking():
    """
    Liest die Anzahl der Klicks aus dem Eingabefeld, öffnet ein neues Fenster für den Fortschritt und startet den Autoklicker in einem neuen Thread.
    """
    num_clicks = int(clicks_entry.get())
    progress_window = Toplevel(root)
    progress_window.title("Autoklicker läuft")
    progress_label = tk.Label(progress_window, text="Klicks ausgeführt: 0")
    progress_label.pack(pady=20)
    center_window(progress_window, 300, 100)

    # Starte den Klickprozess in einem separaten Thread
    thread = threading.Thread(target=auto_clicker, args=(num_clicks, progress_label))
    thread.start()

def center_window(window, width=300, height=100):
    """
    Zentriert das Fenster auf dem Bildschirm.
    """
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Autoklicker")
center_window(root, 300, 120)

# Eingabefeld für die Anzahl der Klicks
clicks_label = tk.Label(root, text="Anzahl der Klicks:")
clicks_label.pack(pady=10)

clicks_entry = tk.Entry(root, font=('Helvetica', 12), width=15)
clicks_entry.pack()

# Startknopf
start_button = tk.Button(root, text="Start Klicken", command=start_clicking, height=2, width=15)
start_button.pack(pady=10)

# Starte das Tkinter event loop
root.mainloop()
