//URL: https://leetcode.com/problems/missing-number/description/
var missingNumber = function(nums) {
    let newSet = new Set(nums) // O(n) time complexity to iterate over the nums array and create the set
    for (let i=0;i<=nums.length;i++){ // O(n) time complexity to iterate over the nums array
        if(!newSet.has(i)) return i
    }
};

// total time complexity is O(2n)
