import zipfile
import time

def crack_zip(zip_path, wordlist_path, update_callback, stop_flag):
    with zipfile.ZipFile(zip_path) as zf:
        passwords = open(wordlist_path, 'r', errors='ignore').readlines()
        total = len(passwords)
        start_time = time.time()

        for i, password in enumerate(passwords):
            if stop_flag():
                return False, "Cracking canceled."
            password = password.strip()
            try:
                zf.extractall(pwd=bytes(password, 'utf-8'))
                duration = time.time() - start_time
                return True, f"Password found: {password} in {duration:.2f}s"
            except:
                percent = (i + 1) / total * 100
                eta = (time.time() - start_time) / (i+1) * (total - (i+1))
                update_callback(percent, password, eta)

        return False, "Password not found in wordlist."
