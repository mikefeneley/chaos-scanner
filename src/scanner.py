import argparse

class Scanner:
    """
    Main class of the chaos-scanner program.

    Reads in command line arguments from the user.
    Executes various scans and vulnerability tests on the target system.

    Usage:
        scanner.py -a ip_address   : Executes all supported scans and test on
                                     server 
        scanner.py -p ip_address   : Execute port scan on server
        
    """


    def __init__(self, ip_address='127.0.0.1'):
        self.ip_address = ip_address
        print("Scanner init")

    def run(self):
        print("Run")

    def scan_ports(self):
        print("Scan ports")

if __name__ == '__main__':
    scanner = Scanner()
    scanner.run()
