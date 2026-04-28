-- script that lists all records if the table
-- if record don't have value in name column it will not be listed
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
