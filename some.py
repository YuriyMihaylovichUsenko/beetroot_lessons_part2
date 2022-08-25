graph = {}

graph['start'] = {}

graph['start']['B'] = 6
graph['start']['A'] = 2

print(graph['start'].keys())
print(graph['start']['A'])
print(graph['start']['B'])

graph['A'] = {}
graph['A']['finish'] = 5
graph['A']['B'] = 3

graph['B'] = {}
graph['B']['finish'] = 1

graph['finish'] = {}

# Costs of relations
costs = {}

costs['B'] = 6
costs['A'] = 2

costs['finish'] = float('inf')

print(float('inf'))

# Parents nodes
parents = {}

parents['A'] = ['start']
parents['B'] = ['start']
parents['finish'] = ['start']
processed = []
print(processed)

def find_lowest_node_cost(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        # print(costs)
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def dijikstra_search():
    # Знайти вузол з найменшою варсітю серед необроблених
    node = find_lowest_node_cost(costs)
    # print(node)

    while node is not None:  # якщо пройдені всі вузли цикл завершуємо
        cost = costs[node]

        neighbors = graph[node]

        for neighbor in neighbors:  # перебираємо усіх сусідів поточного вузла
            new_cost = cost + neighbors[neighbor]
            # Якщо до сусіда можна дійти швидше через поточний вузол
            if costs[neighbor] > new_cost:
                # оновлюємо вартість цього вузла
                costs[neighbor] = new_cost
                # Цей вузол стає батьком для наших нових сусідів
                parents[neighbor].append(node)

        processed.append(node)  # Помічаємо вузол як оброблений
        # Шукаємо наступний вузол з найменшою вартістю
        print(node, parents[node])
        node = find_lowest_node_cost(costs)



print('+' * 80)
dijikstra_search()