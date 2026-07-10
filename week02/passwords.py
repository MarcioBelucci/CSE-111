#I setted a validation for the user input, it checks if the variable password is empty or only have spaces.
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]
   
def main():
    password = input("Enter your password(to quit enter 'q' or 'Q'): ")
    while password != "q" and password != "Q":
        if password.strip() == "":
            print("You can't enter an empty password or only spaces. Try again.")
        else:
            result_password_strength = password_strength(password, min_length=10, strong_length=16)
            print(f"The strength of your password is: {result_password_strength}")
        password = input("Enter your password(to quit enter 'q' or 'Q'): ")
        
def word_complexity(word):
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

def word_has_character(word, character_list):
    for character in word:
        if character in character_list:
            return True    
    return False

def password_strength(password, min_length, strong_length):

        password_length = len(password)
        complexity_score = word_complexity(password)        
        result_wordlist = word_in_file(password, "week02/wordlist.txt", False)
        result_toppasswords = word_in_file(password, "week02/toppasswords.txt", True)
        if result_wordlist == True:
            print("Password is a dictionary word and is not secure.")
            strength = 0        
        elif result_toppasswords == True:
            print("Password is a commonly used password and is not secure.")
            strength = 0
        elif password_length < min_length:
            print("Password is too short and is not secure.")
            strength = 1
        elif password_length > strong_length:
            print("Password is long, length trumps complexity this is a good password.")
            strength = 5
        else:
            strength = 1 + complexity_score
        return strength

def word_in_file(word, filename,case_sensitive=False):
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
        
if __name__ == "__main__":
    main()