import collections
def most_frequent(string):
    d = collections.Counter(string)
    print(list(d.most_common()))

most_frequent('Mississippi')
