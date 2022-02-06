/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  if (nums.length === 1) return nums[0];

  let sum = nums[0],
    maxSum = nums[0];

  for (let i = 0; i < nums.length; i++) {
    sum = Math.max(nums[i], sum + nums[i]);

    maxSum = Math.max(sum, maxSum);
  }
  return maxSum;
};

let nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];

let ans = maxSubArray(nums);
console.log(ans);
