import tkinter as tk
from tkinter import ttk
from threading import Thread
import time, os, random
from cracker.zip_cracker import crack_zip

try:
    import pyttsx3
    tts_available = True
except ImportError:
    tts_available = False

stop_cracking = False

def fake_boot_screen():
    lines = [
        "[ OK ] Starting suyoCr4ck services...",
        "[ OK ] Mounting fsociety modules...",
        "[ OK ] Launching terminal interface...",
    ]
    os.system("clear" if os.name == "posix" else "cls")
    for line in lines:
        print(line)
        time.sleep(random.uniform(0.1, 0.3))
    os.system("clear" if os.name == "posix" else "cls")

def read_ascii_art():
    try:
        with open("assets/ascii_art.txt") as f:
            return f.read()
    except:
        return "=== suyoCr4ck ==="

def get_random_quote():
    try:
        with open("assets/quotes.txt") as f:
            return random.choice(f.readlines()).strip()
    except:
        return "Hack the planet."

def glitch_char(char):
    glitch_pool = ['@', '#', '%', '&', '*', '?', '1']
    return random.choice(glitch_pool) if random.random() < 0.15 else char

def type_writer(label, text, delay=40):
    def inner():
        label.config(text="")
        for char in text:
            label.config(text=label.cget("text") + glitch_char(char))
            label.update()
            time.sleep(delay / 1000)
        label.config(text=text)
    Thread(target=inner, daemon=True).start()

if tts_available:
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.setProperty('volume', 0.8)

    def speak_quote(quote):
        def speak():
            engine.say(quote)
            engine.runAndWait()
        Thread(target=speak, daemon=True).start()
else:
    def speak_quote(quote):
        pass

def crack_thread(zip_path, wordlist_path, progress_var, status_label, result_label):
    def update(percent, current_pass, eta):
        progress_var.set(percent)
        status_label.config(text=f"Trying: {current_pass} | ETA: {int(eta)}s")

    def stop_check():
        return stop_cracking

    success, message = crack_zip(zip_path, wordlist_path, update, stop_check)
    result_label.config(text=message)

def start_crack(zip_entry, wordlist_var, progress_var, status_label, result_label):
    global stop_cracking
    stop_cracking = False
    path = os.path.join("wordlists", wordlist_var.get())
    Thread(target=crack_thread, args=(zip_entry.get(), path, progress_var, status_label, result_label)).start()

def cancel_crack():
    global stop_cracking
    stop_cracking = True

def browse_file(entry):
    from tkinter import filedialog
    path = filedialog.askopenfilename()
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)

def gui():
    root = tk.Tk()
    root.title("suyoCr4ck - ZIP Cracker")
    root.configure(bg="black")
    root.geometry("800x520")

    ascii_label = tk.Label(root, text=read_ascii_art(), fg="red", bg="black", font=("Courier", 10), justify="left")
    ascii_label.pack()

    quote_label = tk.Label(root, text="", fg="green", bg="black", font=("Courier", 10))
    quote_label.pack()
    quote = get_random_quote()
    type_writer(quote_label, quote)
    speak_quote(quote)

    frame = tk.Frame(root, bg="black")
    frame.pack(pady=10)

    zip_entry = tk.Entry(frame, width=50)
    zip_entry.grid(row=0, column=1)
    tk.Label(frame, text="ZIP File:", fg="white", bg="black").grid(row=0, column=0)
    tk.Button(frame, text="Browse", command=lambda: browse_file(zip_entry)).grid(row=0, column=2)

    # Dropdown for wordlists
    tk.Label(frame, text="Wordlist:", fg="white", bg="black").grid(row=1, column=0)
    wordlist_files = os.listdir("wordlists/")
    wordlist_var = tk.StringVar()
    wordlist_var.set(wordlist_files[0])
    wordlist_menu = tk.OptionMenu(frame, wordlist_var, *wordlist_files)
    wordlist_menu.config(bg="black", fg="lime", font=("Courier", 10))
    wordlist_menu.grid(row=1, column=1, columnspan=2)

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, length=400, variable=progress_var)
    progress_bar.pack(pady=5)

    status_label = tk.Label(root, text="Waiting to start...", fg="white", bg="black")
    status_label.pack()

    result_label = tk.Label(root, text="", fg="cyan", bg="black", font=("Courier", 10))
    result_label.pack()

    btn_frame = tk.Frame(root, bg="black")
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Start", command=lambda: start_crack(zip_entry, wordlist_var, progress_var, status_label, result_label), bg="green").grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="Cancel", command=cancel_crack, bg="red").grid(row=0, column=1, padx=10)

    root.mainloop()

if __name__ == "__main__":
    fake_boot_screen()
    gui()
