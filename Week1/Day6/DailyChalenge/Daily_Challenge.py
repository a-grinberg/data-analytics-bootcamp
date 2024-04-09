# Challenge 1

word = "froggy"
letters = {}

for i, l in enumerate(word):
    if l in letters:
        letters[l].append(i)
    else:
        letters[l] = [i]

print(letters)


# Challenge 2

def my_wallet(items_purchase, wallet):
    wallet = int(wallet[1:])
    items_lst = []
    for item, price in items_purchase.items():
        if wallet > 0 and wallet > int(price[1:].replace(',','')):
            wallet -= int(price[1:].replace(',',''))
            items_lst.append(item)
    items_lst.sort()
    return items_lst if len(items_lst) > 0 else "Nothing"


items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"
print(my_wallet(items_purchase, wallet))

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 
print(my_wallet(items_purchase, wallet))

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 
print(my_wallet(items_purchase, wallet))