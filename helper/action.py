def avg_price(dimonds):
    from app import Dimond
    avg_prices = []
    for diamond in dimonds:
        avg_prices.append(float(diamond[Dimond.price.value]))
    total = sum(avg_prices)
    avg = total / len(avg_prices)
    print(f'The average price is {avg:.2f}')
    

        


def most_expensive(dimonds):
    from app import Dimond
    max_price = 0
    for diamond in dimonds:
        price = float(diamond[Dimond.price.value])
        if price > max_price:
            max_price = price
    print(f'The most expensive diamond costs ${max_price:.2f}')


    
        
def amount_ideal_dimonds():
    pass

def dimonds_colors():
    pass
def preimum_dimond_median():
    pass
def avg_carat_per_cut():
    pass
