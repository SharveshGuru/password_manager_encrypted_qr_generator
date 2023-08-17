from fuzzywuzzy import fuzz

# example dictionary
my_dict = {"apple": 1, "banana": 2, "orange": 3}

# function to search for key even with typos
def search_dict(my_dict, key):
    max_score = -1
    closest_match = None
    for dict_key in my_dict:
        score = fuzz.ratio(key, dict_key)
        if score > max_score:
            max_score = score
            closest_match = dict_key
    if max_score < 70:
        print("No match found.")
    else:
        print(f"Did you mean {closest_match}?")
        print(f"The value of {closest_match} is {my_dict[closest_match]}")

# example usage
search_dict(my_dict, "appple") # should suggest 'apple'
search_dict(my_dict, "bananana") # should suggest 'banana'
search_dict(my_dict, "pear") # should not find a match
