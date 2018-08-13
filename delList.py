def delete_nth(order,max_e):
    print('order',order)
    print(max_e)
    return order[0:len(order) - max_e - 1] + order[-max_e:len(order)]
print(delete_nth([20,37,20,21], 1))
print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3, 2, 4, 5, 3, 1], 3))