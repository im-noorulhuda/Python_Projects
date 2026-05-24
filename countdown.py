from colorama import Fore, Style
from datetime import datetime
import time


print(Fore.WHITE + "=" * 26)
print(Fore.YELLOW + "   🌙 Eid Countdown 🌙")
print(Fore.WHITE + "=" * 26)

print(Fore.LIGHTCYAN_EX + "\n   ⏳ Remaining Time \n")


eid = datetime(2026, 5, 27)


while True:
    now = datetime.now()
    print(Fore.WHITE + "\n Current Date : ", now)
    timeleft = eid - now

    days = timeleft.days
    hours, remainder = divmod(timeleft.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(
        f"\r✨ {Fore.YELLOW}Only {Fore.WHITE}{days} Days, {hours} Hours, {minutes} Mins, and {seconds} Secs {Fore.YELLOW}left until Eid! 🕋🐑 ", 
        end=""
    )
    time.sleep(1)
