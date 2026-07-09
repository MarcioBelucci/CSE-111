#I didn't finished the program yet, then I code pass in the function and comment the other code lines.
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]
   
def main():
    password = input("Enter your password(to quit enter 'q' or 'Q'): ")
    while password != "q" and password != "Q":
        print(f"This is the password: {password}")
        password = input("Enter your password(to quit enter 'q' or 'Q'): ")
        password_strength(password, 10, 16)
        
        

def word_complexity(word):
    """
    count = 0
    if word_has_character(word, LOWER):
        count += 1
    if word_has_character(word, UPPER):
        count += 1
    if word_has_character(word, DIGITS):
        count += 1
    if word_has_character(word, SPECIAL):
        count += 1
    return count
    """
    pass

def word_has_character(word, character_list):
    """
    for character in word:
        if character in character_list:
            return True    
    return False
    """
    pass

def password_strength(password, min_length, strong_length):
        """
        password_length = len(password)
        complexity_score = word_complexity(password)        
        word_in_file(password, "toppasswords.txt", True)
        word_in_file(password, "wordlist.txt", False)
        if word_in_file == False:
            print("Password is a dictionaty word and is not secure.")
            strength = 0
        elif word_in_file == True:
            print("Password is a commonly used password and is not secure.")
            strength = 0
        if password_length < min_length:
            print("Password is too short and is not secure.")
            strength = 1
        elif password_length > strong_length:
            print("Password is long, length trumps complexity this is a good password.")
            strength = 5
        else:
            strength = 1 + complexity_score
        return strength
        """
        pass

def word_in_file(word, filename,case_sensitive=False):
    """
    with open(f"{filename}", "r",encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()
            if case_sensitive == True:
                if word == clean_line:
                    return True
            else:
                if word.lower() == clean_line.lower():
                    return True
        return False 
    """
    pass   

            
if __name__ == "__main__":
    main()