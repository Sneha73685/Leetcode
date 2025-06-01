#You are given two positive integers n and limit.
#Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

from math import comb
class Solution:
    def distributeCandies(self, candidates: int, limit: int) -> int:
        if candidates > 3 * limit:
            return 0
        total_distributions = comb(candidates + 2, 2)
        if candidates > limit:
            total_distributions -= 3 * comb(candidates - limit + 1, 2)
        if candidates - 2 >= 2 * limit:
            total_distributions += 3 * comb(candidates - 2 * limit, 2)
        return total_distributions