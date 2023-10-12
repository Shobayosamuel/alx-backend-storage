-- create a procedure to that computes and store average for a student
-- An average score can be decimal

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE scores DECIMAL(10, 2);
	SELECT AVG(score) INTO scores FROM corrections WHERE user_id=user_id;
	INSERT INTO users(id, name, average_score)
	VALUES (user_id, (SELECT name FROM users WHERE id=user_id), scores);
	ON DUPLICATE KEY UPDATE average_score = scores;
END
//
DELIMITER ;
