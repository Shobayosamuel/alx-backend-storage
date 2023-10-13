-- sql script to create a view
-- the view should containlist of all students under 80

DROP TABLE IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score<80 AND (last_meeting IS ULL OR last_meeting>DATE_SUB(NOW(), INTERVAL 1 MONTH));
