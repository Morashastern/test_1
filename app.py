from enum import Enum
import pandas as pd
import csv
from helper.action import avg_price,amount_ideal_dimonds,avg_carat_per_cut,dimonds_colors,most_expensive,preimum_dimond_median
filename='\test_csv\dimond.csv'
avg_prices=[]
class Menu(Enum):
    most_expensive=1
    avg_price=2
    UPDATE=3
    PRINT=4
    SUM=5
    RESET=6
    EXIT=7
class Dimond(Enum):
    carat=0
    cut=1
    color=2
    clarity=3 
    depth=4
    table=5
    price=6
dimonds=[]
def display_menu():
    for action in Menu:
        print (f'{action.value}-{action.name}')
    return Menu(int(input("choose one option:")))
def load_data(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
             dimonds.append(row)
            
        return(dimonds)



def main():
    while True:
        user_choice=display_menu()
        dimonds=load_data(filename)
        try:
            if user_choice==Menu.most_expensive:most_expensive(dimonds)             
            if user_choice==Menu.avg_price:avg_price(dimonds)
            if user_choice==Menu.PRINT:amount_ideal_dimonds()
            if user_choice==Menu.RESET:dimonds_colors()
            if user_choice==Menu.UPDATE:preimum_dimond_median()
            if user_choice==Menu.EXIT:avg_carat_per_cut()
            if user_choice==Menu.EXIT:exit()


        except Exception as e:
            print("error",e)




if __name__=='__main__':
    main()