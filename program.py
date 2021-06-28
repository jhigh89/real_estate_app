import os
import csv
from data_types import Purchase
import statistics

path = "C:\\Repos\\real_estate_app\\data\\SacramentoRealEstateTranscations2008.csv"

def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)

def print_header():
    print(f"{'*' * 50}")
    print(f"{'*' * 10} Real Estate Data Mining App {'*' * 11}")
    print(f"{'*' * 50} \n")

def get_data_file():
    base_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_folder, 'data', 'SacramentoRET2008.csv')

def load_file(filename):
    with open(filename,'r',encoding="utf-8") as file:

        reader = csv.DictReader(file)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        
        return purchases

        # header = file.readline().strip()
        # reader = csv.reader(file)
        # for row in reader:
        #     print(row)

def load_file_basic(filename):
    with open (filename, 'r', encoding="utf-8") as file:
        header = file.readline().strip()
        print('found header: ' + header)

        lines = []
        for line in file:
            line_data = line.strip().split(',')
            lines.append(line_data)

        print(lines[:3])

def get_price(p):
    return p.price

def query_data(data: list[Purchase]):

    data.sort(key=lambda p: p.price)

    
    high_purchase = data[-1]
    print(f"The most expensive house cost: ${high_purchase.price:.2f}. It contained {high_purchase.beds} bedrooms and {high_purchase.baths} bathrooms.")
    # least expensive house?
    low_purchase = data[0]
    print(f"The least expensive house cost: ${low_purchase.price:.2f}. It contained {low_purchase.beds} bedrooms and {low_purchase.baths} bathrooms.")

    prices = [
        p.price # projection or items
        for p in data # the set to process
    ]

    ave_price = statistics.mean(prices)
    print(f"The average home price was ${ave_price:.2f}.")

    prices = [
        p # projection or items
        for p in data # the set to process
        if p.beds == 2 # test / condition
    ]

    ave_2b_price = statistics.mean(p.price for p in prices)
    ave_2b_bath = statistics.mean(p.baths for p in prices)
    ave_2b_sqft = statistics.mean(p.sq__ft for p in prices)
    print(f"Average 2 bedroom house was ${ave_2b_price:.2f}, baths={ave_2b_bath:.2f}, sqft={ave_2b_sqft:.2f}.")

def announce(item, msg):
    print(f"Pulling item {item} for {msg}")
    return item
    

if __name__ == '__main__':
    main()