def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, p, c):
    p = find_parent(parent, p)
    c = find_parent(parent, c)
    parent[c] = p

def makeTree(tree, start):
    answer = ''
    answer += '('
    answer += start
    if start not in tree:
        answer+=')'
        return answer

    if len(tree[start]) == 1:
        answer += makeTree(tree, tree[start][0])
    elif len(tree[start]) == 2:
        if tree[start][0] < tree[start][1]:
            answer += makeTree(tree, tree[start][0])
            answer += makeTree(tree, tree[start][1])
        else:
            answer += makeTree(tree, tree[start][1])
            answer += makeTree(tree, tree[start][0])
    answer += ')'
    return answer

def solution(nodes):

    tree = {}
    isFirst = True
    ufparent = {}
    nn = set()
    nodeList = []
    parent = ''
    child = ''
    for i in range(len(nodes)):
        if nodes[i].isalpha():
            if isFirst:
                parent = nodes[i]
                nn.add(parent)
                isFirst = False
            else:
                child = nodes[i]
                nn.add(child)
                nodeList.append((parent, child))
                # if child not in ufparent:
                #     ufparent[child] = find_parent(ufparent, parent)

                # if find_parent(parent, a) != find_parent(parent, b):
                #     union_parent(parent, a, b)
                #

                if parent not in tree:
                    tree[parent] = [child]
                else:
                    tree[parent].append(child)

                while 1:
                    tree[parent]

                cyclecnt = 0
                for key in tree:
                    if child in tree[key]:
                        cyclecnt+=1
                    if cyclecnt > 1:
                        return "E3"
                isFirst = True

    for nnn in nn:
        ufparent[nnn] = nnn

    for p,c in nodeList:
        if find_parent(ufparent, p) != find_parent(ufparent, c):
            union_parent(ufparent, p,c)

    print(ufparent)
    rootcnt = 0
    root = ''
    for key in tree:
        #more than 2 child
        if len(tree[key]) > 2:
            return "E1"


        isRoot = True
        for v in tree.values():
            # dup edge , 부모 자식 바뀐 것도 생각해야하나?
            if tree[key].count(v) > 1:
                return "E2"


#root면 자식에 그게 없어야함
            if key in v:
                isRoot = False
        # multi root
        if isRoot:
            rootcnt += 1
            root = key
            if rootcnt >= 2:
                return "E4"

    print(tree)
    print(root)
    answer = makeTree(tree, root)
    print(answer)
    return answer

# solution("(B,D) (D,E) (A,B) (C,F) (E,G) (A,C)")
solution("(A,B) (B,D) (B,C) (C,A)")
