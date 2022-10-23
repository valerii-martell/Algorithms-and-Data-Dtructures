def hanoi(quantity, start, end, buf):
    if quantity:
        hanoi(quantity-1, start, buf, end)
        print("{} -> {}".format(start, end))
        hanoi(quantity-1, buf, end, start)