from local_resources.colorama_master import colorama
from time import sleep
from os import system
developed_by = """
_______   ___________    ____  _______  __        ______   .______    _______  _______     
|       \ |   ____\   \  /   / |   ____||  |      /  __  \  |   _  \  |   ____||       \    
|  .--.  ||  |__   \   \/   /  |  |__   |  |     |  |  |  | |  |_)  | |  |__   |  .--.  |   
|  |  |  ||   __|   \      /   |   __|  |  |     |  |  |  | |   ___/  |   __|  |  |  |  |   
|  '--'  ||  |____   \    /    |  |____ |  `----.|  `--'  | |  |      |  |____ |  '--'  |   
|_______/ |_______|   \__/     |_______||_______| \______/  | _|      |_______||_______/    
                                                                                            
                 __  _ __  _    .______   ____    ____      __  _ __  _                                    
                /  \/ /  \/ |   |   _  \  \   \  /   /     /  \/ /  \/ |                                   
               |_/\__/_/\__/    |  |_)  |  \   \/   /     |_/\__/_/\__/                                    
                                |   _  <    \_    _/                                                       
                                |  |_)  |     |  |                                                         
                                |______/      |__|                      
"""

kyle_mistele = """
  __  _ __  _     __  ___ ____    ____  __       _______      __  _ __  _ 
 /  \/ /  \/ |   |  |/  / \   \  /   / |  |     |   ____|    /  \/ /  \/ |
|_/\__/_/\__/    |  '  /   \   \/   /  |  |     |  |__      |_/\__/_/\__/ 
                 |    <     \_    _/   |  |     |   __|                   
                 |  .  \      |  |     |  `----.|  |____                  
                 |__|\__\     |__|     |_______||_______|                 
                                                                          
   .___  ___.  __       _______.___________. _______  __       _______    
   |   \/   | |  |     /       |           ||   ____||  |     |   ____|   
   |  \  /  | |  |    |   (----`---|  |----`|  |__   |  |     |  |__      
   |  |\/|  | |  |     \   \       |  |     |   __|  |  |     |   __|     
   |  |  |  | |  | .----)   |      |  |     |  |____ |  `----.|  |____    
   |__|  |__| |__| |_______/       |__|     |_______||_______||_______|   
                                                                          
"""
andrew_mistele = """
___  ___           ___      .__   __.  _______  .______       ___________    __    ____    
\  \ \  \         /   \     |  \ |  | |       \ |   _  \     |   ____\   \  /  \  /   /    
 \  \ \  \       /  ^  \    |   \|  | |  .--.  ||  |_)  |    |  |__   \   \/    \/   /     
  >  > >  >     /  /_\  \   |  . `  | |  |  |  ||      /     |   __|   \            /      
 /  / /  /     /  _____  \  |  |\   | |  '--'  ||  |\  \----.|  |____   \    /\    /       
/__/ /__/     /__/     \__\ |__| \__| |_______/ | _| `._____||_______|   \__/  \__/        
                                                                                           
.___  ___.  __       _______.___________. _______  __       _______       ___  ___         
|   \/   | |  |     /       |           ||   ____||  |     |   ____|     /  / /  /         
|  \  /  | |  |    |   (----`---|  |----`|  |__   |  |     |  |__       /  / /  /          
|  |\/|  | |  |     \   \       |  |     |   __|  |  |     |   __|     <  < <  <           
|  |  |  | |  | .----)   |      |  |     |  |____ |  `----.|  |____     \  \ \  \          
|__|  |__| |__| |_______/       |__|     |_______||_______||_______|     \__\ \__\   
"""
michael_naguib = """
     ___   .___  ___.  __    ______  __    __       ___       _______  __      ___     
    /  /   |   \/   | |  |  /      ||  |  |  |     /   \     |   ____||  |     \  \    
   /  /    |  \  /  | |  | |  ,----'|  |__|  |    /  ^  \    |  |__   |  |      \  \   
  /  /     |  |\/|  | |  | |  |     |   __   |   /  /_\  \   |   __|  |  |       \  \  
 /  /      |  |  |  | |  | |  `----.|  |  |  |  /  _____  \  |  |____ |  `----.   \  \ 
/__/       |__|  |__| |__|  \______||__|  |__| /__/     \__\ |_______||_______|    \__\
                                                                                       
___           .__   __.      ___       _______  __    __   __  .______              ___
\  \          |  \ |  |     /   \     /  _____||  |  |  | |  | |   _  \            /  /
 \  \         |   \|  |    /  ^  \   |  |  __  |  |  |  | |  | |  |_)  |          /  / 
  \  \        |  . `  |   /  /_\  \  |  | |_ | |  |  |  | |  | |   _  <          /  /  
   \  \       |  |\   |  /  _____  \ |  |__| | |  `--'  | |  | |  |_)  |        /  /   
    \__\      |__| \__| /__/     \__\ \______|  \______/  |__| |______/        /__/ 
"""
def run_color_credits():
    system("cls")
    colorama.init()
    print(colorama.Fore.BLUE + developed_by)
    sleep(2.5)
    system("cls")
    print(colorama.Fore.RED + andrew_mistele)
    sleep(2.5)
    system("cls")
    print(colorama.Fore.MAGENTA + kyle_mistele)
    sleep(2.5)
    system("cls")
    print(colorama.Fore.GREEN + michael_naguib + colorama.Fore.WHITE)
    colorama.deinit()
    sleep(2.5)
    system("cls")

def run_plain_credits():
    system("cls")
    print(developed_by)
    sleep(2.5)
    system("cls")
    print(andrew_mistele)
    sleep(2.5)
    system("cls")
    print(kyle_mistele)
    sleep(2.5)
    system("cls")
    print(michael_naguib)
    sleep(2.5)
    system("cls")