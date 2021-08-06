# https://www.hackerrank.com/challenges/count-triplets-1/problem?fbclid=IwAR2iS6zOE0VJLGrGXl_o07trE1aS3feESNOK68VLu0YqzhoviSSAvi5tbao
# You are given an array and you need to find number of tripets of
# indices (i, j, k) such that the elements at those indices are
# in geometric progression for a given common ratio  and i < j < k
import itertools

def countTriplets(arr, r):
    if r > 1:
        triplets_list_short = [(n, r * n, r * r * n) for n in arr if r * n in arr and r * r * n in arr]
        extra_elements = [t for t in triplets_list_short for i in range((arr.count(t[1]) - 1) + (arr.count(t[2]) - 1))]
        triplets_list = triplets_list_short + extra_elements
    elif r == 1:
        same_number = {
            k: [k] * arr.count(k) for k in arr
        }
        triplets_list = [t for k in same_number for t in itertools.combinations(same_number[k], 3)]
    return len(triplets_list)