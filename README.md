

# Python Port Scanner

Overview  
This project is a simple Python-based port scanner developed and tested on a Linux operating system running inside VirtualBox.  
It is designed for educational and ethical security testing purposes to understand how open ports and network services can be identified.

The scanner checks a target host for open TCP ports and reports their status.

---

Purpose of the Project  
The goal of this project is to:
- Learn how network port scanning works
- Understand basic networking and socket programming
- Practice ethical penetration testing concepts
- Improve defensive security awareness

This project is intended strictly for learning and research.

---

Features
- Scans a target IP address or hostname
- Detects open and closed TCP ports
- Written in Python using standard libraries
- Runs on Linux systems
- Lightweight and easy to understand

---



---

Requirements
- Linux operating system (tested on Linux VM in VirtualBox)
- Python 3.x

No external libraries are required.

---

How to Run the Port Scanner

1. Open a terminal in Linux
2. Navigate to the project directory:
```bash
cd PortScanner
````

3. Run the script:

```bash
python3 port_scanner.py
```

4. Enter the target IP address and port range when prompted.

---

Example Usage

```bash
python3 port_scanner.py
```

The scanner will display which ports are open or closed on the target host.

---

Ethical Usage Policy

This port scanner is created for **ethical and legal purposes only**.

You are allowed to use this tool only on:

* Your own systems
* Systems you own
* Systems you have explicit permission to test

You are NOT allowed to:

* Scan public servers without authorization
* Scan networks you do not own
* Use this tool for malicious activities
* Violate any laws or organizational policies

Unauthorized port scanning may be illegal and punishable by law.

---

# Legal Disclaimer

The author of this project is not responsible for any misuse of this software.
Any actions performed using this tool are solely the responsibility of the user.

This project is provided for educational purposes only.

---

Learning Outcomes

* Understanding TCP/IP networking basics
* Learning Python socket programming
* Awareness of network security risks
* Introduction to ethical hacking concepts





License
MIT License

#########################################################################################################################################################################################

# How to run in Linux?

Great question 👍
Here is the **exact, beginner‑friendly way** someone can run **your port scanner on Linux** (this works on Ubuntu, Kali, Debian, etc.).

You can also copy this into your README if you want.

---

## How to Run the Port Scanner on Linux

### 1️⃣ Open a Terminal

On Linux, press:

* `Ctrl + Alt + T`

---

### 2️⃣ Install Python (if not installed)

Check:

```bash
python3 --version
```

If not installed:

```bash
sudo apt update
sudo apt install python3
```

---

### 3️⃣ Download or Clone the Project

If using GitHub:

```bash
git clone https://github.com/<your-username>/PortScanner.git
cd PortScanner
```

Or if downloaded as ZIP:

```bash
cd Downloads
unzip PortScanner.zip
cd PortScanner
```

---

### 4️⃣ (Optional) Make the Script Executable

Because your script has:

```bash
#!/usr/bin/python3
```

Run:

```bash
chmod +x Scanner.py
```

Now you can run it directly.

---

### 5️⃣ Run the Port Scanner

#### Method 1 (recommended)

```bash
python3 Scanner.py <TARGET_IP> <START_PORT> <END_PORT>
```

Example:

```bash
python3 Scanner.py 127.0.0.1 20 100
```

#### Method 2 (executable)

```bash
./Scanner.py 127.0.0.1 20 100
```

---

### 6️⃣ Expected Output

* Banner and disclaimer
* Each scanned port displayed
* Open ports clearly shown
* Total scan time printed at the end

---

## Important Ethical Rules (MUST READ)

You may scan ONLY:

* Your own machine
* Your own VM
* Systems you have written permission to test

You must NOT scan:

* Public servers
* College / office networks
* Any system without authorization

Unauthorized scanning is illegal.

---

## Common Errors & Fixes

### Permission denied

```bash
chmod +x Scanner.py
```

### Python not found

```bash
sudo apt install python3
```

### Invalid arguments

You must pass exactly 3 arguments:

```bash
python3 Scanner.py TARGET START_PORT END_PORT
```

---

## Example Safe Test (Recommended)

Scan your own VM:

```bash
python3 Scanner.py 127.0.0.1 1 1024

