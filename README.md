<h1>#️ Hasher #️</h1>
Small python script to hash a password

<h2>⚙️ Dependencies ⚙️</h2>

- Python3

Optional:
- <a href="https://pypi.org/project/pyperclip/">Pyperclip</a> (for copy to clipboard functionality)
- Any copy/paste mechanism (like xclip, xselect, wl-clipboard) in the OS (for copy to clipboard functionality)

<h2>🛠️ Usage 🛠️</h2>

1. **Clone the repository:**
   ```bash
   git clone https://github.com/neomikus/42-Webserv.git
   cd 42-Webserv
   ```

2. **Execute the script:**
   ```bash
   python3 main.py [--algorithm/-a] [--clipboard/-c]
   ```

Where algorithm can be any algorithm supported by the hashlib library (case indifferent). If not set, defaults to sha256

If the clipboard flag is set, the program will copy the resulting hashed password into your clipboard (pyperclip needed, see dependencies)
