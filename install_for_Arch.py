import subprocess
import os
import time

GREEN = "\033[92m"
RED = "\033[91m"

apps_apt = [

    #Внешний вид
    "i3-wm",
    "polybar",
    "rofi",
    "feh picom",
    "otf-hasklig-nerd",
    "lxappearance",

    #Полезные программы
    "unzip",
    "lsd",
    "bat",

    #Терминал
    "kitty",
    "fish",

    #Для повседневной жизни
    "firefox",
    "neovim",

    #Приколы
    "cmatrix",
]

packages_yay = [
    "hollywood",
    "cbonsai",
    "superfile",
]

errors = []

def run(cmd):
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f"{GREEN} {cmd}")
        except subprocess.CalledProcessError as e:
            errors.append(f"{RED}Ошибка в команде: {cmd}")

def install_yay():
    if os.path.exists("/usr/bin/yay") or os.path.exists("/usr/local/bin/yay"):
        print(f"{GREEN} Yay уже установлен")
        return
    
    run("sudo pacman -S --needed --noconfirm git base-devel")
    run("git clone https://aur.archlinux.org/yay.git /tmp/yay")
    run("cd /tmp/yay && makepkg -si --noconfirm")
    run("rm -rf /tmp/yay")

tmp_flag = os.path.expanduser("~/tmp/tmp_for_py")

if not os.path.exists(tmp_flag):

    print(f"{GREEN} Начало первой части")
    time.sleep(5)

    #Прелюдия
    run("sudo pacman -Syy")
    install_yay()

    #Установка из pacman
    for app in apps_apt:
        run(f"sudo pacman -S --needed --noconfirm {app}")

    #Установка из AUR
    for pkg in packages_yay:
        run(f"yay -S --needed --noconfirm {pkg}")

    #Отчистка кэша шрифта
    run("fc-cache -fv")

    run("mkdir -p ~/tmp/tmp_for_py")

    print(f"{GREEN} Первая часть готова")

    if errors != []:
        for er in errors:
            print(er)
        print(f"{RED} Были ошибки!")
    else:
        print(f"{GREEN} Ошибок нет...")
        time.sleep(3)
        run("reboot")

else:

    print(f"{GREEN} Начало второй части")
    time.sleep(5)

    #Удаление конфигов по умолчанию
    confs = ["i3", "polybar", "kitty", "fish", "rofi", "superfile"]

    for conf in confs:
        run(f"rm -rf ~/.config/{conf}")

    for conf in confs:
        run(f"cp -rf ~/dotfiles/{conf} ~/.config/")

    #Перемещение обоев
    run("cp -f ~/dotfiles/walpeper.jpg ~/Pictures")

    #Полибар исполняемый
    run("chmod +x ~/.config/polybar/launch.sh")

    run("rm -rf ~/tmp/tmp_for_py")
    run("rm -rf ~/dotfiles")

    print(f"{GREEN} Вторая часть готова")

    if errors != []:
        for er in errors:
            print(er)
        print(f"{RED} Были ошибки!")
    else:
        print(f"{GREEN} Ошибок нет...")
        time.sleep(3)
        run("reboot")
