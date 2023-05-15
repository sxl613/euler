from collections import defaultdict


def read_codes(path):
    ans = []
    with open(path, "r") as fd:
        ans = [tuple(int(i) for i in line.strip()) for line in fd]
    return ans


def build_graph(code_list: list):
    E = defaultdict(set)
    R = defaultdict(set)
    nodes = set()
    for a, b, c in code_list:
        nodes |= set([a, b, c])
        E[a].add(b)
        E[b].add(c)
        R[b].add(a)
        E[c].add(b)

    return nodes, E, R


def topo_sort(nodes: set, edges: dict, R: dict) -> str:
    C = defaultdict(int)
    for v in nodes:
        C[v] = len(R[v])
    stack = [k for k in nodes if C[k] == 0]
    ans = []
    while stack:
        v = stack.pop()
        ans.append(v)
        for e in edges[v]:
            C[e] -= 1
            if C[e] == 0:
                stack.append(e)
        edges[v] = set()
    return "".join(map(lambda v: str(v), ans))


def solve(path="p079_keylog.txt"):
    r = read_codes(path)
    V, E, R = build_graph(r)
    return topo_sort(V, E, R)


if __name__ == "__main__":
    print(f"Code: {solve()}")
