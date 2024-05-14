// URL:https://leetcode.com/problems/move-zeroes/description/
var moveZeroes = function(nums) {
    // let mainLen = nums.length
    // let mainIndx = 0
    // while(mainIndx < mainLen){
    //     if(nums[mainIndx] === 0){
    //         for (let j=0;j<nums.length-1;j++){
    //             if(nums[j] === 0){
    //                 nums[j] = nums[j+1]
    //                 nums[j+1] = 0;
    //             }
    //         }
    //         mainLen--;
    //     }else{
    //         mainIndx++;
    //     }


    // }

    let zeros = 0
    for(let i=0;i<nums.length;i++){
        if(nums[i] == 0) zeros++;
        else if(zeros > 0){
            nums[i-zeros] = nums[i]
            nums[i] = 0;
        }
    }
    return nums
};
