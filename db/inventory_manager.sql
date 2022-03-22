DROP TABLE IF EXISTS manufacturers CASCADE;
DROP TABLE IF EXISTS products CASCADE;


CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    location VARCHAR(255),
    payment_days VARCHAR(255),
    payment_code VARCHAR(255)    
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    stock_quantity VARCHAR(255),
    buying_cost INT,
    selling_cost INT,
    manufacturer_id INT REFERENCES manufacturers(id)
);