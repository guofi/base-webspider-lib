import csv

"""
write
a:追加写入
w:覆盖写
"""


def fun():
    with open('data.csv', 'w', newline='', encoding="utf-8") as csvfile:
        # writer = csv.writer(csvfile, delimiter=' ')
        # writer.writerow(['id', 'name', 'age'])
        # writer.writerow(['10001', 'Mike', 20])
        # writer.writerow(['10002', 'Bob', 22])
        # writer.writerow(['10003', 'Jordan', 21])
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
        writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
        writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})


"""
"""
if __name__ == '__main__':
    fun()
