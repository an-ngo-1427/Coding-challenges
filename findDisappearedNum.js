var findDisappearedNumbers = function(nums) {
    for(let i=0; i<nums.length; i++) {
        const curr = Math.abs(nums[i]);
        if(nums[curr-1] >0) {
            nums[curr-1] *=-1;
        }

    }

    let idx = 0;
    for(let i=0; i<nums.length; i++) {
        if(nums[i] > 0) {
            nums[idx] = i+1;
            idx++;
        }
        console.log(nums)
    }
    return nums.slice(0,idx);
};

findDisappearedNumbers([2,1,3,3])
