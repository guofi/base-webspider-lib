import csv

"""
read
"""


def fun():
    with open('data.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)


"""
"""
if __name__ == '__main__':
    fun()
