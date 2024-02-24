
login = "user"
password = "123"
money = 2000

def border(type_of_symbol):
    if(type_of_symbol == '-'):
        print("----------------------------------------")
    if(type_of_symbol == '!'):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def list():
    print("WYBIERZ DZIALANIE")
    print("1.STAN KONTA")
    print("2.WYPLATA GOTOWKI")
    print("3.WPLAC GOTOWKE")
    print("4.WYLOGOWANIE")
    border('-')
  
def exit():
    input("NACISNIJ DOWOLNY KLAWISZ ABY WYJSC")

def auth(log, passwd):
    return login == log and password == passwd

def change(value, operation):
    global money;
    if(operation == "2"):
        money+=value
    else:
        money-=value
    print("OPERACJA UDANA")

def addMoney(value):
    global money;
    money+=value
    print("OPERACJA UDANA")

def show():
    print("STAN KONTA", money, sep=":")

def validate(value):
    try:
        value = int(value)
    except:
        print("NIEPRAWIDLOWA WARTOSC")
        return False
    return True

def session():
    print("BANK")
    print("LOGOWANIE")
    border('-')
    available_try = 3
    while(available_try > 0):
        log = input("PODAJ LOGIN : ")
        passwd = input("PODAJ HASLO : ")
        if(auth(log, passwd) == False):
            border('!')
            available_try-=1
            if(available_try == 0):
                print("BLOKADA")
                border('!')
                return 
            print("LOGWANIE NIEUDANE POZOSTALO CI", available_try, "PROB", sep=' ')
            border('!')
        else:
            print("LOGOWANIE POPRAWNE")
            available_try = 0
    user_decision = 0
    while(user_decision != "4"):
        border('-')
        list()
        user_decision = input("WYBIERZ : ")
        if(validate(user_decision)):
            if(user_decision == "1"):
                show()
                exit()
            if(user_decision == '2' or user_decision == '3'):
                num = input("WPISZ KWOTE")
                if(validate(num)):
                    change(int(num), user_decision)
                exit()
            if(user_decision == "4"):
                print("ZEGNAJ")
        else:
            border('!')
            print("NIEPRAWIDLOWA WARTOSC")
            border('!')
session()
    





