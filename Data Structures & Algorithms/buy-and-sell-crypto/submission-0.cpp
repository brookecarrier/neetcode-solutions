class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int maxProfit = 0;
        int profit;
        if (prices.size() == 1) return maxProfit;

        int left = 0;
        int right = 1;

        // [10,1,5,6,7,1]
        while (right < prices.size()) {
            if (prices[right] > prices[left]) {
                profit = prices[right] - prices[left];
                if (profit > maxProfit) {
                    maxProfit = profit;
                }
                right++;
            } else {
                left = right;
                right++;
            }

        }

        return maxProfit;
    }
};
