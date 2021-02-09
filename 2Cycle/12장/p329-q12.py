def possible(answer):
    for x, y, is_pole in answer:
        if is_pole == 0: 
            if y == 0 or [x-1, y, 1] in answer or [x,y,1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif is_pole == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frames in build_frame:
        x, y, is_pole, is_build = frames
        if is_build == 0:
            answer.remove([x, y, is_pole])
            if not possible(answer):
                answer.append([x,y,is_pole])
        elif is_build == 1:
            answer.append([x,y,is_pole])
            if not possible(answer):
                answer.remove([x,y,is_pole])
    return sorted(answer)