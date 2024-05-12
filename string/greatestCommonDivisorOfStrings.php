<?php
class Solution
{
    /**
     * @param String $str1
     * @param String $str2
     * @return String
     */
    function gcdOfStrings($str1, $str2)
    {
        $str1_len = strlen($str1);
        $str2_len = strlen($str2);

        if ($str1_len > $str2_len) {
            return substr($str1, 0, $str2_len) == $str2 ?
                self::gcdOfStrings(substr($str1, $str2_len), $str2) : "";
        } else if ($str2_len > $str1_len) {
            return substr($str2, 0, $str1_len) == $str1 ?
                self::gcdOfStrings(substr($str2, $str1_len), $str1) : "";
        } else {
            return $str1 == $str2 ? $str1 : "";
        }
    }
}

// Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
// The code does string GCD recursively, 
// passing the remainder of a longer string on each recursive level
// until the divisor and divider are the same, if not, returns an empty string.