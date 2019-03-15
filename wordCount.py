txtFile = input("Enter file path: ")


def rowCount(txtFile):
    no_of_rows = 0
    for lines in open(txtFile):
        no_of_rows+=1
    return no_of_rows

def wordCount(txtFile):
    no_of_words = 0
    for lines in open(txtFile):
        words_in_a_line = lines.split(" ")
        for i in words_in_a_line:
            no_of_words+=1
    return no_of_words

if __name__ == "__main__":
    print(rowCount(txtFile))
    print(wordCount(txtFile))
