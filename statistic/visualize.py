# -*- coding: utf-8 -*-
import pygal
import history

from pygal.style import Style

hsvgpath = "../view/history/"

h = history.History("../data/history.dat")

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
    line.add(u'2014年11月%02d日 周%02d' % (day, day - 14), h.hours(2014, 11, day))
line.render_to_file(hsvgpath + '2014_11_hours_add.svg')
