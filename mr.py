import os
import sys
import time
from platform import system
from datetime import datetime  # Importing datetime to show date and time

# Clear Screen Command
def cls():
    os.system('clear' if system() == 'Linux' or system() == 'Darwin' else 'cls')

# Colors for styling
RED = '\033[1;31;1m'
GREEN = '\033[1;32;1m'
YELLOW = '\033[1;33;1m'
BLUE = '\033[1;34;1m'
PURPLE = '\033[1;35;1m'
CYAN = '\033[1;36;1m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Display the full interface with updated banner color
def display_interface():
    print(f"""{GREEN}
═══════════════════════════════════════════════════════
{YELLOW}            [ 420 COMMAND ]                
═══════════════════════════════════════════════════════
{BOLD}{GREEN}OWNER : ZIDI JUTT X PANGYBAZ{RESET}
{BOLD}{GREEN}ADMINS : KHANZADA X ZAINI 
{BOLD}{GREEN}MEMBERS : MENTAL MENTAL X MEHAR HUKUM Z X SHEZI X MALANG BABA X ALL 302 WALY BADMASH {RESET}
{BOLD}{GREEN}GANG NAME: JUTT BADSHAH 302{RESET}
═══════════════════════════════════════════════════════
 ## ##    ## ##   ## ##              ## ##     ##     ###  ##   ## ##   
##   ##  ##   ##  ##  ##            ##   ##     ##      ## ##  ##   ##  
     ##  ##   ##      ##            ##        ## ##    # ## #  ##       
   ###   ##   ##     ##             ##  ###   ##  ##   ## ##   ##  ###  
     ##  ##   ##    ##              ##   ##   ## ###   ##  ##  ##   ##  
##   ##  ##   ##   #   ##           ##   ##   ##  ##   ##  ##  ##   ##  
 ## ##    ## ##   ######             ## ##   ###  ##  ###  ##   ## ##   
                                                                      """)

    print("\n" * 2)  # Add extra space between banner and menu options

    print(f"{BOLD}{BLUE}[1] ENTER FACEBOOK ID LINK OR NUMBER{RESET}")
    print(f"{BOLD}{BLUE}[2] EXTRACT DATA{RESET}")
    print(f"{BOLD}{BLUE}[3] CHECK OLD COMMAND'S LINK + NUMBERS{RESET}")
    print(f"{BOLD}{BLUE}[4] CONTACT WITH ZIDI JUTT X PANGYBAZ{RESET}")
    print(f"{BOLD}{BLUE}[5] Exit the System{RESET}")
    print(f"═══════════════════════════════════════════════════════")

