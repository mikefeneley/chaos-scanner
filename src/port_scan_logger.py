
class PortScanLogger:
    """
    Logging class reports open ports to user.
    """
    def __init__(self, filename="PortScanLog.txt"):
        self.filename = filename
        self.log = open(filename, 'w')
        self.log.write("##########################################\n\n")
        self.log.write("Port Scan Results\n\n")

    def __del__(self):
        self.log.write("##########################################\n\n")
        self.log.close()

    def report_close_port(self, port):
        self.log.write("Port " + port + "closed.\n")

    def report_open_port(self, port):
        self.log.write("Port " + port + "open.\n")
