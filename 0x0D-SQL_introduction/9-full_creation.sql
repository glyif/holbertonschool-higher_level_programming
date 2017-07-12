-- full creation
CREATE TABLE IF NOT EXISTS second_table (id INT,
	name VARCHAR(256),
	score INT);
INSERT into `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT into `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT into `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT into `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
