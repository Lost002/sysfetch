from json import load

class parse:
    global config
    with open('.config/.config.jsonc') as conf:
        config = load(conf)

    def fg_color_border():
        return config["fg-color-border"]
    def fg_color_text():
        return config["fg-color-text"]
    def bg_color_border():
        return config["bg-color-border"]
    def bg_color_text():
        return config["bg-color-text"]

    def __str__(self):
        return "Nothing Here Yet"


if __name__ == "__main__":
    print(parse())