from os import popen
import psutil
class main:
    def __init__(self):
        self.os = popen('cat /etc/os-release').read().replace("NAME=", "").replace("\"", "")
        self.os = self.os[:self.os.index("VERSION")].replace("\n", "")
        self.ram = str(psutil.virtual_memory())[6:]
        self.total = self.ram[:self.ram.index(",")].replace("total=", "")
        self.total = int(self.total)/1_000_000_000
        self.total = round(self.total,1)
        self.percent = self.ram[self.ram.index("percent"):].replace("percent=", "")
        self.percent = self.percent[:self.percent.index(",")]
        self.in_use = self.ram[self.ram.index("used"):].replace("used=", "")
        self.in_use = self.in_use[:self.in_use.index(",")]
        self.in_use = int(self.in_use)/1_000_000_000
        self.in_use = round(self.in_use,1)
        self.ram = "RAM: Total: " + str(self.total) + " GB - Percent: " + self.percent + "% - Used: " + str(self.in_use) + "GB"

        self.fetch = "Distro: " + self.os + " | "+ self.ram + "\n\n" + str(psutil.virtual_memory())
    def __str__(self):
        return self.fetch
print(main())