-- create a procedure to that computes and store average for a student
-- An average score can be decimal

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
        DECLARE avg_score FLOAT;
        SELECT SUM(score) IN avg_score FROM corrections
        WHERE user_id = user_id;
        UPDATE users SET average_score=avg_score WHERE id=user_id;
END
//
DELIMITER ;
