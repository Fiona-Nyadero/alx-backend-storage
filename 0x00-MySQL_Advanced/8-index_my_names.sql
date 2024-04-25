-- creates an index on the table
-- and the first letter of a name

CREATE INDEX idx_name_first ON names (LEFT(name, 1));
