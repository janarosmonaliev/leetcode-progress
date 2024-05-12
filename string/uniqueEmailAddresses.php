<?php
class Solution
{
    /**
     * @param String[] $emails
     * @return Integer
     */
    function numUniqueEmails($emails)
    {
        $pattern = "/^(.+?)(?:\+.*)?(@.+)/";
        $dot_pattern = "/\./";
        $output = [];
        foreach ($emails as $email) {
            preg_match($pattern, $email, $matches);
            $output[preg_replace($dot_pattern, "", $matches[1]) . $matches[2]] += 1;
        }
        return count($output);
    }
}
