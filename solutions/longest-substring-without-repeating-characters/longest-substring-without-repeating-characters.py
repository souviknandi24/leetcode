'''
Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/
Author : Souvik Nandi
Date   : 2021-01-02
'''

''' PROBLEM: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPos = 0
        maxLenOfNonRepeatingCharSubStr = 0
        charsPosMap = {}

        for pos in range(len(s)):
            if s[pos] in charsPosMap and leftPos <= charsPosMap[s[pos]]:
                leftPos = charsPosMap[s[pos]] + 1
            else:
                maxLenOfNonRepeatingCharSubStr = max(maxLenOfNonRepeatingCharSubStr, pos - leftPos + 1)
            charsPosMap[s[pos]] = pos
        
        return maxLenOfNonRepeatingCharSubStr
