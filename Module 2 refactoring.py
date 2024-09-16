import random
import string
from collections import Counter

# 1. generate a list of random number of dictionaries(from 2 to 10), key should be a letter in lowercase(from 2 to 5 e.g.), value should be a number(from 0 to 100)
def generate_random_list_of_dictionaries(min_dicts = 2, max_dicts = 10, min_key = 2, max_key = 5, min_value = 0, max_value = 100):
    return [
        {random.choice(string.ascii_lowercase): random.randint(min_value, max_value) for i in range(random.randint(min_key, max_key))}
        for i in range(random.randint(min_dicts, max_dicts))
    ]
# create a Counter to track how many times each key appears across all dictionaries
def count_keys(dict_list):
    key_counter = Counter()
    for n in dict_list:
        key_counter.update(n.keys())
    return key_counter

# 2. create the common dictionary and track the dictionary number with max value for each key
def create_common_dict(dict_list):
    common_dict = {}
    dict_number = 1

    for i in dict_list:
        for key, value in i.items():
            if key in common_dict:
                # if the key already exists, check if the new value is greater
                if value > common_dict[key][0]:
                    common_dict[key] = (value, dict_number) # store the max value and dict number
            else:
                # if the key is not exist, add it
                common_dict[key] = (value, dict_number)
        # increment the dictionary number
        dict_number +=1

    return common_dict

# create the final dictionary with keys renamed if necessary
def create_final_dict(common_dict, key_counter):
    return {
        f"{key}_{idx}" if key_counter[key] > 1 else key: value
        for key, (value, idx) in common_dict.items()
    }

random_list_of_dictionaries = generate_random_list_of_dictionaries()
key_counter = count_keys(random_list_of_dictionaries)
common_dict = create_common_dict(random_list_of_dictionaries)
final_dict = create_final_dict(common_dict, key_counter)

print(random_list_of_dictionaries)
print(key_counter)
print(common_dict)
print(f"Final dictionary: ", final_dict)