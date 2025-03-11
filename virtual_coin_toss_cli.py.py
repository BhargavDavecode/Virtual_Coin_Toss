import random  

def flip_coin():
    return random.choice(["Heads", "Tails"])  

while True:
    while True:
        try:
            num_flips = int(input("\nHow many times would you like to flip the coin?\n"))
            if num_flips <= 0:
                print("Invalid input! Please enter a positive number.")
                continue  # Ask again if 0 or negative number
            break  # Exit loop if valid
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Reset counters at the start of each session
    heads_count = 0
    tails_count = 0

    # Loop through the number of flips
    for i in range(num_flips):
        result = flip_coin()
        print(f"Flip {i+1}: {result}")  # Show individual flip result
        
        # Update counters
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    # Calculate percentages
    heads_percentage = (heads_count / num_flips) * 100
    tails_percentage = (tails_count / num_flips) * 100

    # Display the final results
    print("\nResults Summary:")
    print(f"Heads: {heads_count} ({heads_percentage:.2f}%)")
    print(f"Tails: {tails_count} ({tails_percentage:.2f}%)")

    # Ask user if they want to play again with input validation
    while True:
        play_again = input("\nWould you like to flip again? (yes/no): ").strip().lower()
        if play_again in ["yes", "no"]:
            break  # Valid input, exit loop
        print("Invalid input! Please enter 'yes' or 'no'.")

    if play_again == "no":
        print("Thanks for playing!")
        break
