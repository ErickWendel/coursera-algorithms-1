__author__ = 'erickwendel'

# Quick-union [lazy approach]
# Data structure.
# ・Integer array id[] of length N.
# ・Interpretation: id[i] is parent of i.
# ・Root of i is id[id[id[...id[i]...]]]. keep going until it doesn’t change (algorithm ensures no cycles)
#       Find. Check if p and q have the same root
#       Union. To merge components containing p and q, set the id of p's root to the id of q's root.

# Quick-union defect.
# ・Trees can get tall.
# ・Find too expensive (could be N array accesses).
class quick_union:
    _id = []
    def __init__(self, n):
        self._id = [0] * n
        for i in range(0, n):

            # set id of each object to itself (N array accesses)
            self._id[i] = i

    def root(self, i):
        while i != self._id[i]:

             #chase parent pointers until reach root (depth of i array accesses)
             i = self._id[i]

        return  i


    def connected(self, p, q):

        #check if p and q have same root (depth of p and q array accesses)
        return self.root(p) == self.root(q)

    def  union(self, p, q):
        i = self.root(p)

        j = self.root(q)
        # change root of p to point to root of q (depth of p and q array accesses)
        self._id[i] = j

    def union2(self, p, q):
            if not self.connected(p, q):
                self.union(p, q)
 # test
quick = quick_union(11)
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




