# 🌐 SB-ProxyChecker

SB-ProxyChecker is a lightweight and efficient program designed to verify the status and functionality of proxies from a provided list. Whether you want to check HTTP, SOCKS4, or SOCKS5 proxies, this tool helps ensure their validity. This project is for **educational purposes only** and should not be used for malicious activities. 

---

## ⚡ Features
- 📝 **Bulk Proxy Testing**: Validate large proxy lists with ease.
- ✅ **Check Proxy Functionality**: Verify whether proxies are active or inactive.
- ⚙️ **Customizable**: Supports various proxy types (HTTP, SOCKS4, SOCKS5).
- 📂 **Output Results**: Saves valid and invalid proxies for further use.
- 🔒 **Privacy-Focused**: No data tracking or logging.

---

## 🚀 Installation

1. Clone the repository or download the proxychecker.py file from the github page:
   ```bash
   git clone https://github.com/YourUsername/SB-ProxyChecker.git
   cd SB-ProxyChecker
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python proxy_checker.py
   ```

---

## 🛠️ Usage

1. Prepare a text file (`proxies.txt`) with a list of proxies, one per line:
   ```
   192.168.0.1:8080
   203.0.113.2:3128
   198.51.100.3:1080
   ```

2. Execute the script and provide the proxy list file as input:
   ```bash
   python proxy_checker.py
   ```
   Then select proxy option beetwen: http, socks4, socks5 and put
   the file where you have your proxies

4. View the results:
   - **valid_proxies.txt**: Contains all working proxies.
   - **invalid_proxies.txt**: Contains all non-working proxies.

---

## 📖 Example

```bash
$ python proxy_checker.py
🔹 Select proxy type: [1] HTTP, [2] SOCKS4, [3] SOCKS5:
"1"
📂 Provide the path to the proxy file (ip:port in each line):
"C:\Users\user\Videos\proxies.txt"

[INFO] Starting HTTP proxy check...
[✔️] 192.168.0.1:8080 is working!
[❌] 203.0.113.2:3128 is not working.
[✔️] 198.51.100.3:1080 is working!

[INFO] Process completed. Results saved to valid_proxies.txt and invalid_proxies.txt.
```

---

## ⚠️ Disclaimer
This tool is intended for **educational purposes only**. The author is not responsible for any misuse of this tool. Always ensure you have proper authorization when using proxies.

---

## 📦 Dependencies
- Python 3.8+
- Requests library
- colorama
- Any other dependencies specified in `requirements.txt`

---

## ✨ Contributing
Contributions are welcome! If you'd like to contribute, please:

1. Fork the repository
2. Create a new branch (`feature/YourFeatureName`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 🌟 Support
If you find this project useful, please consider giving it a ⭐ on GitHub. Your support is greatly appreciated!

---

### Made with ❤️ by Wojas
