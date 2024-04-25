-- creates a stored procedure that computes
-- & stores the average student score


DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	UPDATE users
	SET aver_sc = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
	WHERE id = user_id;
END //

DELIMITER ;
