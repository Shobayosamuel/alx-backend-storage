-- script to create index on a table
-- it should make use of first letter of the name and score

CREATE INDEX idx_name_first_score ON names (name(1), score);
