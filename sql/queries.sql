SELECT
stage,
COUNT(*) as deals,
SUM(value) as total_value
FROM deals
GROUP BY stage
ORDER BY total_value DESC;
