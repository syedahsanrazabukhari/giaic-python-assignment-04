def make_sentence(word,p_o_s):
    if p_o_s == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif p_o_s == 1:    
        print(f"It's so nice outside today it makes me want to {word}!")
    elif p_o_s == 2:
        print(f"Looking out my window, the sky is big and {word}!")    
    else:
        print("Unknown part of speech.")    
def main():
    word = input("Enter a word: ")
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word,part_of_speech)

if __name__ == "__main__":
   main()    