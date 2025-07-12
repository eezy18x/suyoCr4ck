# suyoCr4ck 💀🔓  
_Mr. Robot–Inspired ZIP Password Cracker_

```
███████╗██╗   ██╗██╗   ██╗ ██████╗  ██████╗██████╗ ██╗  ██╗ ██████╗██╗  ██╗    
██╔════╝██║   ██║╚██╗ ██╔╝██╔═══██╗██╔════╝██╔══██╗██║  ██║██╔════╝██║ ██╔╝    
███████╗██║   ██║ ╚████╔╝ ██║   ██║██║     ██████╔╝███████║██║     █████╔╝     
╚════██║██║   ██║  ╚██╔╝  ██║   ██║██║     ██╔══██╗╚════██║██║     ██╔═██╗     
███████║╚██████╔╝   ██║   ╚██████╔╝╚██████╗██║  ██║     ██║╚██████╗██║  ██╗    
╚══════╝ ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝
```

A glitchy, GUI-based ZIP password cracker built in Python with Mr. Robot-style animations, terminal boot sequences, and a library of dark monologues.

> “You're not Elliot. You're the fsociety version of him.”  
> — _suyoCr4ck booting into your brain_

```

## 🧠 Features

- ✅ GUI built with Tkinter  
- 🔐 Cracks `.zip` files using wordlists  
- 🗣️ Text-to-speech quote generator  
- 💬 20+ Mr. Robot quotes on loop with glitch effects  
- 🎭 Terminal boot simulation + ASCII art  
- 📦 Wordlist installer script (`install.sh`) — easy setup  
- 🧪 Shows password match %, estimated time, and cancel support

```

## 📦 Installation

### 1. Clone the repository

```
git clone git@github.com:eezy18x/suyoCr4ck.git
cd suyoCr4ck
```



### 2. Install requirements

```
pip install -r requirements.txt


```

### 3. Install wordlists (automatically downloads from Mega.nz)

```
./install.sh
```

This script will:  
- Check if \`/usr/share/wordlists\` exists  
- If not, it downloads the wordlists from Mega.nz and installs them automatically

---

### 4. Run the tool

```
python3 main.py
```

---

## 🧰 Requirements

- Python 3.x  
- \`pyttsx3\`, \`tkinter\`, \`zipfile\`, \`threading\`, etc.  
- MEGA CLI: \`sudo apt install megatools\`  
- unzip, curl (usually pre-installed)

---

## 📁 Directory Structure

```
suyoCr4ck/
├── main.py
├── cracker/
│   └── zip_cracker.py
├── ui/
│   └── animations.py
├── install.sh
├── .gitignore
└── README.md
```

---

## 💬 Mr. Robot Quotes Sample

- “They see me, but they can't see me.”  
- “I'm not saying anything new, we're all living in each other's paranoia now.”  
- “You are not special. You are not the solution.”  
- “The world is a hoax, Elliot.”  
...and many more on a glitch loop.

---

## 🔐 Wordlists

Wordlists are auto-installed via \`install.sh\`, or you can manually place your own in:

\`\`\`
/usr/share/wordlists/
\`\`\`

The tool auto-detects wordlists from there.

---

## 👨‍💻 Created By

**suyog1337**  
_"Control is an illusion. But cracking it? That’s real."_

---

## ⚠️ Disclaimer

This tool is for educational and ethical use only. Do not use it against targets you do not own or have explicit permission to test.
EOF
