def sort_on(dic):
    return dic["count"]

def word_count(file_contents):
    word_list = file_contents.split()
    return len(word_list)

def char_count(file_contents):
    count_map = {}
    lowered = file_contents.lower()
    
    for char in lowered:
        if not char.isalpha():
            continue
        if char in count_map:
            count_map[char] += 1
        else:
            count_map[char] = 1
    
    count_map_list = []
    for k in count_map:
        item_dict = dict()
        item_dict["char"] = k
        item_dict["count"] = count_map[k]
        count_map_list.append(item_dict)

    count_map_list.sort(reverse=True, key=sort_on)

    return count_map_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wc = word_count(file_contents)
        cm_list = char_count(file_contents)

        print(f"{wc} words found in the document")

        for cm in cm_list:
            char = cm["char"]
            count = cm["count"]
            print(f"The {char} character was found {count} times")


main()

