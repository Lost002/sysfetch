from os import popen
import psutil
class main:
    def __init__(self):
        self.os = popen('cat /etc/os-release').read().replace("NAME=", "").replace("\"", "")
        self.os = self.os[:self.os.index("VERSION")].replace("\n", "")
        self.ram = str(psutil.virtual_memory())[6:]
        self.total = self.ram[:self.ram.index(",")].replace("total=", "")
        self.total = int(self.total)/1_000_000_000
        self.total = round(self.total)
        self.percent = self.ram[self.ram.index("percent"):].replace("percent=", "")
        self.percent = self.percent[:self.percent.index(",")]
        self.ram = "RAM: Total= " + str(self.total) + " GB - Percent: " + self.percent

        self.fetch = self.os + " | "+ self.ram
    def __str__(self):
        return self.fetch
print(main())