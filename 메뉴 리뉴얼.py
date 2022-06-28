from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    hubo = defaultdict(int)
    course_hubo_int = defaultdict(int)
    course_hubo = defaultdict(list)
    
    for order in orders:
        order = sorted(order)
        for c in course:
            tmp = list(combinations(order, c))
            d = []
            for t in tmp:
                d.append(''.join(t))
            for j in d:
                hubo[j] += 1
    
    sorted_dict = sorted(hubo.items(), key = lambda item: item[1], reverse = True)
    
    for c in course:
        for keys, values in hubo.items():
                if len(keys) == c:
                    course_hubo_int[c] = max(hubo[keys], course_hubo_int[c])
            
    
    for c in course:
        for keys, values in hubo.items():
            if len(keys) == c and values == course_hubo_int[c] and values > 1:
                course_hubo[c].append(keys)
    

    for c in course_hubo.values():
        for i in c:
            answer.append(i)
    
    return sorted(answer)
