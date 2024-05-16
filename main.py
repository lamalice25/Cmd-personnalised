import os
import datetime
import webbrowser

heure = datetime.datetime.now().strftime("%H:%M")

running = True

os.system('title cmd personnalised')

   
print("Bienvenue sur l'interface d'utilisations de ce nouveau cmd-powershell personalised")

while running:
    commande_name = 1
    
    
    command = input(f'{heure} ----> ')
    
    if command == "google":
        os.system('start chrome')
        commande_name = 2
    
    if command == "firefox":
        os.system('start firefox')
        commande_name = 2

    if command == "opera":
        os.system('start opera')
        commande_name = 2
       
    if command == "install package":
        os.system('start installer_package_py.exe')
        commande_name = 2
    
    if command == "cmd":
        webbrowser.open('https://sites.google.com/view/cmd-personnalised/accueil')
        commande_name = 2
    
    if command == "powershell":
        webbrowser.open('https://sites.google.com/view/cmd-personnalised/accueil')
        commande_name = 2
    
    
    if command == "delete package":
        os.system('start delete_package_py.exe')
        commande_name = 2
    

    if command == "stop":
        running = False
        commande_name = 2
        
        
    if command == "filius":
        os.system('start filius')
        commande_name = 2
        
    if command == "help2":
        print("nslookup : résout un nom d'hote en adresse IP\n")
        print("arp : Affiche la table (ARP)\n")
        print("netstat : Affiche la liste des connexions en cours")
        print("install package : install le package demander")
        print('delete package : supprime les packages demander')
        
        commande_name = 2
    
    if command == "color":
       # On donne les couleurs qui sont disponible en les affichant séparément 
       
        print('voici la palette de couleur disponible \n')
        
        print("---"*9)
        
        print("color vert")
        print("color noir") 
        print("color bleu") 
        print("color bleu gris")
        print("color rouge")  
        print("color violet")  
        print("color jaune")  
        print("color gris")  
        print("color bleu clair")  
        print("color vert clair")
        print("color cyan")
        print("color rouge clair")
        print("color violet clair")
        print("color jaune clair")
        print("color blanc brillant")
        
        commande_name = 2
       
    if command == "color vert":
        os.system('color 2')
        commande_name = 2
        
    if command == "color noir":
        os.system('color 0')
        commande_name = 2
    if command == "color bleu":
       os.system("color 1")
       commande_name = 2
       
    if command == "color bleu gris":
        os.system('color 3')
        commande_name = 2
        
    if command == "color rouge":
        os.system('color 4')
        commande_name = 2
        
    if command == 'color violet': 
        os.system('color 5')
        commande_name = 2
    
    if command == 'color jaune':
        os.system('color 6')
        commande_name = 2
        
    if command == "reset color":
        os.system('color 7')
        commande_name = 2
        
    if command == "color gris":
        os.system('color 8')
        commande_name = 2
        
    if command == "color bleu clair":
        os.system('color 9')
        commande_name = 2
    
    if command == "color vert clair":
        os.system('color A')
        commande_name = 2
    
    if command == "color cyan":
        os.system('color B')
        commande_name = 2
        
    if command == "color rouge clair":
        os.system('color C')
        commande_name = 2
    
    if command == "color violet clair":
        os.system('color D')
        commande_name = 2
        
    if command == "color jaune clair":
        os.system('color E')
        commande_name = 2
    
    if command == "color blanc brillant":
        os.system('color F')
        commande_name = 2
        
    if command == "exit":
        running = False
        
    if commande_name == 1:
        os.system(command)