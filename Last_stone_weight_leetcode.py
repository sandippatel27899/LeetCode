# link : https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3297/

stones = [1,2,3,4,45,5]

while(len(stones) > 1):
    stones =  sorted(stones)
    ans = abs(stones[-1] - stones[-2])
    stones.pop()
    stones.pop()
    if ans:
        stones.append(ans)


if stones:
    print(stones[0]) 
else:
    print(0)
# print(stones)

