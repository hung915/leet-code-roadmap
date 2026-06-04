public class BestTimeToBuySellStock {
    public static int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int price : prices) {
            minPrice = Math.min(minPrice, price);
            maxProfit = Math.max(maxProfit, price - minPrice);
        }
        return maxProfit;
    }

    public static int maxProfitTwoPointers(int[] prices) {
        int maxProfit = 0;
        if (prices.length < 2)
            return maxProfit;

        int leftBuy = 0;
        int rightSell = 1;

        while (rightSell < prices.length) {
            int sellPrice = prices[rightSell];
            int buyPrice = prices[leftBuy];

            if (buyPrice < sellPrice) {
                int currentProfit = sellPrice - buyPrice;
                maxProfit = Math.max(maxProfit, currentProfit);
            } else
                leftBuy = rightSell;

            rightSell++;
        }
        return maxProfit;
    }
}
