from json import load

with open(".config/.ascii.json", "r") as jsonfile:
    distros = load(jsonfile)
with open("/etc/os-release", "r") as finddsitro:
    lines = finddsitro.readlines()
    distro = lines[0].replace("NAME=", "").replace("\n", "").replace("\"", "").replace("'", "").upper()
print(distro)