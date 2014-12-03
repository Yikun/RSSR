import csv
import operator


class Torrent(object):

    def __init__(self, path):
        self.path = path
        self.t_list = []
        self.load(path)

    def load(self, path):
        with open(path, 'r') as infile:
            next(infile)
            reader = csv.reader(infile)
            for t in reader:
                self.t_list.append([int(t[0]),
                                    t[1],
                                    int(t[2]),
                                    int(t[3]),
                                    int(t[4]),
                                    int(t[5]),
                                    int(t[6]),
                                    int(t[7]),
                                    int(t[8])
                                    ])

    def top(self, rank, keyindex):
        topx = sorted(
            self.t_list, key=operator.itemgetter(keyindex), reverse=True)
        return topx[0:rank]

    def cids(self, cid):
        dic = {}
        downloads = []
        for t in self.t_list:
            if t[2] in cid:
                if t[2] in dic:
                    dic[t[2]] += 1
                else:
                    dic[t[2]] = 1
        for c in cid:
            if c in dic:
                downloads.append(dic[c])
            else:
                downloads.append(0)

        return downloads  # sorted(dic.items(), key=operator.itemgetter(0))

    def allcidnum(self):
        return t.cids([1000, 1002, 1003, 1004, 1005,
                       1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207,
                       1400, 1401, 1402, 1403, 1404, 1405, 1406,
                       1600, 1601, 1602, 1603, 1604,
                       1800, 1801, 1802, 1803, 1804,
                       2000, 2001, 2002, 2003, 2004,
                       2200, 2201, 2202, 2203,
                       2400, 2401, 2402, 2403, 2404,
                       2600, 2601, 2602, 2603, 2604,
                       2800, 2801, 2802, 2803, 2804,
                       3000, 3001, 3002])

    def topcidnum(self):
        return [sum(self.cids([1000, 1002, 1003, 1004, 1005])),
                sum(self.cids(
                    [1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207])),
                sum(self.cids([1400, 1401, 1402, 1403, 1404, 1405, 1406])),
                sum(self.cids([1600, 1601, 1602, 1603, 1604])),
                sum(self.cids([1800, 1801, 1802, 1803, 1804])),
                sum(self.cids([2000, 2001, 2002, 2003, 2004])),
                sum(self.cids([2200, 2201, 2202, 2203])),
                sum(self.cids([2400, 2401, 2402, 2403, 2404])),
                sum(self.cids([2600, 2601, 2602, 2603, 2604])),
                sum(self.cids([2800, 2801, 2802, 2803, 2804])),
                sum(self.cids([3000, 3001, 3002]))
                ]

if __name__ == '__main__':
    t = Torrent("../data/torrent.csv")
    # id(0),filename(1),cid(2),size(3),numfiles(4),finished(5),lasttime(6),lastuser(7),tid(8)
    for x in t.top(20, 5):
        print x[1], x[5]

    print t.allcidnum()
    print t.topcidnum()
