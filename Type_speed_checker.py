import time
import random
from text_tsc import df

def claculate_accuracy(target_text, typed_text):
    correct_chars = 0
    min_text = min(len(target_text), len(typed_text))
    for i in range(min_text):
        if target_text[i] ==typed_text[i]:
            correct_chars += 1
        
    if len(target_text) ==0:
        return 100
    elif len(typed_text) == 0:
        return 0
    accuracy = correct_chars/len(typed_text) * 100
    return max(0.0, min(100.0, accuracy))

def word_per_minute(time_taken, typed_text):
    if time_taken <= 0.0:
        return 0.0
    char_count = len(typed_text)
    word = char_count / 5.0  #taking the ideal number per words as 5
    time_taken_in_minutes = time_taken / 60.0
    wpm = word / time_taken_in_minutes
    return wpm 


def start():
    target_text = random.choice(df)
    print(target_text)


    print("-" * 50)
    print("Welcome to the speedtype checker")
    print("-"*50)
    print("Here is your text")
    print("-"*50)
    print(f"{target_text}\n")
    input("press any key to start:")
    start_time = time.time()

    try:
        typed_text = input("Enter the same text as above:")
    except EOFError:
        print("text canceld")
        return
    end_time = time.time()

    time_taken = end_time - start_time
    wpm = word_per_minute(time_taken, typed_text)
    accuracy = claculate_accuracy(target_text, typed_text)
    print("="*50)
    print("RESULTS")
    print("="*50)
    print(f"Time Taken: {time_taken} seconds")
    print(f"Words per minutes: {wpm} WPM")
    print(f"Accuracy: {accuracy}%")
    print("="*50)

if __name__ == "__main__":
    start()