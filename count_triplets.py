# https://www.hackerrank.com/challenges/count-triplets-1/problem?fbclid=IwAR2iS6zOE0VJLGrGXl_o07trE1aS3feESNOK68VLu0YqzhoviSSAvi5tbao
# You are given an array and you need to find number of tripets of
# indices (i, j, k) such that the elements at those indices are
# in geometric progression for a given common ratio  and i < j < k


def countTriplets(arr, r):
    triplets_list_unique = [(n, r * n, r * r * n) for n in arr if r * n in arr and r * r * n in arr]
    extra_elements = [t for t in triplets_list_unique for i in range((arr.count(t[1]) - 1) + (arr.count(t[2]) - 1))]
    triplets_list = triplets_list_unique + extra_elements
    return len(triplets_list)
