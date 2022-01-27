const solution = {
  lengthOfLongestSubstring: (s) => {
    let dict = {};
    let longest = 0;
    let start = 0,
      end = 0;

    if (s.length === 1) {
      return 1;
    }

    while (end < s.length) {
      let letter = s.charAt(end);
      if (!dict[letter]) {
        dict[letter] = 1;
      } else {
        dict[letter] += 1;
      }
      while (dict[letter] > 1) {
        dict[s.charAt(start)] -= 1;
        start++;
      }
      longest = Math.max(longest, end - start + 1);
      end++;
    }
    return longest;
  },
};

const answer = solution.lengthOfLongestSubstring("pwwkew");
console.log(answer);
