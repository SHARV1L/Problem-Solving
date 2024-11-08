class Solution {
    public int maxProfit(int[] prices) {
        int difference = 0;
        int l = prices.length;
        int max = 0;

        for ( int i = 0; i < l-1; i++ ) {
           for ( int j = i + 1; j < l;  j++) {
            difference = prices[j] - prices[i];

            if ( difference > max) max = difference;
           }
        }
        return max;
    }
}