CREATE TABLE `heart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `heartbeat` int NOT NULL,
  `oxygen` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=ascii;
