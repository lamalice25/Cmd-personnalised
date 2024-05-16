import os

running = True



while running:
    uninstall_package_name = input('Please enter a package to unintall im : ')

    uninstall_package_node = os.system("pip uninstall "+uninstall_package_name)
    
        
    stoping_questions = input('If you are finish you can choice to write (cls) and if not finish you write (con) : ')
    
    if stoping_questions == "cls":
        running = False
    
    elif stoping_questions == "con":
        running = True
        