# from itertools import groupby
# s = 'aaa bbb ddd ddd eee fff ttt ddd'
# g = groupby(s.split())
# for k,v in g: print(k)
s = "the sky is blue very blue sky sky any value the"
s = s.lower()
slist = s.split()
print(" ".join(sorted(set(slist), key=slist.index)))