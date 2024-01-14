# konvereensi satuan temperature

# program konverensi celcius ke satuan yang lain

print("\nPROGRAM KONVERENSI TEMPERATURE\n")

celcius = float(input("masukan angka celcius : "))
print('suhu adalah',celcius,'celcius')

# reamur
reamur = 4/5*celcius
print("suhu dalam reamur =",reamur,"reamur")

# fahrenheit
fahrenheit=((9/5)*celcius) + 32
print("suhu dalam fahrenheit =",fahrenheit,"fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin =",kelvin,"kelvin")