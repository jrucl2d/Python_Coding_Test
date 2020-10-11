def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 설치된 것이 기둥이면
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [
                    x, y - 1, 0
            ] in answer:
                continue
            return False
        elif stuff == 1:  # 설치된 것이 보이면
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frames in build_frame:
        x, y, stuff, operate = frames
        if operate == 0:  # 삭제의 경우
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        elif operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)