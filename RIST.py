import Options
from Tkinter import Tk as tk
from webbrowser import open as wopen

if __name__ == "__main__":
    rw = tk()
    rw.title("RIST Reputation Investigation Spawn Tool v.1.04 Jan2017")
    rw.geometry("600x300")
    A = Options.option(rw, thetype="IPs")
    A.grid(sticky="NW")
    B = Options.option(rw, thetype="URLs")
    B.grid(sticky="NW")
    C = Options.option(rw, thetype="SPECs")
    C.grid(sticky="NW")
    wopen("https://github.com/SYANiDE-/RIST")
    rw.lift()
    rw.call('wm', 'attributes', '.', '-topmost', True)
    rw.mainloop()



