-- creates a table "users"
-- with the id, name and email attributes

CREATE TABLE IF NOT EXISTS users (
	id int AUTO_INCREMENT PRIMARY KEY,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
	);
