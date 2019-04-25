def whatFlavors(cost, money):
    costdic = {}
    result = []
    sorted_cost = sorted(cost)
    print('sorted_cost: {}'.format(sorted_cost))
    # get a dictionary of cost
    for i in range(len(cost)):
        costdic[i] = cost[i]

    # get the cost

    for i in range(len(sorted_cost)):
        complement = money - i
        print('complement: {}'.format(complement))

        if complement in sorted_cost[i+1:]:
            print('found one')
            get_right_index(i, complement, cost)


def get_right_index(item1, comp, arr):
     index1 = arr.index(comp)

if __name__ == '__main__':
    menu = [2, 7, 13, 5, 4, 13, 5]
    money = 10

    whatFlavors(menu, money)
