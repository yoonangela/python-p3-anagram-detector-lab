# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word=word

    def match(self, lists):
        word = [let for let in self.word]
        anag=[]
        for wor in lists:
            find = [letter for letter in wor]
            if sorted(find)==sorted(word):
                anag.append(wor)
        return anag
            




# listen = Anagram("listen")
# listen.match(['enlists', 'google', 'inlets', 'banana'])
# # => ['inlets']