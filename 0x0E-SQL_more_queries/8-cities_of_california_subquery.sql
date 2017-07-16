-- subquery

SELECT * FROM cities WHERE state_id = (
	SELECT * FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
