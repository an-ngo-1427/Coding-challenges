class Solution {
    public static void main(String [] args){
        scoreOfString("hello");
    }

    public static int scoreOfString(String s) {
        int sum = 0;
        for(int i=0;i<s.length()-1;i++){
            System.out.println(s.charAt(i));
            int ascii1 = (int)s.charAt(i);
            int ascii2 = (int) s.charAt(i+1);
            sum += Math.abs(ascii1 - ascii2);
        }
        System.out.println(sum);
        return sum;
    }

    // System.out.println(scoreOfString('hello'));
}
