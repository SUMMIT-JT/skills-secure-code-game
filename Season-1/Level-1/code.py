'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    max_orders = 12
    max_total = 1e8
    net = 0.0
    if len(order.items) >= max_orders:
        return 'Total amount payable for an order exceeded'
    for item in order.items:
        if (item.amount < 0) or (item.amount >= max_total):
            continue
        if item.type == 'payment':
            net += item.amount * item.quantity
        elif item.type == 'product':
            net -= item.amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    if int(net) < 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id