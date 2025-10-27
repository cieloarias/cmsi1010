from cards import deal, poker_classification

def main():
    while True:
   
        user_input = input("Enter the number of players (2-10): ").strip().lower()
        
       
        if user_input in ("bye", "exit"):
            print("Goodbye!")
            break
        
        # Check if input is a number
        if not user_input.isdigit():
            print("Please enter a number between 2 and 10, or 'bye' to quit.")
            continue

        num_players = int(user_input)

        # Check if number is within range
        if num_players < 2 or num_players > 10:
            print("Number of players must be between 2 and 10.")
            continue

        try:
            # Deal 5-card hands to each player
            hands = deal(num_players, 5)
            
            # Print each hand and its classification
            for hand in hands:
                hand_str = " ".join(str(card) for card in hand)
                hand_type = poker_classification(hand)
                print(f"{hand_str} is a {hand_type}")
        
        except Exception as e:
            # Catch any unexpected errors
            print("Error:", e)
            continue

if __name__ == "__main__":
    main()