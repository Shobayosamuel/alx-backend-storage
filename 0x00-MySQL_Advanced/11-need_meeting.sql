-- sql script to create a view
-- the view should containlist of all students under 80

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score<80 AND (last_meeting IS NULL OR last_meeting<ADDDATE(CURDATE(), INTERVAL -1 MONTH));
