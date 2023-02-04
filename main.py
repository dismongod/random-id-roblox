from pystyle import Colorate, Colors, Center
from random import randint
import random
import string


user = "" + "".join(random.choices(string.ascii_letters + string.digits, k=10))
password = "" + "".join(random.choices(string.ascii_letters + string.digits, k=10))

print(
        Colorate.Horizontal(
            Colors.blue_to_cyan,
            Center.XCenter(
                f"""
                



╦ ╦╦ ╦╔═╗╦═╗╔═╗  ╦═╗╔═╗╔╗╔╔╦╗╔═╗╔╦╗  ╦╔╦╗  ╦═╗╔═╗╔╗ ╦  ╔═╗═╗ ╦  
╠═╣╚╦╝╠═╝╠╦╝║╣   ╠╦╝╠═╣║║║ ║║║ ║║║║  ║ ║║  ╠╦╝║ ║╠╩╗║  ║ ║╔╩╦╝  
╩ ╩ ╩ ╩  ╩╚═╚═╝  ╩╚═╩ ╩╝╚╝═╩╝╚═╝╩ ╩  ╩═╩╝  ╩╚═╚═╝╚═╝╩═╝╚═╝╩ ╚═  


                 [+] Dev : Hypre#9999
                 [+] Credit : RANDOM ID ROBLOX BY HYPRE
        
        
        
        """
        ),
        
     )
  
  )


print('\n')
print(Colorate.Horizontal(Colors.rainbow, f'USER NAME : {user}'))
print('\n')
print(Colorate.Horizontal(Colors.rainbow, f'PASSWORD : {password}'))
print('\n')
