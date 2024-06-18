// See https://aka.ms/new-console-template for more information

   int NumIdenticalPairs(int[] nums) {
        int count = 0;
        for(int i=0;i<nums.Length;i++){
            for(int j=i+1;j<nums.Length;j++){
                if(nums[i] == nums[j]){
                    count++;
                }
            }
        }
        return count;
    }
    Console.WriteLine(NumIdenticalPairs([1,2,3,1,1,3]));
