class coding:
    '''
    This class carries Most of the functions that other Coding Algorithms would use.
    IN SOME OCCUASIONS THE 'self' VARIABLE SHOULD BE SENT TO THE FUNCTIONS.
    '''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    def splitter(self, phrase = ""):
        '''
        'splitter' function splittes the spaces from words and returns a string without spaces, with low case characters, without numbers and without special characters.
        '''
        phrase = phrase.lower()
        x = phrase.split(" ")
        y = ""
        z = ""
        for i in x:
            y += i
        for i in y:
            if i in self.alphabet:
                z += i
        return z
    def remove_repetition(self, phrase = ""):
        '''
        'remove_repetition' This Function removes repated chataters in a phrase and returns the result with low case characters.
        '''
        result = ""
        seen = []
        phrase = phrase.lower()
        for char in phrase:
            if char not in seen:
                result += char
                seen.append(char)
        
        return result
    def replace(self, index = 0, character = "", string = ""):
        '''
        this function takes a string, charcter and an index then replace the character with in the string with the new one and returns the string back.
        '''
        char_list = list(string)
        char_list[index] = character
        # Convert the list back to a string
        return ''.join(char_list)

    
#Example usage:
if __name__ == "__main__":
    x = coding
    y = x.splitter(x, "Hello World, I am a cypher#$%;.")
    print(y)

    y = x.remove_repetition(x, y)
    print(y)
    print(len(x.alphabet))