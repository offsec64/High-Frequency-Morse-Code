import key_functions
def print(letter):
    for letter in letters:
         try:
             key_func = getattr(key_functions, letter)
         except:
             print("unable to get function corresponding to key..")
             raise
         key_func()


letters = input("Enter text, then press enter to convert to morse code.") 
print(letters)