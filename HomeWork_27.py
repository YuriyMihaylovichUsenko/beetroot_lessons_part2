def search(graph, n1, n2):
    parents = {n1: None}
    searching_list = [n1]

    def result():
        end = n2
        res = []
        while end:
            res.append(end)
            end = parents[end]
        return ' -> '.join(str(i) for i in res[::-1])

    for i in searching_list:
        for j in graph[i]:
            if j in parents:
                continue
            elif j == n2:
                parents[j] = i
                return result()
            else:
                parents[j] = i
                searching_list.append(j)


def main():
    graph = {1: [2, 5], 2: [1, 3, 4], 3: [2, 5], 4: [2, 6], 5: [1, 3], 6: [4]}

    print(search(graph, 6, 1))


if __name__ == '__main__':
    main()
