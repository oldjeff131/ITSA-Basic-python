def min_dispatch():
    order_amount = input()
    orders = input()
    orders = orders.split(" ")
    orders = list(map(int, orders))
    order_pairs = []
    dispatch_counter = int(order_amount)
    for i in range(0, len(orders), 2):
        order_pairs.append((orders[i], orders[i + 1]))

    order_pairs_copy = order_pairs.copy()

    for order_pair in order_pairs:
        removed_index_cache = []
        end_time = order_pair[1]
        for copy_index, order_pair_copy in enumerate(order_pairs_copy):
            if end_time <= order_pair_copy[0]:
                dispatch_counter -= 1
                removed_index_cache.append(copy_index)
                end_time = order_pair_copy[1]
        order_pairs_copy = [order_pair_copy for i, order_pair_copy in enumerate(order_pairs_copy) if i not in removed_index_cache]

    return dispatch_counter


if __name__ == '__main__':
    dispatch_count = min_dispatch()
    print(dispatch_count)