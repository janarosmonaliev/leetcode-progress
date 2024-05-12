<?php
class Solution
{
    /**
     * @param String $word1
     * @param String $word2
     * @return String
     */
    function mergeAlternately($word1, $word2)
    {
        $word1_len = strlen($word1);
        $word2_len = strlen($word2);
        $word1_is_shorter = false;
        if ($word1_len > $word2_len) {
            $shortest_length = $word2_len;
        } else {
            $shortest_length = $word1_len;
            $word1_is_shorter = true;
        }
        $res = "";
        for ($i = 0; $i < $shortest_length; $i++) {
            $res = $res . $word1[$i] . $word2[$i];
        }
        $res = $word1_is_shorter ? $res . substr($word2, $shortest_length) : $res . substr($word1, $shortest_length);

        return $res;
    }
}

// Link https://leetcode.com/problems/merge-strings-alternately
