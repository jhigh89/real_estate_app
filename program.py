import os

path = "C:\\Repos\\real_estate_app\\data\\SacramentoRealEstateTranscations2008.csv"

def main():
    print_header()
    filename = get_data_file()
    print(filename)
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
    with open (filename, 'r', encoding="utf-8") as file:
        header = file.readline().strip()
        print('found header: ' + header)

        lines = []
        for line in file:
            line_data = line.strip().split(',')
            lines.append(line_data)

        print(lines[:3])

def query_data(data):
    pass

if __name__ == '__main__':
    main()