import random

# List of template dictionaries (I did my family for the names)
templates = [
    {"text": "The :color :animal jumped over the :adjective :object.", "author": "Cielo"},
    {"text": "I went to the :place and bought a :adjective :thing.", "author": "Erny"},
    {"text": "Yesterday, my :family_member made :food for :event.", "author": "Luis"},
    {"text": "Once upon a time, a :adjective :hero saved the :noun.", "author": "Daniel"},
    {"text": "The :adjective :weather made me want to :verb all day.", "author": "Yube"},
    {"text": "In the :adjective forest, the :animal found a :object.", "author": "Camila"},
    {"text": "My favorite subject is :subject because it is so :adjective.", "author": "Flavia"},
    {"text": "The :profession said ':quote' before running away.", "author": "Isa"},
    {"text": "At the :event, everyone wore a :adjective :clothing_item.", "author": "Airi"},
    {"text": "I dreamed of a :adjective :creature that wanted to :verb.", "author": "Fabi"},
]

# Set of acceptable yes answers (some peurvian slangs)
yes_answers = {"yes", "y", "sí", "si", "oui", "sure", "yeah", "obvio", "claro", "yara"}

# Set of acceptable yes answers
yes_answers = {"yes", "y", "sí", "si", "oui", "sure", "yeah"}

def play_mad_libs():
    # Make a copy and shuffle to avoid repeating the same template
    templates_copy = templates[:]
    random.shuffle(templates_copy)

    index = 0  # keep track of which template we are on

    while True:
        template = templates_copy[index]
        text = template["text"]
        author = template["author"]

        words = text.split()
        filled_words = {}

        for word in words:
            if word.startswith(":"):
                placeholder = word[1:]  # remove colon
                # Change placeholder for prompt readability
                prompt = placeholder.replace("_", " ")
                while True:
                    user_input = input(f"Please enter a {prompt} (1-30 characters): ").strip().lower()
                    if 1 <= len(user_input) <= 30:
                        filled_words[placeholder] = user_input
                        break
                    else:
                        print("Input must be between 1 and 30 characters.")

        # Build the completed story
        completed_text = []
        for word in words:
            if word.startswith(":"):
                placeholder = word[1:]
                completed_text.append(filled_words[placeholder])
            else:
                completed_text.append(word)

        print("\n" + " ".join(completed_text))
        print(f"\nAuthor: {author}\n")

        # Move to the next template
        index += 1
        if index >= len(templates_copy):
            # Reshuffle when we reach the end
            index = 0
            random.shuffle(templates_copy)

        # Ask if the user wants to play again
        answer = input("Do you want to play again? ").strip().lower()
        if answer not in yes_answers:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_mad_libs()