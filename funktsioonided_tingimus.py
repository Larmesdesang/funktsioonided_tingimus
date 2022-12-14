import re
try:
	print("Tere! Olen sinu uus sõber - Python!")
	i=False
	while not i:
		nimi = input("nimi: ")
		if re.findall(r'\d', nimi)==[]:
			i=True
			print(nimi, ", oi kui ilus nimi!" )
		else: print("kutt kirjuta oma nimi")
	vastus = int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
	if vastus == 1:
		pikkus = int(input("pikkus: "))
		mass = float(input("mass: "))
		indeks = mass /(0.01*pikkus)**2
		if mass>0 and pikkus<250 and pikkus>0 and mass<250:
			print("! Sinu keha indeks on:" ,round(indeks,1))
			if indeks<16:
				print("Tervisele ohtlik alakaal")
			elif indeks>=15 and indeks<19:
				print("Alakaal")
			elif indeks>=19 and indeks<25:
				print("Normaalkaal")
			elif indeks>=25 and indeks<30:
				print("Ülekaal")
			elif indeks>=30 and indeks<35:
				print("Rasvumine")
			elif indeks>=35 and indeks<40:
				print("Tugev rasvumine")
			elif indeks>40:
				print("Tervisele ohtlik rasvumine")
		else:
			print("too much")
			
	else:
		print("Kahju! See on väga kasulik info!")
		print("")
		print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
except:
	print("Error")
