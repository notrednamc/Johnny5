from core.utils import color_text, setup_logger
from termcolor import colored

def show_banner(mode):
    banners = {
        "name"  : banner_name,
        "alive" : banner_alive,
        "battle": banner_battle,
        "sleep" : banner_sleep,
        "recon" : banner_recon,
        "hack"  : banner_hack
    }

    banner = banners.get(mode, banner_name)()
    print(colored(banner, 'cyan'))
    print(colored(f"Johnny 5 - Mode: {mode.upper()} 🚀\n", 'yellow', attrs=['bold']))

def banner_alive():
    banner = r"""
           ___
          [o o]     ________
         /  V  \   | Johnny |
        /| === |\  |   5    |
       /_|_____|_\ |--------|
         || ||     |  IS    |
        (_)(_)     | ALIVE! |
        ||  ||     |________|
     ___||__||___
    /   ||  ||   \
   |____||__||____|
    (__)    (__)
"""
    print(color_text(banner, "green"))

def banner_battle():
    banner = r"""
           ___
          [⚙⚙]     ________
         / >_< \  | Johnny |
        /|  X  |\ |   5    |
       /_|_____|_\|--------|
         || ||     | TARGET|
        (__)(__)   |ACQUIRED|
        ||  ||     |________|
     ___||__||___
    /   ||  ||   \
   |____||__||____|
    (__)    (__)
"""
    print(color_text(banner, "red"))

def banner_sleep():
    banner = r"""
           ___
          [- -]     ________
         /  zZ  \  | Johnny |
        /|  ... |\ |   5    |
       /_|_____|_\ |--------|
         || ||     |  SLEEP |
        (__)(__)   |  MODE  |
        ||  ||     |________|
     ___||__||___
    /   ||  ||   \
   |____||__||____|
    (__)    (__)
"""
    print(color_text(banner, "yellow"))

def banner_recon():
    banner = r"""
           ___
         [🔍  o]    ________
         \ o__/   | Johnny |
        /|  .-. |\|   5    |
       /_|__|_|_\ |--------|
         || ||     |SCANNING|
        (__)(__)   |........|
        ||  ||     |________|
     ___||__||___
    /   ||  ||   \
   |____||__||____|
    (__)    (__)
"""
    print(color_text(banner, "red"))

def banner_hack():
    banner = r"""
           ___
         [>_>]     ________
         \___/    | Johnny |
        /| -_- |\ |   5    |
       /_|_____|_\|--------|
         || ||     |ACCESS |
        (__)(__)   | GRANTED|
        ||  ||     |________|
     ___||__||___
    /   ||  ||   \
   |____||__||____|
    (__)    (__)
"""
    print(color_text(banner, "green"))

def banner_name():
    banner = r"""
  ____            _ _______                  _             
 |  _ \ ___  __ _| |_   _|__ _ __ _ __   ___| |_ ___  _ __ 
 | |_) / _ \/ _` | | | |/ _ \ '__| '_ \ / _ \ __/ _ \| '__|
 |  _ <  __/ (_| | | | |  __/ |  | | | |  __/ || (_) | |   
 |_| \_\___|\__,_|_| |_|\___|_|  |_| |_|\___|\__\___/|_|   
"""
    print(color_text(banner, "cyan"))
    print(color_text("        [ Red Team Modular Toolkit 🕵️‍♂️ ]\n", "yellow"))