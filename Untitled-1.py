import random
i = random.randint(0,100)
liczba_tur=0
odp=int(input("wybierz liczbe od 0 do 100"))
while odp != i:
    if odp>i:
        print("ta liczba jest zbyt duza")
    if odp<i:
        print("ta liczba jest za mala")
    if odp>100:
        print("liczba jest wieksza niz 100")
    if odp==i:
        print("brawo zgadles")
    liczba_tur+=1
    odp=int(input("wybierz liczbe od 0 do 100"))
print(f"gratulacje udalo ci sie odgadnac liczbe w turze {liczba_tur}")

