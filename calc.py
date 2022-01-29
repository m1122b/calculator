
import logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s %(message)s', 
                    filename="logfile.log"
                    )





if __name__ == "__main__":

    kind_str = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    logging.info(f"First input (kind_str) : {kind_str} i typ {type(kind_str)}")

    #if (kind_str):
    #    print(f"{kind_str} - To nie liczba!!!!!")


    kind = int(kind_str)

    if kind > 4 or kind < 1:
        print(f" {kind} - To zła decyzja!!!!!!!!")
        logging.debug(f"Wrong result (kind): {kind}")
        exit(1)


    number1_str = input("Podaj składnik 1: ")
    logging.debug(f"First choice (number1): {number1_str}")
    
    number1 = int(number1_str)
    
    number2_str = input("Podaj składnik 2: ")
    logging.debug(f"Second choice (number2): {number2_str}")
    
    number2 = int(number2_str)
    

    if kind == 1:
        print(f"Dodaje {number1} i {number2}.")
        print(f"Wynik to {number1 + number2}.")
        logging.debug(f"Add result (number1 + number2): {number1 + number2}")
    elif kind == 2:
        print(f"Odejmuje {number1} i {number2}.")
        print(f"Wynik to {number1 - number2}.")
        logging.debug(f"Subtraction result (number1 - number2): {number1 - number2}")
    elif kind == 3:
        print(f"Mnoże {number1} i {number2}.")
        print(f"Wynik to {number1 * number2}.")
        logging.debug(f"Multiplication result (number1 * number2): {number1 * number2}")
    elif kind == 4:
        print(f"Dziele {number1} i {number2}.")
        print(f"Wynik to {number1 / number2}.")
        logging.debug(f"Division result (number1 / number2): {number1 / number2}")
    else:
        print(f" {kind} - Nie ta liczba!!!!!!!!")
        logging.debug(f"Wrong result (kind): {kind}")
    
    


    











