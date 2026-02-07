############################See Disclaimer.txt for legal and ethical usage guidelines.##########################################

#!/usr/bin/python3

import sys
import socket
import time
import threading

print("-"*235)
"""x = "WELCOME TO PORT SCANNER"
print(x.center(235, '-'))"""
y= """                          
 __          __  _                            _______      _____           _      _____                                 
 \ \        / / | |                          |__   __|    |  __ \         | |    / ____|                                
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___   | |__) |__  _ __| |_  | (___   ___ __ _ _ __  _ __   ___ _ __ 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \  |  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
    \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) | | |  | (_) | |  | |_   ____) | (_| (_| | | | | | | |  __/ |   
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/  |_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                                                                                        
"""
#print(y.center(235, '-'))
print(y)

d= "Desclaimer"
#print("#"*235)

print(d.center(235, '#'))

print("This is an Ethical Hacking Tool designed strictly for educational purposes. It is intended for use by cybersecurity professionals, network administrators, or students learning about network security.The tool is meant to help users understand network vulnerabilities and improve their security posture. Legal Use Only: This tool should only be used on systems forwhich you have explicit permission. Unauthorized scanning of networks you do not own or have consent to scan is illegal and unethical.No Malicious Intent: The tool should not be used to exploit or harm any network or system. It is created to enhance knowledge and understanding of network security, not to compromise or disrupt services.Educational Resource: This tool is an educational resource. Users should ensure they understand the legal implications and responsibilities associated with its use.Limited Warranty: The developers of this tool are not responsible for any misuse or damage that may result from its application. Users assume all responsibility for their actions when using this.")


usage = "python3 Scanner.py TARGET START_PORT END_PORT"
print("-"*235)

print("Result For The Entered IP address & Port Ranges")
#print("PORT_SCANNER")
start_time = time.time()


if(len(sys.argv)!=4):
    print(usage)
    sys.exit()


try: 
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:        
    print("Name Resolution Error")
    sys.exit()
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
print("scanning target", target)


def scan_port(port):

    print("Scanning The Port :" , port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    conn = s.connect_ex((target, port))
    if(not conn):
        print("Port" ,format(port),"IS OPEN" ) 
    s.close() 
     
for port in range (start_port , end_port+1):    
    
    thread = threading.Thread(target = scan_port, args = (port,))
    thread.start()
    

end_time = time.time()
print("Time elapsed:", end_time - start_time )    

