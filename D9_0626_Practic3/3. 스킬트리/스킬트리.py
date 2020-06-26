def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in range(len(skill_trees)):
        check =[]
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                check.append(skill.index(skill_trees[i][j]))
        for j in range(len(check)):
            if check[j]!=j:
                answer -=1
                break
    return answer