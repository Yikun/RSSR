# -*- coding: utf-8 -*-
import pygal
import history
import torrent

from pygal.style import Style

custom_style = Style(
    background='white',
    plot_background='rgba(255, 255, 255, 0.1)',
    foreground='rgba(0, 0, 0, 0.5)',
    foreground_light='rgba(0, 0, 0, 0.7)',
    foreground_dark='rgba(0, 0, 0, 0.3)',
    colors=('rgb(163, 190, 140)',
            'rgb(123, 163, 168)',
            'rgb(130, 192, 175)',
            'rgb(159, 224, 246)',
            'rgb(0, 146, 199)',
            'rgb(91, 144, 191)',
            'rgb(40, 81, 113)',
            'rgb(190, 173, 146)',
            'rgb(243, 90, 74)',
            'rgb(91, 73, 71)',
            'rgb(218, 145, 122)',
            'rgb(242, 156, 156)')
)


def historysvg():
    hsvgpath = "../view/history/"

    h = history.History("../data/history.dat")

    line = pygal.Line(
        width=800, height=400, interpolate='hermite', style=custom_style)
    line.title = u'每月种子下载平均量统计'
    line.x_labels = [u'1月', u'2月', u'3月', u'4月', u'5月',
                     u'6月', u'7月', u'8月', u'9月', u'10月', u'11月', u'12月']
    line.add(u'2012年', h.monthes(2012, None))
    line.add(u'2013年', h.monthes(2013, None))
    line.add(u'2014年', h.monthes(2014, None))
    line.render_to_file(hsvgpath + 'month_ave.svg')

    line = pygal.Line(
        width=800, height=400, interpolate='hermite', style=custom_style)
    line.title = u'每月种子下载累积量统计'
    line.x_labels = [u'起始', u'1月', u'2月', u'3月', u'4月', u'5月',
                     u'6月', u'7月', u'8月', u'9月', u'10月', u'11月', u'12月']
    line.add(u'2012年', h.accum(h.monthes(2012)))
    line.add(u'2013年', h.accum(h.monthes(2013)))
    line.add(u'2014年', h.accum(h.monthes(2014)))
    line.render_to_file(hsvgpath + 'month_all.svg')

    line = pygal.Line(
        width=800, height=400, interpolate='hermite', style=custom_style, dots_size=1)
    line.title = u'2012年每月下载量统计'
    line.x_labels = [u'上旬', u'中旬', u'下旬']
    for month in range(1, 13):
        line.add(u'2012年%02d月' % month, h.accum(h.days(2012, month)))
    line.render_to_file(hsvgpath + '2012_day_add.svg')

    line = pygal.Line(
        width=800, height=400, interpolate='hermite', style=custom_style, dots_size=1)
    line.title = u'2013年每月下载量统计'
    line.x_labels = [u'上旬', u'中旬', u'下旬']
    for month in range(1, 13):
        line.add(u'2013年%02d月' % month, h.accum(h.days(2013, month)))
    line.render_to_file(hsvgpath + '2013_day_add.svg')

    line = pygal.Line(
        width=800, height=400, interpolate='hermite', style=custom_style, dots_size=1)
    line.title = u'2014年每月下载量统计'
    line.x_labels = [u'上旬', u'中旬', u'下旬']
    for month in range(1, 13):
        line.add(u'2014年%02d月' % month, h.accum(h.days(2014, month)))
    line.render_to_file(hsvgpath + '2014_day_add.svg')

    line = pygal.Line(
        width=800, height=400, interpolate='hermite', style=custom_style, dots_size=1)
    line.title = u'2014年10~11月每日下载量统计'
    line.x_labels = [u'上旬', u'中旬', u'下旬']
    line.add(u'2014年10月', h.days(2014, 10))
    line.add(u'2014年11月', h.days(2014, 11))
    line.render_to_file(hsvgpath + '2014_11mon.svg')

    line = pygal.Line(
        width=800, height=400, interpolate='hermite', style=custom_style, dots_size=1)
    line.title = u'2014年11月最近几周每天下载量统计'
    line.x_labels = []
    for hours in range(1, 8):
        line.x_labels.append(u'周%d' % hours)
    for week in range(40, 47):
        line.add(u'2014年 第%d周' % week, h.weekdays(2014, week))
    line.render_to_file(hsvgpath + '2014_week.svg')

    line = pygal.Line(
        width=800, height=400, interpolate='hermite', style=custom_style, dots_size=1)
    line.title = u'2014年11月15~22日每小时下载量统计'
    line.x_labels = []
    for hours in range(0, 24):
        line.x_labels.append(u'%02d点' % hours)
    for day in range(15, 22):
        line.add(u'2014年11月%02d日 周%02d' %
                 (day, day - 14), h.hours(2014, 11, day))
    line.render_to_file(hsvgpath + '2014_11_hours_add.svg')


def torrentsvg():
    t = torrent.Torrent("../data/torrent.csv")
    tsvgpath = "../view/torrent/"

    bar = pygal.Bar(width=800, height=400, style=custom_style)
    bar.title = u'种子一级分类情况统计'
    for i, num in enumerate(t.topcidnum()):
        classes = [u'电影',u'剧集',u'音乐',u'动漫',u'游戏',u'综艺',u'体育',u'软件',u'学习',u'其他',u'纪录片']
        bar.add(classes[i], num)
    bar.render_to_file(tsvgpath + 'top_class.svg')

    cls = [['dianying.svg',[1000, 1002, 1003, 1004, 1005],[u'电影',u'中国',u'欧美',u'日韩',u'其他']],
          ['juji.svg',[1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207],[u'剧集', u'大陆', u'港台', u'日剧', u'韩剧', u'欧美', u'合集', u'其他']],
          ['yinyue.svg',[1400, 1401, 1402, 1403, 1404, 1405, 1406],[u'音乐', u'华语', u'欧美', u'日韩', u'古典', u'MV', u'无损']],
          ['dongman.svg',[1600, 1601, 1602, 1603, 1604],[u'动漫', u'动画', u'漫画', u'音乐', u'合集']],
          ['youxi.svg',[1800, 1801, 1802, 1803, 1804],[u'游戏', u'PC', u'PSP', u'其他', u'补丁']],
          ['zongyi.svg',[2000, 2001, 2002, 2003, 2004],[u'综艺', u'大陆', u'港台', u'日韩', u'其他']],
          ['tiyu.svg',[2200, 2201, 2202, 2203],[u'体育', u'足球', u'篮球', u'其他']],
          ['ruanjian.svg',[2400, 2401, 2402, 2403, 2404],[u'软件', u'镜像', u'压缩包', u'exe', u'其他']],
          ['xuexi.svg',[2600, 2601, 2602, 2603, 2604],[u'学习', u'计算机', u'外语', u'考研', u'课件']],
          ['qita.svg',[2800, 2801, 2802, 2803, 2804],[u'其他', u'视频', u'音乐', u'图片', u'文档']],
          ['jilu.svg',[3000, 3001, 3002],[u'纪录片', u'单集', u'合集']]]
    for cl in cls:
        bar = pygal.Bar(width=800, height=400, style=custom_style)
        bar.title = cl[2][0] + u'分类情况统计'
        for i, num in enumerate(t.cids(cl[1])):
            classes = cl[2]
            bar.add(classes[i], num)
        bar.render_to_file(tsvgpath + cl[0])

if __name__ == '__main__':
    historysvg()
    torrentsvg()
