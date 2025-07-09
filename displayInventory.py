stuff = {'rope': 1, 'torch': 7, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    total_items = 0
    # ^ starts the count at 0
    print("Inventory:")

    for item, quantity in inventory.items():
        # ^ assigns "item" to the first variable in the target iterable
            # (in this case, the key)
        # assigns "quantity" to the second variable in the target iterable
            # (in this case, the variable)
        # .items() is a built-in method that  returns all key-value pairs as tuples
            # a tuple is essentially a list that cannot be changed
        print(quantity, item)
        # ^ prints each pair of items in the order of quanity first, then item name
        total_items += quantity
        # ^ updates the count to the total quantity
            # each item will be counted separately, so each time it loops it will add
            # i.e. on loop 1 it will be 1, then loop 2 will add to 8, etc.
    print(f'Total number of items: {total_items}')
    # ^ use the f-string to better interate strings and variables


if __name__ == "__main__":
    displayInventory(stuff)
