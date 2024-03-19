import json
import re

"""

{'index': '1', 'image': 'https://p0.pipi.cn/mmdb/d2dad59253751bd236338fa5bd5a27c710413.jpg?imageView2/1/w/160/h/220', 'title': '我不是药神', 'actor': '徐峥,周一围,王传君', 'time': '2018-07-05', 'score': '9.6'}
{'index': '2', 'image': 'https://p0.pipi.cn/mmdb/fb7386020fa51b0fafcf3e2e3a0bbe694d17d.jpg?imageView2/1/w/160/h/220', 'title': '肖申克的救赎', 'actor': '蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿', 'time': '1994-09-10(加拿大)', 'score': '9.5'}
{'index': '3', 'image': 'https://p0.pipi.cn/mmdb/d2dad592c7e7e1d2365bf1b63cd25951b722b.jpg?imageView2/1/w/160/h/220', 'title': '海上钢琴师', 'actor': '蒂姆·罗斯,比尔·努恩 ,克兰伦斯·威廉姆斯三世', 'time': '2019-11-15', 'score': '9.3'}
{'index': '4', 'image': 'https://p0.pipi.cn/mmdb/d2dad59253751b230f21f0818a5bfd4d8679c.jpg?imageView2/1/w/160/h/220', 'title': '绿皮书', 'actor': '维果·莫腾森,马赫沙拉·阿里,琳达·卡德里尼', 'time': '2019-03-01', 'score': '9.5'}
{'index': '5', 'image': 'https://p0.pipi.cn/mmdb/fb7386beddd338537c8ea3bb80d25a9078b13.jpg?imageView2/1/w/160/h/220', 'title': '霸王别姬', 'actor': '张国荣,张丰毅,巩俐', 'time': '1993-07-26', 'score': '9.4'}
{'index': '6', 'image': 'https://p0.pipi.cn/mmdb/d2dad592c7e7e1d2367a3507befaed31a5903.jpg?imageView2/1/w/160/h/220', 'title': '美丽人生', 'actor': '罗伯托·贝尼尼,朱斯蒂诺·杜拉诺,赛尔乔·比尼·布斯特里克', 'time': '2020-01-03', 'score': '9.3'}
{'index': '7', 'image': 'https://p0.pipi.cn/mmdb/d2dad592c7e7e13ba3ddd25677b4d70fc45fa.jpg?imageView2/1/w/160/h/220', 'title': '这个杀手不太冷', 'actor': '让·雷诺,加里·奥德曼,娜塔莉·波特曼', 'time': '1994-09-14(法国)', 'score': '9.4'}
{'index': '8', 'image': 'https://p0.pipi.cn/mmdb/d2dad592b125bfc9fd300b8a46169f8008efb.jpg?imageView2/1/w/160/h/220', 'title': '星际穿越', 'actor': '马修·麦康纳,安妮·海瑟薇,杰西卡·查斯坦', 'time': '2014-11-12', 'score': '9.3'}
{'index': '9', 'image': 'https://p0.pipi.cn/mmdb/d2dad5925372ffd7c387a9d01bddad81625c3.jpg?imageView2/1/w/160/h/220', 'title': '小偷家族', 'actor': '中川雅也,安藤樱,松冈茉优', 'time': '2018-08-03', 'score': '8.1'}
{'index': '10', 'image': 'https://p0.pipi.cn/mmdb/d2dad592b122ff8d3387a93ccab6036f616c1.jpg?imageView2/1/w/160/h/220', 'title': '怦然心动', 'actor': '玛德琳·卡罗尔,卡兰·麦克奥利菲,艾丹·奎因', 'time': '2010-07-26(美国)', 'score': '8.9'}



"""


