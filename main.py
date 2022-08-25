morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']

text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

finished = False
while not finished:
    translated_text = ""
    human_input = input("insert text to be converted to morse code: ").lower()
    for i in human_input:
        location = text.index(i)
        translated_text += f"{morse_code[location]} "
    print(translated_text)
    repeat = input("type 'no' to stop, otherwise skip: ")
    if repeat == "no":
        finished = True


