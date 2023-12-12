-- This SQL script retrieves the top score along wiht name from second_table table for scores >= 10.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
