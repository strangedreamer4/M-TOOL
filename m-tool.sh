#!/bin/bash
# [/07/04/31/31/03/08\]
# Install required system packages
sudo apt-get update -y
# Install required Python packages
pip3 install tkinter Pillow pyrebase4 gTTS playsound
clear
git pull
sleep 1
clear
git stash
sleep 1
git pull
sleep 1
clear
git stash
sleep 1
chmod +x m-tool.sh
# Function to animate opening effect with fade-in and banner
animate_opening_effect() {
    clear
    banner_text="
███╗░░░███╗░░░░░░████████╗████╗████╗████╗████╗██╗░░░░░
████╗░████║░░░░░░╚══██╔══╝██╔═╝╚═██║██╔═╝╚═██║██║░░░░░
██╔████╔██║█████╗░░░██║░░░██║░░░░██║██║░░░░██║██║░░░░░
██║╚██╔╝██║╚════╝░░░██║░░░██║░░░░██║██║░░░░██║██║░░░░░
██║░╚═╝░██║░░░░░░░░░██║░░░████╗████║████╗████║███████╗
╚═╝░░░░░╚═╝░░░░░░░░░╚═╝░░░╚═══╝╚═══╝╚═══╝╚═══╝╚══════╝
                            link to web : https://mtool4.netlify.app
                                                  by StRaNgEdReAmEr."
    echo "$banner_text"

    text="Welcome to MTool..."
    length=${#text}

    for ((i = 0; i < length; i++)); do
        echo -e "\e[96m${text:0:i}\e[0m"
        sleep 0.1
        clear
        echo "$banner_text"
    done

    # After the fade-in effect, clear the screen once more
    clear
}

# Function to simulate a "hacking" effect
simulate_hacking_effect() {
    clear
    echo "Hacking into the mainframe..."
    sleep 2
    echo "Decrypting security protocols..."
    sleep 2
    echo "Bypassing firewall..."
    sleep 2
    echo "Access granted!"
    sleep 1
}

# Function to install and launch a tool from GitHub
install_and_launch_tool() {
    animate_opening_effect

    case $1 in
        "1")
            tool_dir="hellcat"
            tool_repo="https://github.com/strangedreamer4/hellcat.git"
            tool_script="python3 hellcat.py"
            tool_banner="Tool 1 (hellcat)"
            ;;
        "2")
            tool_dir="MacChanger"
            tool_repo="https://github.com/strangedreamer4/MacChanger.git"
            tool_script="chmod +x machanger.sh && ./machanger.sh"
            tool_banner="Tool 2 (MacChanger)"
            ;;
        "3")
            tool_dir="IPRUNNER"
            tool_repo="https://github.com/strangedreamer4/IPRUNNER.git"
            tool_script="chmod +x iprunner.sh && ./iprunner.sh"
            tool_banner="Tool 3 (iprunner)"
            ;;
        "4")
            tool_dir="M-SENDER"
            tool_repo="https://github.com/strangedreamer4/M-SENDER.git"
            tool_script="chmod +x msender.py && python3 msender.py"
            tool_banner="Tool 4 (M-Sender)"
            ;;   
        "5")
            tool_dir="VCHAT"
            tool_repo="https://github.com/strangedreamer4/VCHAT.git"
            tool_script="chmod +x vchat.py && python3 vchat.py"
            tool_banner="Tool 4 (VChat)"
            ;;       
            
        *)
            echo "Invalid selection"
            return
            ;;
    esac

    if [ -d "$tool_dir" ]; then
        echo "$tool_banner is already installed. Launching..."
    else
        echo "Installing $tool_banner..."
        git clone "$tool_repo" "$tool_dir"
    fi

    cd "$tool_dir"
    simulate_hacking_effect
    eval "$tool_script"

    # Automatically delete the tool after it has been run
    cd ..
    rm -rf "$tool_dir"
    chmod +x m-tool.sh
}

# Main menu
while true; do
    clear
    echo -e "███╗░░░███╗░░░░░░████████╗████╗████╗████╗████╗██╗░░░░░"
    echo -e "████╗░████║░░░░░░╚══██╔══╝██╔═╝╚═██║██╔═╝╚═██║██║░░░░░"
    echo -e "██╔████╔██║█████╗░░░██║░░░██║░░░░██║██║░░░░██║██║░░░░░"
    echo -e "██║╚██╔╝██║╚════╝░░░██║░░░██║░░░░██║██║░░░░██║██║░░░░░"
    echo -e "██║░╚═╝░██║░░░░░░░░░██║░░░████╗████║████╗████║███████╗"
    echo -e "╚═╝░░░░░╚═╝░░░░░░░░░╚═╝░░░╚═══╝╚═══╝╚═══╝╚═══╝╚══════╝
                            link to web : https://mtool4.netlify.app
                                                by StRaNgEdReAmEr."
    echo -e "\e[95m*********************\e[0m"
    echo -e "\e[95m**** \e[93mMTool\e[0m \e[95m************\e[0m"
    echo -e "\e[95m*********************\e[0m"
    echo "Select a tool to install and launch:"
    echo -e "\e[93m1. Tool 1 (hellcat)\e[0m"
    echo -e "\e[93m2. Tool 2 (MacChanger)\e[0m"
    echo -e "\e[93m3. Tool 3 (iprunner)\e[0m"
    echo -e "\e[93m4. Tool 4 (M-sender)\e[0m"
    echo -e "\e[93m5. Tool 5 (VChat)\e[0m"
    echo -e "\e[91mQ. Quit\e[0m"

    read choice

    case $choice in
        "1" | "2" | "3" | "4" | "5")
            install_and_launch_tool "$choice"
            ;;
        "Q" | "q")
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid selection"
            ;;
    esac
done
