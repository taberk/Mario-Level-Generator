def get_height(prompt):
    while True:
        try:
            value = int(raw_input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 1:
            print("Sorry, your response must be greater than 0.")
            continue
        elif value > 23:
            print("Sorry, your response must be less than 24.")
            continue
        else:
            break
    return value

height = get_height("Enter a number greater than 0 and less than 24: ")
blocks = 1
spaces = height - 1

while blocks <= height:
    print ((' ' * spaces) + ('#' * blocks) + (' ' * 2) + ('#' * blocks))
    blocks += 1
    spaces -= 1
