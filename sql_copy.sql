-- ex 1

select title from movies

select director from movies

select title, director from movies

select title, year from movies

SELECT * from movies

-- ex 2

SELECT * FROM movies
    where id = 6

SELECT * FROM movies
    where year between 2000 and 2010

SELECT * FROM movies
    where year not between 2000 and 2010

SELECT * FROM movies
    where id between 1 and 5

-- ex 3
SELECT * FROM movies
    where title like "toy story%"

SELECT * FROM movies
    where director = "John Lasseter"

SELECT * FROM movies
    where director != "John Lasseter"

SELECT * FROM movies
    where title LIKE "%WALL-%"

-- ex 4
SELECT distinct director FROM movies
    order by director asc;

SELECT * FROM movies
    order by year desc
    limit 4;

SELECT * FROM movies
    order by title
    limit 5;

SELECT * FROM movies
    order by title
    limit 5 offset 5;

-- ex 5
SELECT city, population 
FROM north_american_cities
    where country like"Canada"

SELECT * FROM north_american_cities
    where country like "united states"
    order by latitude desc

SELECT * FROM north_american_cities
    where longitude < (SELECT longitude FROM north_american_cities WHERE city = 'Chicago')
    order by longitude

SELECT * FROM north_american_cities
    where country like "mexico"
    order by population desc
    limit 2

SELECT * FROM north_american_cities
    where country like "united states"
    order by population desc
    limit 2 offset 2

-- ex 6

SELECT * FROM movies
    inner join boxoffice
    on id = movie_id

SELECT * FROM movies
    inner join boxoffice
    on id = movie_id
    where international_sales > domestic_sales

SELECT * FROM movies
    inner join boxoffice
    on id = movie_id
    order by rating desc

-- ex 7
SELECT distinct building FROM employees

SELECT * FROM buildings

SELECT distinct building_name, role FROM buildings
    left join employees
    on building_name = building

-- ex 8
SELECT name, role FROM employees
    where building is null

SELECT distinct building_name FROM buildings
    left join employees
    on building_name = building
    where building is null

-- ex 9
SELECT title, (domestic_sales + international_sales) / 1000000 AS sales_millions
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id

SELECT title, rating * 10 AS rating_percentage
FROM movies
  JOIN boxoffice
    ON movies.id = boxoffice.movie_id;

SELECT title, year
FROM movies
WHERE year % 2 = 0

-- ex 10
SELECT name, max(years_employed) FROM employees

SELECT role, avg(years_employed) as avg_year
FROM employees
GROUP BY role


SELECT building, sum(years_employed) as total_years
FROM employees
GROUP BY building

-- ex 11
SELECT role, count(*) as num_of_artists
FROM employees
WHERE role = "Artist";

SELECT role, count(role)
FROM employees
GROUP BY role;

SELECT role, sum(years_employed)
FROM employees
GROUP BY role
HAVING role = "Engineer";

-- ex 12
SELECT director, count(id) as movies_count
FROM movies
GROUP BY director;

SELECT director, sum(domestic_sales + international_sales) as total_sales
FROM movies
    INNER JOIN boxoffice
        ON id = movie_id
GROUP BY director;

-- ex 13 
insert into movies 
values (15, "Toy story 4", "Gemma", 2024, 110 )

insert into boxoffice
values (15, 8.7, 340000000, 270000000)

-- ex 14

Update movies
set director = "John Lasseter"
    where id = 2;

Update movies
    set year = 1999
    where id = 3;

Update movies
    set title = "Toy Story 3", director = "Lee Unkrich"
    where id = 11

-- ex 15
SELECT * FROM movies
where year < 2005
DELETE FROM movies
    where year < 2005

SELECT * FROM movies
where director = "Andrew Stanton"
Delete FROM movies
    where director = "Andrew Stanton"

-- ex 16
CREATE TABLE database(
    id INTEGER PRIMARY KEY,
    name TEXT,
    version FLOAT,
    download_count INTEGER
);

-- ex 17
ALTER TABLE movies
ADD aspect_ratio FLOAT

ALTER TABLE movies
ADD Language TEXT
default "English"