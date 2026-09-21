def word_counter(text):
    text = text.lower()
    
    punctuations = [".", ",", "!", "?", ";", ":", "-", '"', "'", "“", "”"]
    for p in punctuations:
        text = text.replace(p, "")
        
    word_list = text.split()
    
    total_words = len(word_list)
    
    word_counts = {}
    
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    return total_words, word_counts

print("\n ~~~~~~~~~~~~ Welcome to Word Counter ~~~~~~~~~~~~~~~\n")
user_text = input("Enter a sentence or paragraph to count words:")
print("\n")
total_words, result_dict = word_counter(user_text)

print("-" * 30)
print(f"Total Words : {total_words}")
print("-" * 30)

print("\nFor view Full Words Count|Enter--> (yes) ortherwise (No) to exit)\n")
user_choice = input("Yes or No:")

choice = user_choice.lower()

if choice == "yes":
    print("\n--- Count of Different Words ---")
    
    for word, count in result_dict.items():
        print(f"{word} : {count}")
        
elif choice == "no":
    print("\nThanks for using Word Counter\n")
    
else:
    print("Invalid Option,Type only('Yes' or 'No') ")