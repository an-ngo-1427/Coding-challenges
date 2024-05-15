// URL: https://leetcode.com/problems/contains-duplicate/
var containsDuplicate = function(nums) {
    let map = {}
    for  (let num of nums){
        if(!map[num]) {

            map[num] = 1
            console.log(map[num])
        }
        else return true
    }
    return false
};

containsDuplicate([1,2,3,1])
