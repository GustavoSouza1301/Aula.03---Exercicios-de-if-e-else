time1 = input(f"Primerio Time")
gtime1 = int(input(f"Quantidade de gol do {time1}?"))
time2 = input("Segundo Time")
gtime2 = int(input(f"Quantidade de gol do {time2}?"))

if gtime1 == gtime2:
    print(f"Empate de {gtime1}x{gtime2}")
else:
    if gtime1 > gtime2:
        print(f"Vitória do {time1} de {gtime1}x{gtime2}")
    else:
        print(f"Vitória do {time2} de {gtime2}x{gtime1}")
