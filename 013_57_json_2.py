import json

"""
dump  
中文需要：指定参数 ensure_ascii 为 False
"""


def fun():
    data = [{
        'name': 'Bob',
        'gender': 'male',
        'birthday': '1992-10-18'
    }]
    # with open('data.json', 'w') as file:
    with open('data.json', 'w', encoding='utf-8') as file:
        # file.write(json.dumps(data))
        file.write(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    fun()
