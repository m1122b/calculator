
import logging

logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s %(message)s', 
                    #filename="logfile2.log"
                    )


if __name__ == "__main__":

    print("\n")

    numbers_str = input("Podaj składniki działań oddzielone przecinkiem: ")
    #numbers_str = "2,4,6,7,8"
    logging.debug(f"składniki działań (numbers_str) : {numbers_str} i typ {type(numbers_str)}")
    
    print("\n")

    mynumbers = numbers_str.split(',')
    logging.debug(f"    : {mynumbers} , {len(mynumbers)} i typ {type(mynumbers)} i {type(mynumbers[0])}")

    print("\n")

    mynumbers_int = []
    mynumbers_sum = 0
    mynumbers_multi = 1

    for i in range(len(mynumbers)):

        print("\n")

        mynumbers_int.append(int(mynumbers[i]))
        logging.debug(f"    : {mynumbers_int} i typ {type(mynumbers_int)} i {type(mynumbers_int[i])}")

        print("\n")

        mynumbers_sum = mynumbers_sum + mynumbers_int[i]
        logging.debug(f"    : {mynumbers_sum} i typ {type(mynumbers_sum)} ")

        mynumbers_multi = mynumbers_multi * mynumbers_int[i]
        logging.debug(f"    : {mynumbers_multi} i typ {type(mynumbers_multi)} ")

    print("\n")

    
