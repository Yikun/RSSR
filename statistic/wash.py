import random
import csv
import time
import operator


def sample(inpath, outpath, samplenum):
	"""
	Sample data by 1/samplenum sample rate
	"""
	with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
		for row in infile:
			if random.randint(0, samplenum) == 0:
				outfile.write(row)


def gen_history(inpath, outpath):
    """
    Generate history downloads info with time
    in : (uid, tid, timestamp)
    out: (year, month, day, hour, week, weekday, yearday, downloads)
    """
    with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:
        stadic = {}
        # skip header row
        # header = next(infile)
        infile.next()
        reader = csv.reader(infile)
        for uid, tid, timestamp in reader:
            # year, month, day, hour, week, weekday, yearday
            ym = time.strftime(
                '%Y,%m,%d,%H,%W,%w,%j', time.localtime(int(timestamp)))
            if ym in stadic:
                stadic[ym] += 1
            else:
                stadic[ym] = 1
        # sort by key
        sorted_stadic = sorted(stadic.items(), key=operator.itemgetter(0))
        for x, y in sorted_stadic:
            outfile.write(("%s,%s\n") % (x, y))


def wash_torrent(inpath, outpath):
    """
    Wash the comma of torrent title
    """
    with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:

        reader = csv.reader(infile)

        for row in reader:
            rowcontent = ("%s,%s,%s,%s,%s,%s,%s,%s\n") % (
                row[0], ''.join(row[1:-6]), row[-6], row[-5], row[-4], row[-3], row[-2], row[-1])
            outfile.write(rowcontent)

if __name__ == '__main__':
    # Sample data
	sample("../data/user.csv", "../data/test/user.csv", 3000)
	sample("../data/torrent.csv", "../data/test/torrent.csv", 3000)
	sample("../data/history.csv", "../data/test/history.csv", 50000)
    # Wash the comma of torrent's title.
    wash_torrent("../data/rsdata_11-27/torrents.csv", "../data/torrent.csv")
    # Generate downloads history.(time, downloads)
    gen_history("../data/history.csv","../data/history.dat")
