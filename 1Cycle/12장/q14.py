from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    # 길이를 두 배로 늘려서 원형을 일자 형태로 만들 수 있다.
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    for start in range(length):  # 각 취약점을 시작점으로
        for friend in list(permutations(dist, len(dist))):  # 친구를 나열하는 모든 경우
            count = 1  # 투입할 친구 수
            limit = weak[start] + friend[count - 1]  # 현재 친구가 확인 가능한 최대 위치
            for index in range(start, start + length):
                if limit < weak[index]:  # 현재 친구만으로 모두 커버할 수 없다면
                    count += 1
                    if count > len(dist):  # 더이상 투입 불가
                        break
                    # 다음 친구가 확인할 수 있는 최대 위치로 갱신
                    limit = weak[index] + friend[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer
