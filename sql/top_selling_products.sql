SELECT Product,
       SUM(TotalSales) AS TotalRevenue
FROM retail_sales
GROUP BY Product
ORDER BY TotalRevenue DESC
LIMIT 5;
