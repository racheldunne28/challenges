# https://www.hackerrank.com/challenges/count-triplets-1/problem?fbclid=IwAR2iS6zOE0VJLGrGXl_o07trE1aS3feESNOK68VLu0YqzhoviSSAvi5tbao
# You are given an array and you need to find number of tripets of
# indices (i, j, k) such that the elements at those indices are
# in geometric progression for a given common ratio  and i < j < k


def countTriplets(arr, r):
    triplets_list = [(n, r * n, r * r * n) for n in arr if r * n in arr and r * r * n in arr]
    triplets_set = set(triplets_list)
    return len(triplets_set)
