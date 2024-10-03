# defining the menu of resturent
menu={
    'Pizza':50,
    'Biryani':110,
    'Chowmin':60,
    'Salad':50,
    'Coffee':40,
    'Tea':40,
}

# print(menu)

# Greeting
print('Welcome to My Resturant!')
print('Pizza: Rs.50\nBiryani: Rs.110\nChowmin: Rs.60\nSalad: Rs.50\nCoffee: Rs.40\nTea: Rs.40')


order_total=0

item_1=input('Enter the name of the item you wish to order:')
if item_1 in menu:
    order_total += menu[item_1]
    print(f'You have ordered {item_1} for Rs.{menu[item_1]}')

else:
    print(f'{item_1} is not available')

another_order=input('Do you want to order anything else? (yes/no)')
if another_order=='yes':
    item_2=input('Enter the name of the item you wish to order:')
    if item_2 in menu:
        order_total += menu[item_2]
        print(f'You have ordered {item_2} for Rs.{menu[item_2]}')

    else:
        print(f'{item_2} is not available')

print(f'Total amount of item is to pay {order_total}')