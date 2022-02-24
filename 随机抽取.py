import sys
import random
user_input = input("Please enter some text, and I will display it(enter 继续 to continue 终止 to exit): ")
if user_input == "继续":
    print(random.randint(1,47))
else:
    if user_input == "终止":
        sys.exit()
        sys.exit(0)
  


