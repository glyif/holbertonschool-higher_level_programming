-- lists number of rows with same score
SELECT score, Count(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
