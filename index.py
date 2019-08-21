from flask import Flask, render_template, request,redirect
import requests
from lxml import etree
from qq_music import get_music

app = Flask(__name__)


@app.route('/my_music', methods=("POST", "GET"))
def my_music():
    if request.method == "GET":
        return render_template('get_music.html')
    else:
        music_name = request.form.get('music_name')
        url = get_music(music_name)
        return redirect(url)


# @app.route('/get_music', methods=("POST", "GET"))
# def get_music():
#     if request.method == "GET":
#         music_name = request.args.get('music_name')
#
#         url = 'https://music.163.com/#/search/m/?id=13702610&type=1&s='+music_name
#
#         # 外链 这里的外链是在括号里面放入音乐后获得的链接
#         base_url = "https://link.hhtjim.com/163/"
#         dic = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
#
#         # # 请求
#         result = requests.get(url, headers=dic).text
#         print(result)
#         # # 筛选数据
#         # dom = etree.HTML(result)
#         # ids = dom.xpath('//a[contains(@href,"song?")]/@href')
#         #
#         # # 遍历
#         # for son_id in ids:
#         #     count_id = son_id.strip('/song?id=')
#         #     if ('$' in count_id) == False:
#         #         song_url = base_url + '%s'%count_id+'.mp3'
#         #         return song_url
#         return 'abc'


if __name__ == '__main__':
    app.run('192.168.16.36', 9001)

