__author__ = 'erickwendel'


# Weighted quick-union.

# Quick union with path compression.
# Just after computing the root of p, set the id of each examined node to point to that root

class quick_union_weighted:
    _id = []
    _sz = []
    def __init__(self, n):
        self._id = [0] * n
        self._sz = [0] * n

        for i in range(0, n):

            self._id[i] = i
            self._sz[i] = 1
    def root(self, i):
        while i != self._id[i]:
            # this line set the root more up
            # Two-pass implementation:
            #   add second loop to root() to set the id[] of each examined node to the root.
            # Simpler one-pass variant: Make every other node in path point to its grandparent (thereby halving path length).
            if self._id[i] != self._id[self._id[i]]:
                print("self._id[i] = [%d], self._id[self._id[i]] = [%d]" % (self._id[i], self._id[self._id[i]]))

            self._id[i] = self._id[self._id[i]]
            i = self._id[i]

        return  i


    def connected(self, p, q):

        #check if p and q have same root (depth of p and q array accesses)
        return self.root(p) == self.root(q)

    def  union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i == j:  return;

        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]

        else:
            self._id[j] = i
            self._sz[i]  += self._sz[j]

        # change root of p to point to root of q (depth of p and q array accesses)
        # self._id[i] = j

    def union2(self, p, q):
            if not self.connected(p, q):
                self.union(p, q)
 # test
quick = quick_union_weighted(11)
quick.union2(4,3)
quick.union2(3,8)
quick.union2(6,5)
quick.union2(9,4)
quick.union2(2,1)
quick.union2(8,9)
quick.union2(5,0)
quick.union2(7,2)
quick.union2(6,1)
quick.union2(7,3)


for i in range(0, len(quick._id)):
    print("[%d] = [%d]" % (i, quick._id[i]));

# output
# [0] = [6]
# [1] = [2]
# [2] = [6]
# [3] = [4]
# [4] = [6]
# [5] = [6]
# [6] = [6]
# [7] = [2]
# [8] = [4]
# [9] = [4]
# [10] = [10]


