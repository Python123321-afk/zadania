from colorama import Fore
from Task Manager import TaskManager
choose=1
manager=TaskManager()
while choose!=5:
    print("wybierz opcje")
    print(Fore.RED +"1. "+ Fore.WHITE+"dodaj zadanie" )
    print(Fore.RED +"2. "+ Fore.WHITE+"usun zadanie" )
    print(Fore.RED +"3. "+ Fore.WHITE+"oznacz zadanie jako zrobione" )
    print(Fore.RED +"4. "+ Fore.WHITE+"wyswietl liste zadan" )    
    print(Fore.RED +"5. "+ Fore.WHITE+"wyjdz" )
    choose=int(input())
    if 1==choose:
        title=input("podaj nazwe zadania : ")
        description=input("podaj opis zadania : ")
        manager.add_tasks(title,description)
    elif 4==choose:
        manager.display_tasks()
    elif 2==choose:
        title=input("podaj nazwe zadania ktore chcesz usunac : ")
        manager.remove_task(title)
    elif 3==choose:
        title=input("podaj nazwe zadania ktorego chcesz zmienic status : ")
        for i in manager.tasks:
            if title==i.title:
                i.mark_as_done()


    


