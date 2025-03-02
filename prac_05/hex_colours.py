HEX_COLOURS = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "AQUAMARINE": "#7fffd4",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "BISQUE": "#ffe4c4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#ffebcd",
    "BLUE": "#0000ff"
}

def main():
    print("Enter a color name to get its hexadecimal code. Enter a blank line to exit.")
    while True:
        color_name = input("Enter color name: ").strip().upper()
        if not color_name:
            print("Exiting program.")
            break
        try:
            print(f"The hexadecimal code for {color_name.lower()} is {HEX_COLOURS[color_name]}")
        except KeyError:
            print(f"Sorry, {color_name.lower()} is not in our list of colors.")

main()