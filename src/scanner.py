import argparse
from port_scanner import PortScanner

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

    def parse_args(self):
        pass
    
    
    def run(self, args):
        """
        Execute all scans specified by user
        """
        self.scan_ports()


    


    def scan_ports(self):
        scanner = PortScanner(self.ip_address)
        
        print("Scan ports")

if __name__ == '__main__':
    scanner = Scanner()
    scanner.run()
