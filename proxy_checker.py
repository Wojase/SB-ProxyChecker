import threading
import socket
import requests
import time
import sys
from queue import Queue
from colorama import Fore, Style, init

# Inicjalizacja colorama (Windows fix)
init()

print(Fore.CYAN + "\n🌐 SBProxy Checker - MultiThreaded 🌐\n" + Style.RESET_ALL)

# Wybór typu proxy
types = {"1": "http", "2": "socks4", "3": "socks5"}
proxy_type = input("🔹 Select proxy type: [1] HTTP, [2] SOCKS4, [3] SOCKS5: ")
while proxy_type not in types:
    proxy_type = input(Fore.RED + "⛔ Wrong choice! Select 1, 2 or 3: " + Style.RESET_ALL)
proxy_type = types[proxy_type]

# Wybór pliku
file_path = input("📂 Provide the path to the proxy file (ip:port in each line): ")

try:
    with open(file_path, "r") as f:
        proxies = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    print(Fore.RED + "⛔ The file does not exist!" + Style.RESET_ALL)
    sys.exit()

# Konfiguracja multi-threadingu
q = Queue()
working_proxies = []
lock = threading.Lock()

def check_proxy(proxy):
    """Sprawdza proxy i zapisuje działające"""
    try:
        proxy_dict = {proxy_type: f"{proxy_type}://{proxy}"}
        start = time.time()
        response = requests.get("http://www.google.com", proxies=proxy_dict, timeout=5)
        elapsed = time.time() - start
        if response.status_code == 200:
            with lock:
                working_proxies.append(proxy)
                print(Fore.GREEN + f"✅ {proxy} works! ({elapsed:.2f}s)" + Style.RESET_ALL)
    except (requests.RequestException, socket.error):
        print(Fore.RED + f"❌ {proxy} doesn't work!" + Style.RESET_ALL)

def worker():
    """Obsługuje kolejkę proxy"""
    while not q.empty():
        proxy = q.get()
        check_proxy(proxy)
        q.task_done()

# Wypełnianie kolejki
for proxy in proxies:
    q.put(proxy)

print(Fore.YELLOW + f"🔎 Checking {len(proxies)} proxy..." + Style.RESET_ALL)
threads = []
for _ in range(20):  # Liczba wątków
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Zapisywanie działających proxy
timestamp = time.strftime("%Y%m%d_%H%M%S")
output_file = f"proxy_checked_{proxy_type}_{timestamp}.txt"
with open(output_file, "w") as f:
    f.write("\n".join(working_proxies))

print(Fore.BLUE + f"\n📁 Saved working proxy to: {output_file}" + Style.RESET_ALL)