def parse_one_page(html):
    regex = '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>'
    pattern = re.compile(regex, re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {'index': item[0],
               'image': item[1],
               'title': item[2].strip(),
               'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
               'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
               'score': item[5].strip() + item[6].strip()}


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')  # ensure_ascii 参数为 False，这样可以保证输出结果是中文形式而不是 Unicode 编码


def main():
    html = '''
<!DOCTYPE html>

<!--[if IE 8]><html class="ie8"><![endif]-->
<!--[if IE 9]><html class="ie9"><![endif]-->
<!--[if gt IE 9]><!--><html><!--<![endif]-->
<head>
  <title>TOP100榜 - 猫眼电影 - 一网打尽好电影</title>
  
  <link rel="dns-prefetch" href="//p0.meituan.net"  />
  <link rel="dns-prefetch" href="//p1.meituan.net"  />
  <link rel="dns-prefetch" href="//ms0.meituan.net" />
  <link rel="dns-prefetch" href="//ms1.meituan.net" />
  <link rel="dns-prefetch" href="//lx.meituan.net"/>
  <link rel="dns-prefetch" href="//lx1.meituan.net"/>
  <link rel="dns-prefetch" href="//plx.meituan.com"/>

  
  <meta charset="utf-8">
  <meta name="keywords" content="猫眼电影,电影排行榜,热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100">
  <meta name="description" content="猫眼电影热门榜单,包括热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100,多维度为用户进行选片决策">
  <meta http-equiv="cleartype" content="yes" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="renderer" content="webkit" />

  <meta name="HandheldFriendly" content="true" />
  <meta name="format-detection" content="email=no" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="viewport" content="width=device-width, initial-scale=1">

  
  <script>"use strict";!function(){var i=0<arguments.length&&void 0!==arguments[0]?arguments[0]:"_Owl_",n=window;n[i]||(n[i]={isRunning:!1,isReady:!1,preTasks:[],dataSet:[],use:function(i,t){this.isReady&&n.Owl&&n.Owl[i](t),this.preTasks.push({api:i,data:[t]})},add:function(i){this.dataSet.push(i)},run:function(){var t=this;if(!this.isRunning){this.isRunning=!0;var i=n.onerror;n.onerror=function(){this.isReady||this.add({type:"jsError",data:arguments}),i&&i.apply(n,arguments)}.bind(this),(n.addEventListener||n.attachEvent)("error",function(i){t.isReady||t.add({type:"resError",data:[i]})},!0)}}},n[i].run())}();</script>
  <script>
  cid = "c_wx6zb55";
  ci = 30;
val = {"subnavId":4};    window.system = {};

  window.openPlatform = '';
  window.openPlatformSub = '';
  window.$mtsiFlag = '0';
  window.NODE_ENV = 'production';

  </script>
  <link rel="stylesheet" href="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/common.118924d9.css"/>
<link rel="stylesheet" href="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/board-index.92a06072.css"/>
  <script crossorigin="anonymous" src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/stat.b4e55d45.js"></script>
  <script>if(window.devicePixelRatio >= 2) { document.write('<link rel="stylesheet" href="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image-2x.8ba7074d.css"/>') }</script>
  <style>
    @font-face{font-family: "mtsi-font";src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/432017e7.eot");src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/432017e7.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/432017e7.woff");}
    .stonefont {
      font-family: mtsi-font;
    }
  </style>
  <script>
  var _hmt = _hmt || [];
  (function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?703e94591e87be68cc8da0da7cbd0be2";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
  })();
  </script>
</head>
<body>


<div class="header">
  <div class="header-inner">
          <a href="//www.maoyan.com" class="logo" data-act="icon-click">猫眼电影</a>
        <div class="city-container" data-val="{currentcityid:30 }">
            <div class="city-selected">
                <div class="city-name">
                  深圳
                  <span class="caret"></span>
                </div>
            </div>
            <div class="city-list" data-val="{ localcityid: 30 }">
                <div class="city-list-header">定位城市：<a class="js-geo-city" data-ci="30">深圳</a></div>
            </div>
        </div>


        <div class="nav">
            <div><a href="/" data-act="home-click"  >首页</a></div>
            <div><a href="/films" data-act="movies-click" >电影</a></div>
            <div><a href="/cinemas" data-act="cinemas-click" >影院</a></div> 
            <div><a href="http://www.gewara.com">演出</a></div>
            <!-- <div><a href="/dramas" data-act="TVdramas-click" >电视剧</a></div> -->
            <!-- <div><a href="/board" data-act="board-click"  class="active" >榜单</a></div> -->
            <!--             <div><a href="/news" data-act="hotNews-click" >热点</a></div>
 -->
            <!-- <div><a href="/edimall"  >商城</a></div> -->
        </div>

        <div class="user-info">
            <div class="user-avatar J-login">
              <img src="https://p0.meituan.net/movie/7dd82a16316ab32c8359debdb04396ef2897.png">
              <span class="caret"></span>
              <ul class="user-menu no-login-menu">
                <li><a href="javascript:void 0">登录</a></li>
              </ul>
            </div>
        </div>

        <form style="display: none;" action="/query" target="_blank" class="search-form" data-actform="search-click">
            <input name="kw" class="search" type="search" maxlength="32" placeholder="找影视剧、影人、影院" autocomplete="off">
            <input class="submit" type="submit" value="">
        </form>

        <div class="app-download">
          <a href="/app" target="_blank">
            <span class="iphone-icon"></span>
            <span class="apptext">APP下载</span>
            <span class="caret"></span>
            <div class="download-icon">
                <p class="down-title">扫码下载APP</p>
                <p class='down-content'>选座更优惠</p>
            </div>
          </a>
        </div>
    
  </div>
</div>
<div class="header-placeholder"></div>

<div class="subnav">
  <ul class="navbar">
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:7}"
          href="/board/7"
      >热映口碑榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:6}"
          href="/board/6"
      >最受期待榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:1}"
          href="/board/1"
      >国内票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:2}"
          href="/board/2"
      >北美票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:4}"
          data-state-val="{subnavId:4}"
          class="active" href="javascript:void(0);"
      >TOP100榜</a>
    </li>
  </ul>
</div>


    <div class="container" id="app" class="page-board/index" >

<div class="content">
    <div class="wrapper">
        <div class="main">
            <p class="update-time">2024-03-19<span class="has-fresh-text">已更新</span></p>
            <p class="board-content">榜单规则：将猫眼电影库中的经典影片，按照评分和评分人数从高到低综合排序取前100名，每天上午10点更新。相关数据来源于“猫眼电影库”。</p>
            <dl class="board-wrapper">
                <dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1200486" title="我不是药神" class="image-link" data-act="boarditem-click" data-val="{movieId:1200486}">
      <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.pipi.cn/mmdb/d2dad59253751bd236338fa5bd5a27c710413.jpg?imageView2/1/w/160/h/220" alt="我不是药神" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1200486" title="我不是药神" data-act="boarditem-click" data-val="{movieId:1200486}">我不是药神</a></p>
        <p class="star">
                主演：徐峥,周一围,王传君
        </p>
<p class="releasetime">上映时间：2018-07-05</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">6</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/1297" title="肖申克的救赎" class="image-link" data-act="boarditem-click" data-val="{movieId:1297}">
      <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.pipi.cn/mmdb/fb7386020fa51b0fafcf3e2e3a0bbe694d17d.jpg?imageView2/1/w/160/h/220" alt="肖申克的救赎" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1297" title="肖申克的救赎" data-act="boarditem-click" data-val="{movieId:1297}">肖申克的救赎</a></p>
        <p class="star">
                主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿
        </p>
<p class="releasetime">上映时间：1994-09-10(加拿大)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-3">3</i>
    <a href="/films/1292" title="海上钢琴师" class="image-link" data-act="boarditem-click" data-val="{movieId:1292}">
      <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.pipi.cn/mmdb/d2dad592c7e7e1d2365bf1b63cd25951b722b.jpg?imageView2/1/w/160/h/220" alt="海上钢琴师" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1292" title="海上钢琴师" data-act="boarditem-click" data-val="{movieId:1292}">海上钢琴师</a></p>
        <p class="star">
                主演：蒂姆·罗斯,比尔·努恩 ,克兰伦斯·威廉姆斯三世
        </p>
<p class="releasetime">上映时间：2019-11-15</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">3</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-4">4</i>
    <a href="/films/1206605" title="绿皮书" class="image-link" data-act="boarditem-click" data-val="{movieId:1206605}">
      <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.pipi.cn/mmdb/d2dad59253751b230f21f0818a5bfd4d8679c.jpg?imageView2/1/w/160/h/220" alt="绿皮书" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1206605" title="绿皮书" data-act="boarditem-click" data-val="{movieId:1206605}">绿皮书</a></p>
        <p class="star">
                主演：维果·莫腾森,马赫沙拉·阿里,琳达·卡德里尼
        </p>
<p class="releasetime">上映时间：2019-03-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-5">5</i>
    <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
      <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.pipi.cn/mmdb/fb7386beddd338537c8ea3bb80d25a9078b13.jpg?imageView2/1/w/160/h/220" alt="霸王别姬" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
        <p class="star">
                主演：张国荣,张丰毅,巩俐
        </p>
<p class="releasetime">上映时间：1993-07-26</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">4</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-6">6</i>
    <a href="/films/1303" title="美丽人生" class="image-link" data-act="boarditem-click" data-val="{movieId:1303}">
      <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.pipi.cn/mmdb/d2dad592c7e7e1d2367a3507befaed31a5903.jpg?imageView2/1/w/160/h/220" alt="美丽人生" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1303" title="美丽人生" data-act="boarditem-click" data-val="{movieId:1303}">美丽人生</a></p>
        <p class="star">
                主演：罗伯托·贝尼尼,朱斯蒂诺·杜拉诺,赛尔乔·比尼·布斯特里克
        </p>
<p class="releasetime">上映时间：2020-01-03</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">3</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-7">7</i>
    <a href="/films/4055" title="这个杀手不太冷" class="image-link" data-act="boarditem-click" data-val="{movieId:4055}">
      <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.pipi.cn/mmdb/d2dad592c7e7e13ba3ddd25677b4d70fc45fa.jpg?imageView2/1/w/160/h/220" alt="这个杀手不太冷" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/4055" title="这个杀手不太冷" data-act="boarditem-click" data-val="{movieId:4055}">这个杀手不太冷</a></p>
        <p class="star">
                主演：让·雷诺,加里·奥德曼,娜塔莉·波特曼
        </p>
<p class="releasetime">上映时间：1994-09-14(法国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">4</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-8">8</i>
    <a href="/films/78341" title="星际穿越" class="image-link" data-act="boarditem-click" data-val="{movieId:78341}">
      <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.pipi.cn/mmdb/d2dad592b125bfc9fd300b8a46169f8008efb.jpg?imageView2/1/w/160/h/220" alt="星际穿越" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/78341" title="星际穿越" data-act="boarditem-click" data-val="{movieId:78341}">星际穿越</a></p>
        <p class="star">
                主演：马修·麦康纳,安妮·海瑟薇,杰西卡·查斯坦
        </p>
<p class="releasetime">上映时间：2014-11-12</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">3</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-9">9</i>
    <a href="/films/1216365" title="小偷家族" class="image-link" data-act="boarditem-click" data-val="{movieId:1216365}">
      <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.pipi.cn/mmdb/d2dad5925372ffd7c387a9d01bddad81625c3.jpg?imageView2/1/w/160/h/220" alt="小偷家族" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1216365" title="小偷家族" data-act="boarditem-click" data-val="{movieId:1216365}">小偷家族</a></p>
        <p class="star">
                主演：中川雅也,安藤樱,松冈茉优
        </p>
<p class="releasetime">上映时间：2018-08-03</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-10">10</i>
    <a href="/films/46818" title="怦然心动" class="image-link" data-act="boarditem-click" data-val="{movieId:46818}">
      <img src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.pipi.cn/mmdb/d2dad592b122ff8d3387a93ccab6036f616c1.jpg?imageView2/1/w/160/h/220" alt="怦然心动" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/46818" title="怦然心动" data-act="boarditem-click" data-val="{movieId:46818}">怦然心动</a></p>
        <p class="star">
                主演：玛德琳·卡罗尔,卡兰·麦克奥利菲,艾丹·奎因
        </p>
<p class="releasetime">上映时间：2010-07-26(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">9</i></p>        
    </div>

      </div>
    </div>

                </dd>
            </dl>

        </div>
            <div class="pager-main">
                
  
  <ul class="list-pager">



  
      <li class="active">
    <a class="page_1"
      href="javascript:void(0);" style="cursor: default"
  >1</a>

</li>
  <li >
    <a class="page_2"
      href="?offset=10"
  >2</a>

</li>
  <li >
    <a class="page_3"
      href="?offset=20"
  >3</a>

</li>
  <li >
    <a class="page_4"
      href="?offset=30"
  >4</a>

</li>
  <li >
    <a class="page_5"
      href="?offset=40"
  >5</a>

</li>

    <li class="sep">...</li>
      <li >
    <a class="page_10"
      href="?offset=90"
  >10</a>

</li>

  

<li>  <a class="page_2"
      href="?offset=10"
  >下一页</a>
</li>
</ul>


            </div>
    </div>
</div>

    </div>

<div class="footer">
  <p class="friendly-links">
    关于猫眼 :
    <a href="https://ir.maoyan.com/Company-Information">关于我们</a>
    <span></span>
    <a href="https://ir.maoyan.com/Board-Members">董事会成员</a>
    <span></span>
    <a href="https://ir.maoyan.com">投资者关系</a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    友情链接 :
    <a href="http://www.meituan.com" data-query="utm_source=wwwmaoyan">美团网</a>
    <span></span>
    <a href="http://www.gewara.com" data-query="utm_source=wwwmaoyan">格瓦拉</a>
    <span></span>
    <a href="http://i.meituan.com/client" data-query="utm_source=wwwmaoyan">美团下载</a>
    <span></span>
    <a href="https://www.huanxi.com" data-query="utm_source=maoyan_pc">欢喜首映</a>
  </p>
  <p class="friendly-links">
    商务合作邮箱：v@maoyan.com
    客服电话：10105335
    违法和不良信息/涉未成年人有害信息举报电话：4006018900
  </p>
  <p class="friendly-links">
    用户举报/涉未成年人有害信息举报邮箱：tousujubao@meituan.com
    舞弊线索举报邮箱：wubijubao@maoyan.com
  </p>
  <p class="friendly-links  credentials">
    <a href="/about/licence/1" target="_blank">中华人民共和国增值电信业务经营许可证 京B2-20190350</a>
    <span></span>
    <a href="/about/licence/4" target="_blank">营业性演出许可证 京演（机构）（2019）4094号</a>
  </p>
  <p class="friendly-links  credentials">
    <a href="/about/licence/3" target="_blank">广播电视节目制作经营许可证 （京）字第08478号</a>
    <span></span>
    <a href="/about/licence/2" target="_blank">网络文化经营许可证 京网文（2022）1334-041号 </a>
  </p>
  <p class="friendly-links  credentials">
    <a href="/about/licence/6" target="_blank">艺术品经营单位备案证明  京东艺（2022）0095号 </a>
  </p>
  <p class="friendly-links  credentials">
    <a href="/rules/agreement" target="_blank">猫眼用户服务协议 </a>
    <span></span>
    <a href="/rules/rule" target="_blank">猫眼平台交易规则总则 </a>
    <span></span>
    <a href="/rules/privacy" target="_blank">隐私政策 </a>
  </p>
  <p class="friendly-links  credentials">
    <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102003232">京公网安备
      11010102003232号</a>
    <span></span>
    <a href="http://beian.miit.gov.cn/">京ICP备16022489号-1</a>
  </p>
  <p>北京猫眼文化传媒有限公司</p>
  <p>
    &copy;<span class="my-footer-year">2016</span>
    猫眼电影 www.maoyan.com</p>
  <div class="certificate">
    <a href="http://sq.ccm.gov.cn:80/ccnt/sczr/service/business/emark/toDetail/350CF8BCA8416C4FE0530140A8C0957E">
      <img src="https://p0.meituan.net/moviemachine/e54374ccf134d1f7b2c5b075a74fca525326.png" />
    </a>
    <a href="/about/licence/5" target="_blank">
      <img src="https://pipi-p0-1251246104.cos.ap-beijing.myqcloud.com/rock/prod/common/media/1706097114317-license.png" />
    </a>
    <a href="https://www.12377.cn">
      <img src="https://p0.meituan.net/scarlett/3cd2a9b7dc179531d20d27a5fd686e783787.png" />
    </a>
  </div>
</div>

    <script crossorigin="anonymous" src="//www.dpfile.com/app/owl/static/owl_1.7.11.js"></script>
    <script>
      Owl.start({
        project: 'com.sankuai.myfe.mywww.media',
        pageUrl: location.href.split('?')[0].replace(/\/\d+/g, '/:id'),
        devMode: false
      })
    </script>
    <!--[if IE 8]><script crossorigin="anonymous" src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/es5-shim.bbad933f.js"></script><![endif]-->
    <!--[if IE 8]><script crossorigin="anonymous" src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/es5-sham.221f40f5.js"></script><![endif]-->
    <script crossorigin="anonymous" src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/common.665aebb1.js"></script>
<script crossorigin="anonymous" src="//s3.meituan.net/static-prod01/com.sankuai.movie.fe.mywww-files/board-index.faf8d1ca.js"></script>
    <script src="//lx.meituan.net/lx.js" type="text/javascript" charset="utf-8" async></script>
</body>
</html>
    '''

    parse_one_page(html)
    for item in parse_one_page(html):
        write_to_file(item)


"""
获取首页的电影列表 (单页内容写入文本文件)

"""
main()
