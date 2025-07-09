translater = {
    "привіт":"hello",
    "допобачення":"goodbye",
    "дякую":"thank you",
    "допоможіть":"help",
    "стіл":"table",
    "крісло":"chair",
    "кіт":"cat",
    "собака":"dog",
    "вовк":"wolf",
    "олівець":"pensil",
}
ask = input('Напишіть слово українською яке вас цікавить і ми дамо вам переклад цього слова англійською!: \n').lower()
if ask in translater:
    print(f'Слово {ask} означає - {translater.get(ask)}')
else:
    print('такого слова немає у нашому перекладачі, вибачте')
