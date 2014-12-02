import csv
import calendar


class History(object):

    """
    Class for download history
    """

    def __init__(self, path):
        self.dl_list = []
        self.load(path)

    def load(self, path):
        self.dl_list = []
        with open(path, 'r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                self.dl_list.append(row)
        return self.dl_list

    def monthes(self, year, default=0):
        """Get monthes downloads list of 'year'."""
        stadic = {}
        for record in self.dl_list:
            if int(record[0]) == year:
                if record[1] in stadic:
                    stadic[record[1]] += int(record[7])
                else:
                    stadic[record[1]] = int(record[7])
        monlist = []

        for i in range(1, 13):
            if (("%02d") % i) in stadic:
                monlist.append(stadic[("%02d") % i])
            else:
                monlist.append(default)
        return monlist

    def weekdays(self, year, week, default=0):
        """Get weekdays downloads list of 'year.week'."""
        stadic = {}
        for record in self.dl_list:
            if (int(record[0]), int(record[4])) == (year, week):
                if record[5] in stadic:
                    stadic[record[5]] += int(record[7])
                else:
                    stadic[record[5]] = int(record[7])
        weeklist = []

        for i in [1, 2, 3, 4, 5, 6, 0]:
            if (("%d") % i) in stadic:
                weeklist.append(stadic[("%d") % i])
            else:
                weeklist.append(default)
        return weeklist

    def days(self, year, month, default=0):
        """Get days downloads list of 'year.month'."""
        stadic = {}
        for record in self.dl_list:
            if (int(record[0]), int(record[1])) == (year, month):
                if record[2] in stadic:
                    stadic[record[2]] += int(record[7])
                else:
                    stadic[record[2]] = int(record[7])
        daylist = []

        mondays = calendar.monthrange(int(year), int(month))[1]
        # print mondays
        for i in range(1, mondays + 1):
            if (("%02d") % i) in stadic:
                daylist.append(stadic[("%02d") % i])
            else:
                daylist.append(default)
        return daylist

    def hours(self, year, month, day, default=0):
        """Get hours downloads list of 'year.month'."""
        stadic = {}
        for record in self.dl_list:
            if (int(record[0]), int(record[1]), int(record[2])) == (year, month, day):
                if record[3] in stadic:
                    stadic[record[3]] += int(record[7])
                else:
                    stadic[record[3]] = int(record[7])
        hourlist = []

        for i in range(0, 24):
            if (("%02d") % i) in stadic:
                hourlist.append(stadic[("%02d") % i])
            else:
                hourlist.append(default)
        return hourlist

    def accum(self, dl_list):
        """Get accumulate list of list.[1,2,3] => [0, 1, 1+2, 1+2+3]"""
        dl_list_add = [0]
        for dl in dl_list:
            dl_list_add.append(dl + dl_list_add[-1])
        return dl_list_add

if __name__ == '__main__':

    h = History("../data/history.dat")

    # get 2014's monthes downloads list, missing info set 0
    print h.monthes(2014)
    # get 2014's monthes downloads list, missing info set 'None'
    print h.monthes(2014, None)

    # get 2014's 46th week's weekdays downloads list
    print h.weekdays(2014, 46)
    print h.weekdays(2014, 46, None)

    # get 2014's.Jan's days downloads list
    print h.days(2014, 1)
    print h.days(2014, 1, None)

    # get 2014.11.27's hours downloads list
    print h.hours(2014, 11, 27)
    print h.hours(2014, 11, 27, None)

    # accumulate h.days(2014, 1)
    print h.accum(h.days(2014, 1))
