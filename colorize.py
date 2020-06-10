class Colorize():
    def __init__(self, word_colors, colors={}):
        self.colors = {
            "Red": "\u001b[31m",
            "Green": "\u001b[32m",
            "Yellow": "\u001b[33m",
            "Blue": "\u001b[34m",
            "Magenta": "\u001b[35m",
            "Cyan": "\u001b[36m",
            "White": "\u001b[37m"
        }
        self.reset = "\u001b[0m"
        self.word_colors = word_colors
        if word_colors:
            self.word_colors.update(word_colors)
        if colors:
            self.colors.update(colors)

    def colorize(self, text):
        list_text = text.split()
        i = 0
        for word in list_text:
            l_word = word.lower()
            for s in ["!",",",".","?"]:
                l_word = l_word.strip(s)
            if l_word in self.word_colors:
                list_text[i] = "%s%s%s" % (self.colors[self.word_colors[l_word]],word,self.reset)
            i += 1
        text = " ".join(list_text)
        return text
    
    def c_print(self, text):
        print(self.colorize(text))

    def c_input(self,text):
        return input(self.colorize(text))
