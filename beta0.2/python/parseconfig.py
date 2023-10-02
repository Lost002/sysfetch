import json
class getcolor:
    with open('/usr/bin/SysFetch/.config/.config.jsonc') as conf:
        config = json.load(conf)
    fg = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "grey": "37",
        "white": "0",
        "0": "0",
        "1": "1"
    }
    bg = {
        "black": "40",
        "red": "41",
        "green": "42",
        "yellow": "43",
        "blue": "44",
        "magenta": "45",
        "cyan": "46",
        "white": "47",
        "0": "0",
        "1": "1"
    }
    fg_color_border = "\033[0;"+fg[config["fg-color-border"]]+"m".replace(" ", "")
    fg_color_text = "\033[0;"+fg[config["fg-color-text"]]+"m".replace(" ", "")
    bg_color_border = "\033[0;"+fg[config["bg-color-border"]]+"m".replace(" ", "")
    bg_color_text = "\033[0;"+fg[config["bg-color-text"]]+"m".replace(" ", "")
    reset = "\033[0m".replace(" ", "")