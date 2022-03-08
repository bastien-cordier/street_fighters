from random import randint
from player import Player
from ia import IA

# PRÉSENTATION
print("""
   _____ __                 __            
  / ___// /_________  ___  / /_           
  \__ \/ __/ ___/ _ \/ _ \/ __/           
 ___/ / /_/ /  /  __/  __/ /_             
/__________/   \____\_______/             
   / ____(_)___ _/ /_  / /____  __________
  / /_  / / __ `/ __ \/ __/ _ \/ ___/ ___/
 / __/ / / /_/ / / / / /_/  __/ /  (__  ) 
/_/   /_/\__, /_/ /_/\__/\___/_/  /____/  
        /____/                            
""")
print("Bienvenue dans StreetFighters LVIII 🕹")
player_name = input("Choisissez votre pseudo : ")

ADVERSAIRES = ["Ryu", "Ken", "Dhalsim", "Blanka", "Zangief"]
for i in enumerate(ADVERSAIRES, 1):
  print(f"{i}")
ia_name = input("Choisissez votre adversaire : ")
ia_name = ADVERSAIRES[int(ia_name)-1]

player = Player(player_name, 100, 3, 1)
ia = IA(ia_name, 100)

print(f"\nOk {player.get_name().upper()} ! 🔥\n{ia.get_name().upper()} sera votre adversaire 👹")
print("=" * 50)
print("""
    __    _____________ _____    _______       __    __ 
   / /   / ____/_  __( ) ___/   / ____(_)___ _/ /_  / /_
  / /   / __/   / /  |/\__ \   / /_  / / __ `/ __ \/ __/
 / /___/ /___  / /    ___/ /  / __/ / / /_/ / / / / /_  
/_____/_____/ /_/    /____/  /_/   /_/\__, /_/ /_/\__/  
                                     /____/             
""")
print("=" * 50)

# FIGHT ⚔️

while True:
  player_choice = ""
  while player_choice not in ["1", "2", "3"]:
    player_choice = input(f"""
Tape sur 1 pour attaquer 🤺 
Tape sur 2 si tu souhaites prendre un soin 💊 ({player.get_pilule()} 💊 restantes) 
Tape sur 3 pour une attaque spéciale de 50 de dégâts 🤯 ? ({player.get_attackSP()} attaque spéciale disponible) 

Quel est ton choix ? """)

  if player_choice == "1":
    player_attack = randint(5, 30)
    updated_hp = ia.get_hp() - player_attack
    ia.set_hp(updated_hp)
    print(f"Vous infligez {player_attack} points de dégâts sur votre adversaire 😱")
  elif player_choice == "2":
    if player.get_pilule() > 0:
      player_bonus = randint(10, 35)
      updated_hp = player.get_hp() + player_bonus
      player.set_hp(updated_hp)
      updated_pilule = player.get_pilule() - 1
      player.set_pilule(updated_pilule)
      print(f"Vous venez de récupérez {player_bonus} points de vie 💖\nIl vous reste {player.get_pilule()} 💊")
    else:
      print("Vous n'avez plus de potions")
      continue
  elif player_choice == "3":
    if player.get_attackSP() > 0:
      player_finishHim = 50
      updated_hp = ia.get_hp() - player_finishHim
      ia.set_hp(updated_hp)
      updated_attackSP = player.get_attackSP() -1
      player.set_attackSP(updated_attackSP)
      print(f"Vous venez d'utiliser votre seule attaque spéciale 🤯\n {player_finishHim} points de dégâts sur {ia.get_name().upper()}")
    else:
      print("Vous n'avez plus d'attaques spéciales ...")
      continue

  if ia.get_hp() <= 0:
    print("""
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗    ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║    ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║    ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║    ╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║    ██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═╝

    """)
    break

  ia_attack = randint(10, 35)
  update_hp = player.get_hp() - ia_attack
  player.set_hp(update_hp)
  print(f"{ia.get_name().upper()} vient de vous infliger {ia_attack} points de dégâts ...")
  print(f"{player.get_name().upper()} = {player.get_hp()} 💖\n{ia.get_name().upper()} = {ia.get_hp()} 💖")

  if player.get_hp() <= 0:
    print("""
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   
    """)
    break

# FINALE

print(f"Fin de la partie ! Merci d'avoir joué {player.get_name().upper()}")