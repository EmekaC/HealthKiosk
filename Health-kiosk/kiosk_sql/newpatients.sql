CREATE TABLE `patients` (
  `id` varchar(8) NOT NULL,
  `active` tinyint NOT NULL DEFAULT '1',
  `name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phone` int NOT NULL,
  `gender` enum('M','F','O') NOT NULL,
  `birthdate` date NOT NULL,
  `deceased` tinyint NOT NULL DEFAULT '0',
  `deceased_date` datetime DEFAULT NULL,
  `address` varchar(45) NOT NULL,
  `marital_status` enum('Single','Married','Civil Union') NOT NULL,
  `multiple_birth` varchar(45) DEFAULT '0',
  `multiple_birth_pos` varchar(45) DEFAULT NULL,
  `photo` longblob,
  `general_practitioner` int DEFAULT NULL,
  `managed_organization` varchar(45) DEFAULT NULL,
  `communitcation` enum('English','Maltese','Italian','French') NOT NULL,
  `nok` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `phone_UNIQUE` (`phone`),
  KEY `doctor_idx` (`general_practitioner`),
  KEY `next_of_ken_idx` (`nok`),
  CONSTRAINT `doctor` FOREIGN KEY (`general_practitioner`) REFERENCES `doctor` (`doctorId`),
  CONSTRAINT `next_of_ken` FOREIGN KEY (`nok`) REFERENCES `next_of_ken` (`id`),
  CONSTRAINT `ifDeceased` CHECK ((((`deceased` = 1) and (`deceased_date` is not null)) or ((`deceased` = 0) and (`deceased_date` is null)))),
  CONSTRAINT `ifMultiBirth` CHECK ((((`multiple_birth` = 1) and (`multiple_birth_pos` is not null)) or ((`multiple_birth` = 0) and (`multiple_birth_pos` is null))))
) ENGINE=InnoDB DEFAULT CHARSET=ascii;
