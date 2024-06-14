public class Solution {
    public string AddBinary(string a, string b) {
        int i = a.Length - 1;
        int j = b.Length - 1;
        int carry = 0;
        string result = "";
        while(i >= 0 || j >= 0){
            int sum = carry;
            carry = 0;
            if (i>=0){
                sum += a[i] - '0';
            }
            if (j>=0){
                sum += b[j] - '0';
            }
            if(sum >= 2){
                result += '0';
                carry = 1;
            }else{
                result += sum.ToString();
            }

            i--;
            j--;
        }
        if (carry > 0){
            result += carry.ToString();
        }

        string reverseString = "";
        for (int k=result.Length-1; k>= 0;k--){
            reverseString += result[k];
        }


        return reverseString;
    }
}
