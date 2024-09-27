foods = []
prices = []
total = 0
while True:
      food = input("Enter a food to buy (q to quit):")
      if food.lower()=='q':
            break
      isprice= True
      while isprice:
            price = input("Enter a price of a {food}:$")
            if price.isdigit():
                  foods.append(food)
                  prices.append(price)
                  isprice = False
            else:
                  print("invalid price")


print("----- YOUR CART -----")
for food in foods:
      print(food, end=" ")
for price in prices:
      total += float(price)
print()
print(f"Your total is: ${total}")