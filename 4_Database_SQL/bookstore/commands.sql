-- CREATE DATABASE Bookstore;
-- USE Bookstore;
CREATE TABLE Authors (
    author_id INT NOT NULL,
    author_name VARCHAR(50),
    PRIMARY KEY (author_id)
);
CREATE TABLE Books (
    book_id INT NOT NULL,
    title VARCHAR(50),
    author_id INT NOT NULL,
    PRIMARY KEY (book_id),
    FOREIGN KEY (author_id) REFERENCES Authors (author_id)
);
CREATE TABLE Sales (
    book_id INT NOT NULL,
    units_sold INT,
    unit_price DECIMAL(10, 2),
    PRIMARY KEY (book_id),
    FOREIGN KEY (book_id) REFERENCES Books (book_id)
);
-- SHOW TABLES;

INSERT INTO Authors (author_id, author_name) 
VALUES (1, 'J.K. Rowling'), 
       (2, 'George R. R. Martin'),
       (3, 'Long task man'),
       (4, 'Agatha Christie'), 
       (5, 'Stephen King');

INSERT INTO Books (book_id, title, author_id) 
VALUES (1, 'Harry Potter and the Sorcerer\'s Stone', 1),
       (2, 'Harry Potter and the Chamber of Secrets', 1),
       (3, 'A Game of Thrones', 2),
       (4, 'A Clash of Kings', 2),
       (5, 'The Hobbit', 3),
       (6, 'The Lord of the Rings: The Fellowship of the Ring', 3),
       (7, 'Murder on the Orient Express', 4),
       (8, 'The Murder of Roger Ackroyd', 4),
       (9, 'The Shining', 5),
       (10, 'It', 5);
INSERT INTO Sales (book_id, units_sold, unit_price) 
VALUES (1, 100000, 19.99),
       (2, 95000, 19.99),
       (3, 50000, 29.99),
       (4, 40000, 29.99),
       (5, 150000, 12.99),
       (6, 120000, 15.99),
       (7, 20000, 9.99),
       (8, 25000, 9.99),
       (9, 75000, 24.99),
       (10, 70000, 24.99);
       
SELECT * FROM Authors 
WHERE author_name IS NULL;

SELECT Books.book_id, Books.title, Authors.author_name
FROM Books
INNER JOIN Authors ON Books.author_id = Authors.author_id;

SELECT Books.title, 
       SUM(Sales.units_sold * Sales.unit_price) AS total_sales_revenue
FROM Sales
INNER JOIN Books ON Sales.book_id = Books.book_id
GROUP BY Books.book_id;

SELECT Books.*, Sales.*
FROM Books
INNER JOIN Sales ON Sales.book_id = Books.book_id;
