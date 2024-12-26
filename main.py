DEFAULT_FILE_PATH = "/root/workspace/BootdevBookbot/books/frankenstein.txt"

def main():
    file_txt = ""
    with open(DEFAULT_FILE_PATH) as f:
        file_txt = f.read()

    #print(file_txt)
    return file_txt

def count_words():
    return len(main().split()) 

def count_letters():
    mylist = {}
    for letter in main():
        if letter.isalpha():
            if letter.lower() in mylist:
                mylist[letter.lower()] += 1
            else:
                mylist[letter.lower()] = 1
    return sorted(mylist.items(), key=lambda x:x[1], reverse=True)

def status_report():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words()} words found in the document\n")
    for item in count_letters():
        print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End report ---")

if __name__ == "__main__":
    status_report()
