# This program adds the items looted from the dragon to the player's inventory.

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k in inventory.keys():
        print(str(inventory.get(k,0)) + ' ' + str(k))
        item_total = item_total + inventory.get(k, 0) # This is tracking all the numbers correctly
    print('Total number of items: ' + str(item_total))

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 0)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(inv, dragon_loot)
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
