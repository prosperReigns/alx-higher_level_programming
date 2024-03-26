-- list all records that has a name
SELECT score, name FROM second_table
WHERE name != ""
ORDER BY score DESC;
