-- Top three temerture city
SELECT city, avg(value) as avg_temp
FROM temperatures 
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;