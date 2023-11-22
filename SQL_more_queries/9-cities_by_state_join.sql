--Write a script that lists all cities contained in the database hbtn_0d_usa.
Select
    a.id AS id,
    a.name AS name,
    b.name AS name
FROM
    cities
    INNER JOIN states ON cities.state_id = states.id
ORDER BY
    acities.id ASC;