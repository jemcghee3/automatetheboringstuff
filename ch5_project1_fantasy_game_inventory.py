stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger':1, 'arrow': 12}

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k in inventory.keys():
        print(str(inventory.get(k,0)) + ' ' + str(k))
        item_total = item_total + inventory.get(k, 0) # This is tracking all the numbers correctly
    print('Total number of items: ' + str(item_total))

display_inventory(stuff)

