// URL:https://leetcode.com/problems/move-zeroes/description/
const moveZeroes = function(nums) {
    let l=0
    for(let i=0;i<nums.length;i++){
       if (nums[i]){
        const temp = nums[i]
        nums[i] = nums[l]
        nums[l] = temp
        l++;
        }
    }
    return nums
};

console.log(moveZeroes([0,1,0,3,12]))
