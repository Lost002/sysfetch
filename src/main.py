from os import popen
import psutil
class main:
    def __init__(self):
        self.os = popen('cat /etc/os-release').read().replace("NAME=", "").replace("\"", "")
        self.os = self.os[:self.os.index("VERSION")].replace("\n", "")
        self.ram = str(psutil.virtual_memory())[6:]
        self.ram = self.ram[:self.ram.index(",")].replace("total=", "")
        self.ram = int(self.ram)/1_000_000_000
        self.ram = round(self.ram)
        self.ram = "RAM: total= " + str(self.ram) + " GB"

        self.fetch = self.os+" | "+self.ram
    def __str__(self):
        return self.fetch
print(main())