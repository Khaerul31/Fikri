def celcius_ke_fahrenheit(celcius):
    return(celcius* 9/5) + 32

def fahrenheit_ke_celcius(fahrenheit) : 
    return(fahrenheit -32) * 5/9

def main():
    print("konversi suhu")
    print("1. fahrenheit ke celcius")
    print("2. celcius ke fahrenheit")

    pilihan = input(" pilih (1/2) ")

    if pilihan == '1' :
        celcius = float(input("masukan suhu dalam celcius"))
        fahrenheit = celcius_ke_fahrenheit(celcius)
        print(f"{celcius}derajatC = {fahrenheit}derajatF")
    elif pilihan == '2':
        fahrenheit = float(input(" masukan suhu dalam fahrenheit"))
        celcius = fahrenheit_ke_celcius(fahrenheit)
        print(f"{fahrenheit}derajatF = {celcius}derajatC")
    else:
        print("pilihan tidak valid")

if __name__ == "__main__" : main()