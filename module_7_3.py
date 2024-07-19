class WordsFinder:
    def __init__(self, *file):
        self.file_names = file




    def get_all_words(self):
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_word = {}


        for i in range(len(self.file_names)):
            a = []


            with open(self.file_names[i]) as file:
                file_list = file.readlines()

                for k in range(len(file_list)):
                    string = file_list[k]
                    for z in range(len(punct)):
                        string = string.replace("\n", '')
                        string=string.replace(punct[z],'')
                    list_word = string.split()
                    a = a + list_word

            all_word[self.file_names[i]]=a


        return all_word
    def find(self,word):
        a= {}
        list1 = list(self.get_all_words().items())
        for i in range(len(list1)):
            if word in list1[i][1]:
                a[list1[i][0]] = list1[i][1].index(word)+1

        return a
    def count(self,word):
        a={}
        list1 = list(self.get_all_words().items())
        for i in range(len(list1)):
            a[list1[i][0]] = list1[i][1].count(word)
        return a







