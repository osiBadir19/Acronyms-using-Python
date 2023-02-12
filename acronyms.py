class Acronyms:

    def convert_to_acro(self, phrase: str) -> str:
        """
        :param phrase: a <str> of multiple words
        :return: a shortened acronyms <str>
        """
        
        phrase = phrase.split()
        for word in phrase:
            phrase[phrase.index(word)] = word[:1].upper()

        return "".join(phrase)



    def receive_return(self):
        """
        :return: the acronym version of a given phrase
        """
        
        inp = input("please enter the phrase : \n\t")
        out = self.convert_to_acro(inp)
        return out
