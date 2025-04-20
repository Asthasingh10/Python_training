
def count_vowels(sentence:str)->int:
    vowels=['a','e','i','o','u']
    count=0;
    for char in sentence:
        if char==vowels:
            count=count+1
    return count;
print(count_vowels("asthasingh"));