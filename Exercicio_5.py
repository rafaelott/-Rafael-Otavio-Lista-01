def similar_pair(n, k, edges):
    tree = {}
    ch = set()
    
    for p, c in edges:
        if p not in tree:
            tree[p] = []
        tree[p].append(c)
        ch.add(c)
    
    for i in range(1, n + 1):
        if i not in ch:
            root = i
            break

    res = 0

    def dfs(nd, anc):
        nonlocal res
        for a in anc:
            if abs(a - nd) <= k:
                res += 1
        if nd in tree:
            for c in tree[nd]:
                dfs(c, anc + [nd])

    dfs(root, [])
    return res

def main():
    n, k = map(int, input().split())
    ed = [tuple(map(int, input().split())) for _ in range(n - 1)]
    res = similar_pair(n, k, ed)
    print(res)

if __name__ == "__main__":
    main()
