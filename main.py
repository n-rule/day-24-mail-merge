with open('./input/names/invited_names.txt', mode='r') as file:
    list_names = file.read().splitlines()

with open('./input/letters/starting_letter.txt', mode='r') as file:
    example = file.read()

    for name in list_names:
        new_letter = example.replace('[name]', name)
        with open(f'./output/readytosend/{name}.txt', mode='w') as sendfile:
            sendfile.write(new_letter)

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
