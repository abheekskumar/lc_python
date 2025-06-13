import traceback
def repeating_lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    lexicographic_reference = "abcdefghijklmnopkrstuvwxyz"
    sub_string = ""
    dict_substrings = dict()
    for i in range(len(s)):
        try:
            if lexicographic_reference.index(s[i]) <= lexicographic_reference.index(s[i+1]):# if this is true
                if len(sub_string) ==0: # empty string; add both as it's a new instance
                    sub_string += s[i]
                    sub_string += s[i+1]
                else: # not empty; add only the next one as the previous iteration would've already added the character
                    sub_string += s[i+1]
            else:# the next character isn't above this one; close the substring and add the current one to the dictionary
                dict_substrings[len(dict_substrings)+1] = sub_string
                sub_string = ""

        except Exception as e:
            # should only be hit on the character check; we should just add it to dict and reset 
            #print(f"Index position: {i}, Character: {s[i]}, Exception: {e}")
            #print(traceback.format_exc())
            dict_substrings[len(dict_substrings)+1] = sub_string
            sub_string = ""
            
    # print out the longest substring
    list_substrings = list(dict_substrings.values())
    print(list_substrings)
    longest_substring = max(list_substrings,key=len)
    return longest_substring
def non_repeating_lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    lexicographic_reference = "abcdefghijklmnopkrstuvwxyz"
    sub_string = ""
    dict_substrings = dict()
    for i in range(len(s)):
        try:
            if lexicographic_reference.index(s[i]) <= lexicographic_reference.index(s[i+1]):# if this is true
                if len(sub_string) ==0: # empty string; add both as it's a new instance
                    if s[i] not in sub_string:# non-repeating condition
                        sub_string += s[i]
                    if s[i+1] not in sub_string:
                        sub_string += s[i+1]
                else: # not empty; add only the next one as the previous iteration would've already added the character
                    if s[i+1] not in sub_string: # non-repeating condition
                        sub_string += s[i+1]
            else:# the next character isn't above this one; close the substring and add the current one to the dictionary
                dict_substrings[len(dict_substrings)+1] = sub_string
                sub_string = ""

        except Exception as e:
            # should only be hit on the character check; we should just add it to dict and reset 
            #print(f"Index position: {i}, Character: {s[i]}, Exception: {e}")
            #print(traceback.format_exc())
            dict_substrings[len(dict_substrings)+1] = sub_string
            sub_string = ""
            
    # print out the longest substring
    list_substrings = list(dict_substrings.values())
    print(list_substrings)
    longest_substring = max(list_substrings,key=len)
    return len(longest_substring)


if __name__ == "__main__":
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    print(non_repeating_lengthOfLongestSubstring(s1))
    print(non_repeating_lengthOfLongestSubstring(s2))
    print(non_repeating_lengthOfLongestSubstring(s3))