CREATE TABLE `patient` (
  `id` varchar(8) NOT NULL,
  `name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `dob` date NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(14) NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(45) NOT NULL,
  `mobile` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `mobile_UNIQUE` (`mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=ascii;
