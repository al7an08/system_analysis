import csv
import math


def main(csv_str: str):
    reader = csv.reader(csv_str.splitlines(), delimiter=',')
    data = list(reader)
    length = len(data)
    entropy_sum = 0

    for row in data:
        for cell in row:
            cell_value = cell
            if cell_value != '0':
                digit_value = float(cell_value) / (length - 1)
                entropy_sum += -digit_value * math.log2(digit_value)

    return round(entropy_sum, 1)

input_data = "2,0,2,0,0\n0,1,0,0,1\n2,1,0,0,1\n0,1,0,1,1\n0,1,0,1,1"
output = main(input_data)
print(output) #~6.5