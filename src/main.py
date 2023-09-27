from os import popen
import psutil

RAM:str = str(psutil.virtual_memory())[6:]
BYTES_TO_GB = 1_000_000_000

class main:
    def __init__(self):
        self.SEPERATOR:str = "\033[31m\n|\033[0m "
        self.OS_SEPERATE:str = ""
        self.TOTAL_SEPERATE:str = ""
        self.PERCENT_SEPERATE:str = ""
        self.IN_USE_SEPERATE:str = ""
        self.TOP_BOTTOM:str = ""

        for i in range(max(len(os), len(total), len(percent), len(in_use))-len(os)):
            self.OS_SEPERATE += " "
        for i in range(max(len(os), len(total), len(percent), len(in_use))-len(total)):
            self.TOTAL_SEPERATE += " "
        for i in range(max(len(os), len(total), len(percent), len(in_use))-len(percent)):
            self.PERCENT_SEPERATE += " "
        for i in range(max(len(os), len(total), len(percent), len(in_use))-len(in_use)):
            self.IN_USE_SEPERATE += " "
        for i in range(max(len(os), len(total), len(percent), len(in_use))+4):
            self.TOP_BOTTOM += "-"
        self.TOP_BOTTOM += "\n"
        self.OS_SEPERATE += "\033[31m |\033[0m"
        self.TOTAL_SEPERATE += "\033[31m |\033[0m"
        self.PERCENT_SEPERATE += "\033[31m |\033[0m"
        self.IN_USE_SEPERATE += "\033[31m |\033[0m"
        self.fetch = f"\033[31m{self.TOP_BOTTOM}|\033[0m {os}{self.OS_SEPERATE}{self.SEPERATOR}{total}{self.TOTAL_SEPERATE}{self.SEPERATOR}{percent}{self.PERCENT_SEPERATE}{self.SEPERATOR}{in_use}{self.IN_USE_SEPERATE}\033[31m\n{self.TOP_BOTTOM}\033[0m"
    
    def os():
        """Get the Linux Distro of user's system"""
        global os
        os = popen('cat /etc/os-release').read().replace("NAME=", "").replace("\"", "")
        os = os[:os.index("\n")].replace("\n", "")
        return os

    def RAM_total():
        """Gets total RAM of user's system"""
        global total
        total = RAM[:RAM.index(",")].replace("total=", "")
        total = int(total)/BYTES_TO_GB
        total = round(total,2)
        total = f"RAM: Total:   {str(total)} GB"
        return total

    def RAM_percent():
        """Gets percent of RAM being used"""
        global percent
        percent = RAM[RAM.index("percent"):].replace("percent=", "")
        percent = percent[:percent.index(",")]
        percent = f"RAM: Percent: {percent}%"
        return percent
        
    def RAM_in_use():
        """Gets amount of ram that is in-use"""
        global in_use
        in_use = RAM[RAM.index("used"):].replace("used=", "")
        in_use = in_use[:in_use.index(",")]
        in_use = int(in_use)/BYTES_TO_GB
        in_use = round(in_use,2)
        in_use = f"RAM: In Use:  {str(in_use)} GB"
        return in_use

    os = os()
    total = RAM_total()
    percent = RAM_percent()
    in_use = RAM_in_use()

    def __str__(self):
        return self.fetch

if __name__ == "__main__":
    print(main())