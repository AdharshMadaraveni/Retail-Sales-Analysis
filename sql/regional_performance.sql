SELECT Region,
       SUM(TotalSales) AS RegionalSales
FROM retail_sales
GROUP BY Region
ORDER BY RegionalSales DESC;
