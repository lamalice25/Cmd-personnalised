import os

running = True



while running:
    name_package = input('Please enter the name package : ')

    os.system('pip install '+name_package)
    
    
    stoping_questions = input('If you are finish you can choice to write (cls) and if not finish you write (con) : ')
    
    if stoping_questions == "cls":
        running = False
    
    elif stoping_questions == "con":
        running = True
    