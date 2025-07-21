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

# --- Boot Screen ---
def fake_boot_screen():
    lines = [
        "[ OK ] Initializing suyoCr4ck system...",
        "[ OK ] Loading fsociety modules...",
        "[ OK ] Connecting to darknet...",
        "[ OK ] Initial handshake completed...",
    ]
    os.system("clear" if os.name == "posix" else "cls")
    for line in lines:
        print(line)
        time.sleep(random.uniform(0.2, 0.4))
    os.system("clear" if os.name == "posix" else "cls")

# --- ASCII Art ---
def read_ascii_art():
    try:
        with open("assets/ascii_art.txt") as f:
            return f.read()
    except:
        return "=== suyoCr4ck ==="

# --- Quotes / Dialogues ---
def get_random_quote():
    try:
        with open("assets/quotes.txt") as f:
            return random.choice(f.readlines()).strip()
    except:
        return "Hack the planet."

def loop_quotes(label, delay=7):
    def updater():
        while True:
            quote = get_random_quote()
            type_writer(label, quote)
            speak_quote(quote)
            time.sleep(delay)
    Thread(target=updater, daemon=True).start()

# --- Glitch Effect ---
def glitch_char(char):
    glitch_pool = ['@', '#', '%', '&', '*', '?', '1', '$']
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

# --- TTS ---
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

# --- Cracking Logic ---
def crack_thread(zip_path, wordlist_path, progress_var, status_label, result_label):
    def update(percent, current_pass, eta):
        progress_var.set(percent)
        status_label.config(text=f"Trying: {current_pass} | ETA: {int(eta)}s")

    def stop_check():
        return stop_cracking

    success, message = crack_zip(zip_path, wordlist_path, update, stop_check)
    result_label.config(text=message)

# --- Start Cracking ---
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

# --- GUI ---
def gui():
    root = tk.Tk()
    root.title("suyoCr4ck - ZIP Cracker")
    root.configure(bg="black")
    root.geometry("820x580")

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TProgressbar", foreground='green', background='lime')

    # ASCII
    ascii_label = tk.Label(root, text=read_ascii_art(), fg="red", bg="black", font=("Courier New", 11), justify="left")
    ascii_label.pack()

    # QUOTES
    quote_label = tk.Label(root, text="", fg="#00ff00", bg="black", font=("Courier New", 10))
    quote_label.pack(pady=5)
    loop_quotes(quote_label)

    frame = tk.Frame(root, bg="black")
    frame.pack(pady=10)

    zip_entry = tk.Entry(frame, width=50, font=("Courier", 10))
    zip_entry.grid(row=0, column=1, padx=10)
    tk.Label(frame, text="ZIP File:", fg="white", bg="black").grid(row=0, column=0)
    tk.Button(frame, text="Browse", command=lambda: browse_file(zip_entry), bg="#1f1", fg="black").grid(row=0, column=2, padx=5)

    # Wordlist menu
    tk.Label(frame, text="Wordlist:", fg="white", bg="black").grid(row=1, column=0, pady=5)
    wordlist_files = os.listdir("wordlists/")
    wordlist_var = tk.StringVar()
    wordlist_var.set(wordlist_files[0])
    wordlist_menu = tk.OptionMenu(frame, wordlist_var, *wordlist_files)
    wordlist_menu.config(bg="black", fg="lime", font=("Courier", 10))
    wordlist_menu.grid(row=1, column=1, columnspan=2)

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, length=500, variable=progress_var)
    progress_bar.pack(pady=8)

    status_label = tk.Label(root, text="Waiting to start...", fg="white", bg="black", font=("Courier", 10))
    status_label.pack()

    result_label = tk.Label(root, text="", fg="cyan", bg="black", font=("Courier", 11, "bold"))
    result_label.pack(pady=5)

    btn_frame = tk.Frame(root, bg="black")
    btn_frame.pack(pady=10)

    start_btn = tk.Button(btn_frame, text="Start", width=10, bg="#0f0", fg="black",
                          command=lambda: start_crack(zip_entry, wordlist_var, progress_var, status_label, result_label))
    start_btn.grid(row=0, column=0, padx=10)

    cancel_btn = tk.Button(btn_frame, text="Cancel", width=10, bg="red", fg="white", command=cancel_crack)
    cancel_btn.grid(row=0, column=1, padx=10)

    # Glow Effect
    def animate():
        colors = ['#0f0', '#1f1', '#2f2', '#3f3']
        i = 0
        while True:
            current = colors[i % len(colors)]
            start_btn.config(bg=current)
            root.update_idletasks()
            time.sleep(0.2)
            i += 1
    Thread(target=animate, daemon=True).start()

    root.mainloop()

if __name__ == "__main__":
    fake_boot_screen()
    gui()
