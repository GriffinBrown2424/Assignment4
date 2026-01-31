# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

def remove_duplicates_keep_order(values):
    seen = set()
    result = []

    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


# Example test
print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"]))


"""
this challenge I chose did to use a combination of a list and a set to
remove all the duplicates while i kept the original order. The list
keeps the final ordered while the set tracks which ones have already
been seen. This works well because the sets allow time lookups
making it fast at detecting the duplicates

Because this was the timing challenge I was using a fast an reliable
solution rather than making overly complex. The list and set
pattern is a common and a easy approach that is easy to implement
correctly under time. It allowed me to concentrate on correctness and
 while still making it fast

One down side made due to the timeing was assuming that all values in
the input are hashable. this solution demonstrates a good understanding
of choosing appropriate data structures based on the problem requirements.
"""
