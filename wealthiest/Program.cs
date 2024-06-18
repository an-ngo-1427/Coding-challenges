// https://leetcode.com/problems/richest-customer-wealth/description/
int MaximumWealth(int[][] accounts) {
        int wealthiest = 0;
        for(int i=0;i<accounts.Length;i++){
            int total = 0;
            for (int j=0;j<accounts[i].Length;j++){
                total += accounts[i][j];
            }
            if(total > wealthiest){
                wealthiest = total;
            }
        }
        return wealthiest;
    }
