# note that dictionaries preserve sort order in python 3.7+
# https://stackoverflow.com/a/21912744/4292910

# count_by_part_id is a dictionary
sorted_count = {k: v for k, v in reversed(sorted(count_by_part_id.items(), key=lambda item: item[1]))}