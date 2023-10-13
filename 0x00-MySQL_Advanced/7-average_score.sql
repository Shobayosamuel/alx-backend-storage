-- create a procedure to that computes and store average for a student
-- An average score can be decimal

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
        DECLARE avg_score FLOAT;
        SET avg_score = (SELECT SUM(score) FROM corrections WHERE corrections.user_id = user_id);
        UPDATE users SET average_score=avg_score WHERE id=user_id;
END
//
DELIMITER ;
