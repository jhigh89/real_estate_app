import os


def main():
    print_header()
    filename = get_data_file()
    print(filename)
    data = load_file(filename)
    print(data)
    query_data(data)

def print_header():
    print(f"{'*' * 50}")
    print(f"{'*' * 10} Real Estate Data Mining App {'*' * 11}")
    print(f"{'*' * 50} \n")

def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')

def load_file(filename):
    return []

def query_data(data):
    pass

if __name__ == '__main__':
    main()