import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}


low_num = 1
high_num = 6
running = True
while running:
      num_of_dice = 0
      dice = []
      total = 0
      
      num_of_dice = input("How many dice?: ")
      if num_of_dice.isdigit() and num_of_dice is not '0':
            num_of_dice = int(num_of_dice)
            if  num_of_dice>high_num:
                  print("we do not have so much dices")
            else:
                  for die in range(num_of_dice):
                        dice.append(random.randint(1, 6))
                  for line in range(5):
                        for die in dice:
                              print(dice_art.get(die)[line],end="")
                        print()
                  for die in dice:
                        total += die
                  print(f"total: {total}")

                  if not input("continue playing(Y/N):").lower() == 'y':
                        running = False

      else:
            print("please put an integer number")
      