# Fake Loading Animation
def loading_animation(message):
    animation = ["|", "/", "-", "\\"]
    for i in range(20):  # Adjust length to fit your needs
        sys.stdout.write(f"\r{YELLOW}{message} {animation[i % len(animation)]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)

# Fake Data Hacking Display
def fake_hacking_process(profile_id):
    loading_animation("PANGYBAZ X ZIDI JUTT ONFIRE")

    print(f"\n{CYAN}[INFO] PLEASE WAIT ZIDI JUTT X PANGYBAZ IS WORKING...{RESET}")
    time.sleep(2)
    
    print(f"\n{GREEN}[✓] Successfully connected to Facebook server for {profile_id}{RESET}")
    time.sleep(1)
    
    loading_animation("loading [ PANGYBAZ X ZIDI XWD ] retrieving ALL CONTACT LIST + DATA")
    
    print(f"\n{GREEN}[✓] Data extraction initiated...{RESET}")
    time.sleep(1)
    
    print(f"{RED}[WARNING] Extracting sensitive data... This may take a few minutes...{RESET}")
    time.sleep(2)
    
    loading_animation("loading [PANGYBAZ X ZIDI JUTT XWD] processing data")
    
    print(f"\n{GREEN}[INFO] Data secured for owner {BOLD}ZIDI JUTT X PANGYBAZ{RESET}")
    print(f"{GREEN}[INFO] Gang Name: {BOLD}JUTT BADSHAH 302{RESET}")
    print(f"{GREEN}[INFO] Admin: {BOLD}KHANZADA URF ANAS X ZAINI {RESET}\n")
    time.sleep(1)
    
    print(f"{CYAN}[INFO] PANGYBAZ X ZIDI JUTT ONFIRE{RESET}")

    # List of phone numbers (updated)
    phone_numbers = [
        "AKMAL MAMO\n+923047114663\n",
        "ANTI\n+923002069700\n",
        "AQSA APYY\n+923222201500\n",
        "AREEBA\n+923333473487\n",
        "ASAD BHAI\n+923279176972\n",
        "ASAD BHAI 2\n+923474745746\n",
        "ATIF BHAI\n+923030071265\n",
        "ABU JAN\n+923068277362\n",
        "AMI JAN\n+923015370468\n",
        "ANTI NASEEM\n+923082806353\n",
        "ATIF PAROSI\n+923122087018\n",
        "AYESHA\n+923101206686\n",
        "AZHAR BHAI\n+923162084407\n",
        "AZHAR 2\n+923132310315\n",
        "BAJI KHDA WAR\n+923212860863\n",
        "BAJI MANZURA\n+923242008896\n",
        "BAJI BAGALI\n+923212469172\n",
        "BAJI ANVRI\n+923064216350\n",
        "BAJI\n+923343553146\n",
        "BANO FRIEND\n+923497797370\n",
        "CHACHU JAMEEL\n+923092592880\n",
        "CHARSAN\n+923480738138\n",
        "CHARSAN INSIDE\n+923057273845\n",
        "FAHEEM BHAI 2\n+923027359832\n",
        "FAHEEM BHAI\n+923166515077\n",
        "FAHEEM BHAI\n+923029298468\n",
        "FIZA\n+923249247821\n",
        "FAISAL BHAI\n+923213759764\n",
        "FAIZAN\n+923201275508\n",
        "HAMZA FRIEND\n+923067369093\n",
        "HASSAN BHAI\n+923132226121\n",
        "HASSAN BHAI 2\n+923131386866\n",
        "ISHFAQ MAMO\n+923007060632\n",
        "IBRAR BHAI\n+923452925595\n",
        "J CHACHU\n+923072486801\n",
        "J CHACHU 2\n+923462471218\n",
        "JAWED BHAI\n+923002787458\n",
        "KAKA MAMA\n+923139486935\n",
        "KAINAT\n+923216093842\n",
        "MAHNOOR\n+923022931695\n",
        "MAMO NADEEM\n+923448212616\n",
        "MINAHA SISTER\n+923340393028\n",
        "MISBAH APYY\n+923092008267\n",
        "MADIHA\n+923232343422\n",
        "MAHNOOR APYY\n+923042382113\n",
        "MALAIKA\n+923476223352\n",
        "MAMA\n+923022160488\n",
        "MAMO BUSHIR\n+923019299257\n",
        "MUSTAQ BHAI\n+923212046491\n",
        "MAMU LANDHI\n+923146581585\n",
        "NIDA\n+923123599257\n",
        "NAWAZ BHAI\n+923101000080\n",
        "MANWAR BAJI\n+923173028949\n",
        "PAPA\n+923007319760\n",
        "RAMZAN BHAI\n+923022255239\n",
        "RAZAK BHAI\n+923213863541\n",
        "SAIMA ANTI\n+923074789481\n",
        "SADAF API\n+923017802041\n",
        "SAIMA SON\n+923370447600\n",
        "SAQIB KI MAMA\n+923228019727\n",
        "SHAFIQ BHAI\n+923249420617\n",
        "SHAHZAIB BHAI\n+923462821606\n",
        "SHERY MOTHER\n+923067021113\n",
        "SIKNDAR BHAI\n+923219228940\n",
        "SONA ANTI RUKSANA\n+923222641669\n",
        "TAYYABA SISTER\n+923329476197\n",
        "TAYA ABU\n+923253695952\n",
        "TAYYABA\n+923352651489\n", 
        # (add more numbers here)
    ]
    
    # Show current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{CYAN}Date and Time: {current_time}{RESET}\n")
    
    # Print each phone number with a "PLEASE WAIT" message before it
    for number in phone_numbers:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{YELLOW}[INFO] PLEASE WAIT...{RESET}")
        time.sleep(1)  # Short delay before showing the number
        print(f"{CYAN}{number}{RESET}{PURPLE}(420 COMMAND) | {current_time}{RESET}")
        time.sleep(1)  # Adjust the delay as needed

# Waiting for Exit Prompt
def waiting_for_exit():
    input(f"\n{RED}[!] Press Enter to exit...{RESET}")

# Main menu with fake hacking process
def main_menu():
    while True:
        cls()  # Clear the screen to show the latest information
        display_interface()
        choice = input(f"{BOLD}[+] Select an option: {CYAN}")
        if choice == '1':
            profile_id = input(f"{BOLD}[+] Enter Facebook ID or Number: {CYAN}")
            print(f"{CYAN}[INFO] Facebook ID/Number: {profile_id}{RESET}")
            time.sleep(1)
        elif choice == '2':
            profile_id = input(f"{BOLD}[+] Input Facebook ID or Number for Extraction: {CYAN}")
            fake_hacking_process(profile_id)
        elif choice == '3':
            print(f"{CYAN}[INFO] Checking old command's links and numbers...{RESET}")
            time.sleep(2)
        elif choice == '4':
            print(f"{CYAN}[INFO] Contacting ZIDI JUTT X PANGYBAZ...{RESET}")
            time.sleep(2)
        elif choice == '5':
            print(f"\n{RED}[!] Exiting...{RESET}")
            waiting_for_exit()
            sys.exit(0)
        else:
            print(f"{RED}[!] Invalid option, please try again.{RESET}\n")
            time.sleep(1)

# Main Execution
if __name__ == "__main__":
    main_menu()