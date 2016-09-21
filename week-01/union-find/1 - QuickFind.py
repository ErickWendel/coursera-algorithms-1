__author__ = 'erickwendel'


#Quick-find [eager approach]
#Data structure.
#   Integer array id[] of length N
#   Interpretation: p and q are connected if and only if they have the same id
#       Find. Check if p and q have the same id.
#       Union. To merge components containing p and q, change all entries whose id equals id[p] to id[q].
#Union is too expensive. It takes N2 (quadratic) array accesses to process a sequence of N union commands on N objects.

# Quick-find defect.
# ・Union too expensive (N array accesses).
# ・Trees are flat, but too expensive to keep them flat.

class quick_find:
    _id = []
    def __init__(self, n):
        self._id = [0] * n
        # set id of each object to itself (N array accesses)
        for i in range(0, n):
            self._id[i] = i

    #     check whether p and q
    # are in the same component (2 array accesses)
    def connected(self, p, q):
        return self._id[p] == self._id[q]

    def  union(self, p, q):
        pid = self._id[p]
        qid = self._id[q]
        for i in range(0, len(self._id)):
            if self._id[i] == pid:
                self._id[i] = qid


    def union2(self, p, q):
        if not quick.connected(p, q):
            self.union(p, q)

 # test
quick = quick_find(11)

quick.union2(4,3)
quick.union2(3,8)
quick.union2(6,5)
quick.union2(9,4)
quick.union2(2,1)
quick.union2(8,9)
quick.union2(5,0)
quick.union2(7,2)
quick.union2(6,1)



for i in range(0, len(quick._id)):
    print("[%d] = [%d]" % (i, quick._id[i]));

#output
# [0] = [1]
# [1] = [1]
# [2] = [1]
# [3] = [8]
# [4] = [8]
# [5] = [1]
# [6] = [1]
# [7] = [1]
# [8] = [8]
# [9] = [8]
# [10] = [10]



