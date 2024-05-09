from anagram_checker import AnagramChecker
user_answer = None
while True:
    user_answer = input('Input a word or input "exit" to exit: ').upper()
    if user_answer.lower() == 'exit':
        break
    res = AnagramChecker('Week4/Day5/MiniProject/sowpods.txt')
    if res.is_valid_word(user_answer):
        anagrams = res.get_anagrams(user_answer) 
        print(f'''YOUR WORD : "{user_answer}" \nthis is a valid English word. \nAnagrams for your word: {', '.join(anagrams)}''')