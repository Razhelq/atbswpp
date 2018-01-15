# List to dictionary function for Fantasy Game Inventory
# Update the exsisting inventory


inv = {'rope' : 1, 'torch' : 6, 'gold coin' : 42, 'dagger' : 1, 'arrow' : 12}


def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1    
    print("Inventory:")
    total = 0    
    for x, y in inventory.items():
        print(y, " ", x)
        total += y
    print("\nTotal number of items: ", total)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'gold coin']

add_to_inventory(inv, dragon_loot)    
