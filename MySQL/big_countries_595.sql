-- My first guess
-- SELECT 
--     name, population, area
-- FROM 
--     World
-- WHERE 
--     area > 3000000 or population > 25000000
-- ;

-- Second approach, bit faster
SELECT
    name, population, area
FROM
    world
WHERE
    area > 3000000

UNION

SELECT
    name, population, area
FROM
    world
WHERE
    population > 25000000
