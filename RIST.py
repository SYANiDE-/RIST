import Options
from Tkinter import Tk as tk
from webbrowser import open as wopen

if __name__ == "__main__":
    rw = tk()
    rw.title("RIST Reputation Investigation Spawn Tool")
    rw.geometry("600x300")
    A = Options.option(rw, thetype="IPs")
    A.grid(sticky="NW")
    B = Options. option(rw, thetype="URLs")
    B.grid(sticky="NW")
    wopen("https://github.com/SYANiDE-/RIST")
    rw.lift()
    rw.call('wm', 'attributes', '.', '-topmost', True)
    rw.mainloop()



