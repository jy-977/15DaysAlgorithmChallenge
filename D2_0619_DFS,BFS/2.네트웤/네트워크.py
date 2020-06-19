def new_dfs(start, node,cnt,computers,path):

    for i in range(start, len(node)) : #이거만 바꾸면 된다!!!


        print("\n\n\n")
        print("start : ",start, "len node : ", len(node))
        print("path :", path)
        print("nodes :", node)
        node.remove(start)

        for j in node:
            print("i : ", i, "j: ", j)
            if computers[i][j] ==1 :
                path.append(i)
                computers[i][j], computers[j][i] = 0, 0
                start = j
                new_dfs(start,node,cnt,computers,path)
                return
        path.append(i)
        print("path :", path)
        print("nodes :", node)
        if node:
            start = node[0]
            new_dfs(start, node, cnt, computers, path)

        cnt+=1
        print("cnt : ", cnt)
    return cnt

"""
def dfs(n,cnt,computers,path) :
    print(computers)
    print(path)
    for i in range(x,n):
        for j in range(n):
            print('i : ', i, 'j : ', j)
            if computers[i][j] ==1 :
                if i+1 not in path:
                    path.append(i)#나중에 i+1로 고치기
                path.append(j)
                print(j)
                computers[i][j], computers[j][i] = 0 , 0
                dfs(j,i,n,cnt,computers,path)
                path.pop()
            print("after pop path",path)
    cnt +=1
    print("cnt:", cnt)
    return cnt
"""
def solution(n, computers):
    answer = 0
    path = []
    node = []
    for _ in range(n) :
        node.append(_)
        computers[_][_] =0
    answer = new_dfs(0,node,n,computers,[])
    return answer


solution(6, [[1,0,0,0,1,0],[0,1,1,0,0,0],[0,1,1,0,0,1],[0,0,0,1,0,0],[1,0,0,0,1,0],[0,0,1,0,0,1]])