import requests
from lxml import etree

url = 'https://www.shuzhaige.com/xuezhonghandaoxing/148033.html';
xiaoshuo = '雪中悍刀行.txt'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36 Edg/134.0.0.0'
}

while True:
    print(url)
    reps = requests.get(url, headers=headers)
    reps.encoding = 'utf-8'

    e = etree.HTML(reps.text)

    title = e.xpath('//div/h1')[0].text

    text_str = '\n'.join([x.text for x in e.xpath('//div/p')])

    url = e.xpath('//*[@id="content"]/div/ul/li[2]/a/@href')[0]

    with open(xiaoshuo, 'a', encoding='utf-8') as f:
        f.write(title + '\n\n' + text_str + '\n')
