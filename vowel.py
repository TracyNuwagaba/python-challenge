string = "Hello Tracy"
vowels = "aeiou"

def countVowels(string, vowels): 
    final = [each for each in string if each in vowels] 
    print(len(final)) 
    print(final) 

countVowels(string, vowels)


