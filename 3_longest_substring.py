import traceback
def non_repeating_lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    substring: contiguous(touching,border);non-repeating in this case,
    """
    # edge cases to take care off: len == 0, len == 1, string is unique
    try:
        dict_substrings = {}
        seq = ""
        # now figuring out the characters to check
        i = 0
        while i < len(s):
            check_char = s[i] 
            if check_char not in seq:# if the subsequent characters aren't in the sequence formed already, add it to the sequence seq- current substring formation; check_char- the character that is next in line
                seq += check_char
                i +=1 # move onto the next character
                #print(seq)
                
            else: # store the substring and reset seq and set the pointer to the same index
                dict_substrings[len(dict_substrings)+1] = seq
                seq = ""
                # stay on the same character
                

            
        #print(dict_substrings)
        
        list_substrings = list(dict_substrings.values())
        longestSubstrings = max(list_substrings,key= len)
        #debug print statements:
        #print(list_substrings)
        return len(longestSubstrings)
    except: # edge cases
        if len(s) == 0: # empty string case
            return 0
        else: # unique substring
            return(len(s))


if __name__ == "__main__":
    s1 = "au"
    s2 = "bbbbb"
    s3 = "pwwkew"
    s4 = ""
    s5 = " "

    print(non_repeating_lengthOfLongestSubstring(s1))
    #print(non_repeating_lengthOfLongestSubstring(s2))
    #print(non_repeating_lengthOfLongestSubstring(s3))
    #print(non_repeating_lengthOfLongestSubstring(s4))
    #print(non_repeating_lengthOfLongestSubstring(s5))