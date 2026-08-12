def word_replace():
    sentence="Meka ladla meow gop gop gop gop gop gop"
    word_to_replace=input("Enter the word u wanna replace:")
    word_to_replace_with=input("Enter the word u wanna replace with:")
    replaced_sentence=sentence.replace(word_to_replace,word_to_replace_with)
    print(replaced_sentence)
    

    
word_replace()