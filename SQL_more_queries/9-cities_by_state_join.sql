--Write a script that lists all cities contained in the database hbtn_0d_usa.
Select
    a.id AS id,
    a.name AS name,
    b.name AS name
FROM
    cities a
    inner join states b ON a.state_id = b.id
ORDER BY
    a.id ASC;