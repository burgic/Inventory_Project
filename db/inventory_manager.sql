DROP TABLE IF EXISTS manufacturers;
DROP TABLE IF EXISTS product;

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    stock_quantity VARCHAR(255),
    buying_cost INT,
    manufacturer VARCHAR(255)
);

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    location VARCHAR(255)
    payment_code VARCHAR(255)
)
