def word_count(frankenstein_read):
    words = frankenstein_read.split()
    return len(words)


def letter_count(frankenstein_read):
    library_dict = {}
    for letters in frankenstein_read.lower():
        if letters not in library_dict:
            library_dict[letters] = 0
        library_dict[letters] += 1
    return library_dict
        
        
def sort(library_dict):
    sorted_list = []
    for letters in library_dict:
        sorted_list.append({"name": letters, "num": library_dict[letters]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list




