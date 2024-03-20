import json


def fun():
    str = '''
    [{
        "name": "Bob",
        "gender": "male",
        "birthday": "1992-10-18"
    }, {
        "name": "Selina",
        "gender": "female",
        "birthday": "1995-10-18"
    }]
    '''
    print(type(str))
    data = json.loads(str)
    print(
        data)  # [{'name': 'Bob', 'gender': 'male', 'birthday': '1992-10-18'}, {'name': 'Selina', 'gender': 'female',
    # 'birthday': '1995-10-18'}]
    print(type(data))


if __name__ == '__main__':
    fun()
