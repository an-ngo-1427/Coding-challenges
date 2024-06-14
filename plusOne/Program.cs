// See https://aka.ms/new-console-template for more information

public class Solution {
    public static void Main(string[] args)
    {
        int[] inputs = [1,2,3];
        int[] results = PlusOne(inputs);
        foreach(int item in results){
            Console.WriteLine(item);
        }
    }

    public static int[] PlusOne(int[] digits) {
        for (int i=digits.Length -1; i>=0;i--){
            digits[i] += 1;
            if(digits[i] <= 9){
                return digits;
            };
            digits[i] = 0;
        };
        int[] newDigits = new int[digits.Length + 1];
        newDigits[0] = 1;
        return newDigits;
    }

    // Console.WriteLine(PlusOne([1,2,3]));
}
