function maxProfit(prices: number[]): number {
  let minPrice = Number.MAX_SAFE_INTEGER;
  let maxProfit = 0;
  for (const price of prices) {
    minPrice = Math.min(minPrice, price);
    maxProfit = Math.max(maxProfit, price - minPrice);
  }
  return maxProfit;
}

function maxProfitTwoPointers(prices: number[]): number {
  if (prices.length < 2) return 0;

  let maxProfit = 0;
  let leftBuy = 0;
  let rightSell = 1;
  while (rightSell < prices.length) {
    const currentPrice = prices[rightSell];
    const buyPrice = prices[leftBuy];

    if (buyPrice < currentPrice) {
      const currentProfit = currentPrice - buyPrice;
      maxProfit = Math.max(currentProfit, maxProfit);
    } else {
      leftBuy = rightSell;
    }
    rightSell++;
  }
  return maxProfit;
}
