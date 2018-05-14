#
# Author: jun10000 (https://github.com/jun10000)
#

def contains_last_listitems(small, large):
    cdef int small_count = len(small)
    cdef int large_count = len(large)
    if small_count > large_count: return False

    cdef int count = small_count
    cdef int i, s, l
    for i in range(count):
        s = small[small_count - i - 1]
        l = large[large_count - i - 1]
        if s != l: return False

    return True
