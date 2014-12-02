import csv


class User(object):

    def __init__(self, path):
        self.path = path
        self.u_list = []
        self.load(path)

    def load(self, path):
        with open(path, 'r') as infile:
            next(infile)
            reader = csv.reader(infile)
            for user in reader:
                self.u_list.append(user)

if __name__ == '__main__':
    u = User("../data/test/user.csv")
    print u.u_list