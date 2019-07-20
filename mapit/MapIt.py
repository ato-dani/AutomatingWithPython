#!usr/bin/python3
import webbrowser,sys
def main():
    address = "https://www.google.com/maps/place/"
    if len(sys.argv) <= 1:
        print("No address was given")
    else:
        address += " ".join(sys.argv[1:])
        webbrowser.open(address)
if __name__ == "__main__":
    main();

