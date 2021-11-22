def minimumDivision(a, b, k):
    # Write your code here
    segs = []
    conn = []
    for i in range(len(a)):
        segs.append((a[i], b[i]))
    segs.sort(key= lambda a : (a[0],a[1]))
    print(segs)

    bb = segs[0][1]
    for i in range(1, len(segs)):
        if segs[i][0] > bb:
            conn.append((bb, segs[i][0]))
            bb = segs[i][1]

        elif segs[i][0] == bb:
            bb = segs[i][1]

        else:
            if segs[i][1] > bb:
                bb = segs[i][1]

    # conn.append((aa,bb))
    print(conn)
    print(k)

    ans = 0
    for i in range(len(conn)):
        ca = conn[i][0]
        cb = conn[i][1]
        posible = 0
        if cb - ca > k:
            continue
        else:
            posible+=1

        for j in range(i+1, len(conn)):
            ncb = conn[j][1]
            if ncb - ca <= k:
                posible+=1
            else:
                break
        ans = max(posible, ans)

    return len(conn)-ans+1




print(minimumDivision([1,2,5,10], [2,4,8,11], 2))