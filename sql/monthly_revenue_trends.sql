-- Monthly Revenue Trends
-- Aggregates total sales at month level for trend analysis

SELECT
    DATE_FORMAT(Date, 'yyyy-MM') AS Month,
    SUM(TotalSales) AS MonthlyRevenue
FROM retail_sales
GROUP BY DATE_FORMAT(Date, 'yyyy-MM')
ORDER BY Month;
