# Fantasy Game Inventory
# Function that takes any possible inventory and display it in a specipic way


inv = {'rope' : 1, 'torch' : 6, 'gold coin' : 42, 'dagger"' : 1, 'arrow' : 12}


def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for x, y in inventory.items():
        print(y, " ", x)
        total += y
    print("Total number of items: ", total)

display_inventory(inv)


    
