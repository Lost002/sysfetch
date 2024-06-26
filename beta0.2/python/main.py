from os import popen
from parseconfig import getcolor
import psutil

RAM:str = str(psutil.virtual_memory())[6:]
BYTES_TO_GB:int = 1_000_000_000

class main:
    def __init__(self):
        self.textcolorfg = getcolor.fg_color_text
        self.FIRST_CHAR:str = getcolor.fg_color_border + "| " + getcolor.reset
        self.SEPERATOR:str = getcolor.fg_color_border + "\n|" + getcolor.reset 
        self.OS_SEPERATE:str = ""
        self.TOTAL_SEPERATE:str = ""
        self.PERCENT_SEPERATE:str = ""
        self.IN_USE_SEPERATE:str = ""
        self.TOP_BOTTOM:str = getcolor.fg_color_border + ""
        self.FREE_SEPERATE:str = ""

        for i in range(max(len(os), len(total), len(percent), len(in_use), len(free))-len(os)-1):
            self.OS_SEPERATE += " "
        for i in range(max(len(os), len(total), len(percent), len(in_use), len(free))-len(total)):
            self.TOTAL_SEPERATE += " "
        for i in range(max(len(os), len(total), len(percent), len(in_use), len(free))-len(percent)):
            self.PERCENT_SEPERATE += " "
        for i in range(max(len(os), len(total), len(percent), len(in_use), len(free))-len(in_use)):
            self.IN_USE_SEPERATE += " "
        for i in range(max(len(os), len(total), len(percent), len(in_use), len(free))-len(free)):
            self.FREE_SEPERATE += " "
        for i in range(max(len(os), len(total), len(percent), len(in_use), len(free))+3):
            self.TOP_BOTTOM += "-"

        self.TOP_BOTTOM += getcolor.reset+"\n"
        self.OS_SEPERATE += getcolor.fg_color_border + " |" + getcolor.reset
        self.TOTAL_SEPERATE += getcolor.fg_color_border + " |" + getcolor.reset
        self.PERCENT_SEPERATE += getcolor.fg_color_border + " |" + getcolor.reset
        self.IN_USE_SEPERATE += getcolor.fg_color_border + " |" + getcolor.reset
        self.FREE_SEPERATE += getcolor.fg_color_border + " |" + getcolor.reset
        self.fetch = f"{self.TOP_BOTTOM}{self.FIRST_CHAR}{self.textcolorfg}{os}{getcolor.reset}{self.OS_SEPERATE}{self.SEPERATOR}{self.textcolorfg}{total}{getcolor.reset}{self.TOTAL_SEPERATE}{self.SEPERATOR}{self.textcolorfg}{percent}{getcolor.reset}{self.PERCENT_SEPERATE}{self.SEPERATOR}{self.textcolorfg}{in_use}{getcolor.reset}{self.IN_USE_SEPERATE}{self.SEPERATOR}{self.textcolorfg}{free}{getcolor.reset}{self.FREE_SEPERATE}\n{self.TOP_BOTTOM}"
    
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
        total = f" RAM: Total:   {str(total)} GB"
        return total

    def RAM_percent():
        """Gets percent of RAM being used"""
        global percent
        percent = RAM[RAM.index("percent"):].replace("percent=", "")
        percent = percent[:percent.index(",")]
        percent = f" RAM: Percent: {percent}%"
        return percent
        
    def RAM_in_use():
        """Gets amount of ram that is in-use"""
        global in_use
        in_use = RAM[RAM.index("used"):].replace("used=", "")
        in_use = in_use[:in_use.index(",")]
        in_use = int(in_use)/BYTES_TO_GB
        in_use = round(in_use,2)
        in_use = f" RAM: In Use:  {str(in_use)} GB"
        return in_use
    def RAM_free():
        global free
        free = RAM[RAM.index('free'):].replace("free=", "")
        free = free[:free.index(",")]
        free = int(free)/BYTES_TO_GB
        free = round(free, 2)
        free = f" RAM: Free:    {str(free)} GB"
        return free

    os = os()
    total = RAM_total()
    percent = RAM_percent()
    in_use = RAM_in_use()
    free = RAM_free()

    def __str__(self):
        return self.fetch

if __name__ == "__main__":
    print(main())