from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

'''

containerid         可以发现，它就是 107603 加上用户 id

'''


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo


'''
{'id': '5012880691299523', 'text': '', 'attitudes': 1, 'comments': 0, 'reposts': 1}
{'id': '5009817909330018', 'text': '一只又乖又好看的招财猫 北京', 'attitudes': 7, 'comments': 2, 'reposts': 0}
{'id': '5009815632347393', 'text': '猫咪狂想曲 北京 崔庆才丨静觅的微博视频', 'attitudes': 4, 'comments': 0, 'reposts': 0}
{'id': '5007268665626463', 'text': '面向猫猫编程 崔庆才丨静觅的微博视频', 'attitudes': 7, 'comments': 0, 'reposts': 0}
{'id': '5006866248110639', 'text': '转发微博', 'attitudes': 0, 'comments': 0, 'reposts': 2}
{'id': '5006408536033990', 'text': '转发微博', 'attitudes': 0, 'comments': 0, 'reposts': 0}
{'id': '5005270026030012', 'text': '//@王尼玛:', 'attitudes': 1, 'comments': 1, 'reposts': 0}
{'id': '5005042991499580', 'text': '//@金山://@老刀99:能有工牌戴都不错了，那些再老一点的牛不仅没有工牌还有可能随时被宰（cai ）了//@土味老爹:天天喊辞职，工牌戴的比谁都快//@渣蜀黍:怎么上传我的工作vlog？//@大头和他的朋友们:哈哈哈哈//@酥饼188-:是谁破防了我不说，但是这个场景真的眼熟', 'attitudes': 4, 'comments': 1, 'reposts': 2}
{'id': '5003799390062161', 'text': '', 'attitudes': 0, 'comments': 0, 'reposts': 0}
{'id': '5002161844388701', 'text': '转发微博', 'attitudes': 0, 'comments': 0, 'reposts': 0}
{'id': '4999278390675992', 'text': '转发微博', 'attitudes': 1, 'comments': 0, 'reposts': 4}
{'id': '4997791894210170', 'text': '服了', 'attitudes': 0, 'comments': 0, 'reposts': 0}
{'id': '4977701278715265', 'text': '//@SexFriend:不知道原理，反正管用。', 'attitudes': 1, 'comments': 1, 'reposts': 5}
{'id': '4962172771238026', 'text': '转发微博', 'attitudes': 0, 'comments': 0, 'reposts': 0}
{'id': '4952880811345128', 'text': '转发微博', 'attitudes': 0, 'comments': 0, 'reposts': 1}
{'id': '4952700757216129', 'text': '转发微博', 'attitudes': 1, 'comments': 0, 'reposts': 0}
{'id': '4952699990967581', 'text': '//@梁斌penny:重大信号//@明涛ECON:军公教//@学术大观察://@科技与女性:其实是所有公务员退休金都要腰斩…然后会有30%以上的下岗比例。我从前两年就不推荐考公。', 'attitudes': 2, 'comments': 0, 'reposts': 2}
{'id': '4950198410808975', 'text': '', 'attitudes': 2, 'comments': 1, 'reposts': 0}
'''
if __name__ == '__main__':
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
