SELECT Product,
       Region,
       SUM(TotalSales) AS Sales,
       RANK() OVER (PARTITION BY Region ORDER BY SUM(TotalSales) DESC) AS RankInRegion
FROM retail_sales
GROUP BY Product, Region;
