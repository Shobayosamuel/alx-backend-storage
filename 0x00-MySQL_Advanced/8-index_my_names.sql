-- script the creates an index
-- the index should comprise the first letter of name

CREATE INDEX idx_name_first ON names (name(1));
