import subprocess
import os
import time

GREEN = "\033[92m"
RED = "\033[91m"

apps_apt = [
    "i3 i3status",
    "feh picom",
    "unzip",
    "traceroute",
    "polybar",
    "fish",
    "chromium-browser",
    "language-pack-ru",
    "rofi",
    "kitty",
    "curl",
    "bibata-cursor-theme",
    "lxappearance",
    "lsd",
    "neovim",
    "cmatrix",
    "hollywood",
    "cbonsai",
    "cargo",
    "dex",
    "xss-lock",
    "network-manager-gnome",
]

packages_cargo = [
    "bat",
    "lsd",
]

errors = []

def run(cmd):
        try:
            subprocess.run(cmd, shell=True, check=True)
            print(f"{GREEN} {cmd}")
        except subprocess.CalledProcessError as e:
            errors.append(f"{RED}Ошибка в команде: {cmd}")

tmp_flag = os.path.expanduser("~/tmp/tmp_for_py")

if not os.path.exists(tmp_flag):

    #Прелюдия
    run("sudo apt update")
    run("sudo apt upgrade -y")

    #Для вируалки
    run("sudo apt install -y build-essential dkms gcc make perl")
    run("sudo apt install -y linux-headers-$(uname -r)")

    #Установка из apt
    for app in apps_apt:
        run(f"sudo apt install -y {app}")

    #Установка cargo
    run("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y")

    #Шрифт
    if not os.path.exists(os.path.expanduser("~/.local/share/fonts/FiraCode")):
        run("wget -O /tmp/FiraCode.zip https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/FiraCode.zip")
        run("unzip /tmp/FiraCode.zip -d /tmp/FiraCode")
        run("mkdir -p ~/.local/share/fonts/FiraCode")
        run("cp /tmp/FiraCode/*.ttf ~/.local/share/fonts/FiraCode/")
        run("fc-cache -fv")

    #spf
    if not os.path.exists("/usr/local/bin/spf"):
        run("curl -sLo- https://superfile.dev/install.sh | bash")
    else:
        print("Superfile уже установлен.")

    run("mkdir -p ~/tmp/tmp_for_py")
    print("Первая часть готова")

    if errors != []:
        for er in errors:
            print(er)
    else:
        print("Ошибок нет...")
        time.sleep(3)
        run("reboot")

else:
    #Установка из cargo
    for pkg in packages_cargo:
        run(f"cargo install --locked {pkg}")

    # Клонировать репозиторий
    run("git clone https://github.com/Alehandro77/for_ubuntu/configs.git ~/dotfiles")

    #Удаление конфигов по умолчанию
    run("rm -rf ~/.config/i3")
    run("rm -rf ~/.config/polybar")
    run("rm -rf ~/.config/kitty")
    run("rm -rf ~/.config/fish")
    run("rm -rf ~/.config/rofi")
    run("rm -rf ~/.config/superfile")

    # Скопировать конфиги на места
    run("cp -rf ~/dotfiles/i3 ~/.config/")
    run("cp -rf ~/dotfiles/polybar ~/.config/")
    run("cp -rf ~/dotfiles/kitty ~/.config/")
    run("cp -rf ~/dotfiles/fish ~/.config/")
    run("cp -rf ~/dotfiles/rofi ~/.config/")
    run("cp -rf ~/dotfiles/superfile ~/.config/")

    #Скачивание обоев
    run("git clone https://github.com/Alehandro77/for_ubuntu/walpeper.jpg ~/Pictures")

    #Полибар исполняемый
    run("chmod +x ~/.config/polybar/launch.sh")

    run("rm -rf ~/tmp/tmp_for_py")
    print("Вторая часть готова")

    if errors != []:
        for er in errors:
            print(er)
    else:
        print("Ошибок нет...")
        time.sleep(3)
        run("reboot")

