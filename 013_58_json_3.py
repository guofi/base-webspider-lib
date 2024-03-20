import json

"""
read
"""


def fun():
    with open('data.json', 'r') as file:
        str = file.read()
        data = json.loads(str)
        print(data)


"""
[{'name': 'Bob', 'gender': 'male', 'birthday': '1992-10-18'}]
"""
if __name__ == '__main__':
    fun()
