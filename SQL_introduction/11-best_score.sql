-- Script to list records from a specific table in a MySQL database
-- based on a condition, displaying specific columns and ordered by one of the columns.
SELECT
    score,
    name
FROM
    second_table
WHERE
    score >= 10
ORDER BY
    score DESC;