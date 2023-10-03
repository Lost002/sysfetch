# sysfetch
#### A **bash** neofetch alternative ~~with live system resorce usage.~~ DEPRECATED LIVE USAGE (May be added in/after release 2.0)

### !!For linux systems!!

## Dependencies
- Python3
- Bash
- psutil (Should already be installed with python3) (If not ```pip(3) install psutil```)

## Beta 0.2 Usage
1. 
    - source make.sh (from the projects make directory)
    - restart bash (You may also have to reboot)
    - Then, Just run ```sysfetch```!

2. To change color go to sysfetch/beta0.2/.config/.config.jsonc and change the fg-color-[test/border] then re-make the project after running ```sudo rm -rf /usr/bin/SysFetch``` OR edit /usr/bin/SysFetch/.config/.config.jsonc (No re-make or restart required!)
## Fixing make.sh gone wrong
```sudo rm -rf /usr/bin/SysFetch/```