from itertools import permutations


def solution(n, weak, dist):
    theLen = len(weak)
    for i in range(theLen):
        weak.append(n + weak[i])
    answer = int(1e9)
    for si in range(theLen):
        friend_poss = list(permutations(dist, len(dist)))
        for friend in friend_poss:
            friend_cnt = 1
            border = weak[si] + friend[friend_cnt - 1]
            for i in range(si, si + theLen):
                if border < weak[i]:
                    friend_cnt += 1
                    if friend_cnt > len(dist):
                        break
                    border = weak[i] + friend[friend_cnt - 1]
            answer = min(answer, friend_cnt)
    if answer > len(dist):
        return -1
    return answer
