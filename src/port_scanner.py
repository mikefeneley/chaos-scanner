from port_scan_logger import PortScanLogger

class PortScanner:
    def __init__(self, ip_address='127.0.0.1'):
        self.ip_address = ip_address

    def scan(self):
        """
        Scan target server for open ports and report findings to user in text
        document.
        """
        pass

if __name__ == '__main__':
    scanner = PortScanner()
    scanner.scan()
