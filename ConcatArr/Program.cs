// https://leetcode.com/problems/concatenation-of-array/

     void GetConcatenation(int[] nums) {
        int[] ans = new int[nums.Length*2];
        for(int i=0;i<nums.Length; i++){
            ans[i] = nums[i];
            ans[i+nums.Length] = nums[i];
        }
        // foreach(int num in ans){
        //     Console.WriteLine($"{num}");
        // }
        Console.WriteLine($"{ans}");
    }
    GetConcatenation([1,2,3])
;// Console.Write("printing");
