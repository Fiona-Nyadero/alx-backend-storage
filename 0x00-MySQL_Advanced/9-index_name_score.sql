-- Creates an index on a table
-- and the first letter & score

CREATE INDEX idx_name_first_score ON names (name(1), score);
