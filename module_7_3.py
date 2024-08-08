punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
class WordsFinder:
    file_names = []
    def __new__(cls, *args, **kwargs):
        for i in args:
            cls.file_names.append(i)
        return object.__new__(cls)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                line = file.read().lower()
                for j in punctuation:
                    if j in line:
                        line = line.replace(j, ' ')
                line = line.split()
                all_words.update({i: line})
        return all_words

    def find(self, word):
        slovarb = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                slovarb.update({name: words.index(word.lower())+1})
        return slovarb

    def count(self, word):
        slovarb = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                slovarb.update({name: words.count(word.lower())})
        return slovarb

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте

'''
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
'''