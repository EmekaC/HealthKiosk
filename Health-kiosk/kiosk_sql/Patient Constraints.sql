CREATE TABLE `patients` (
  `id` varchar(8) NOT NULL,
  `active` tinyint NOT NULL DEFAULT '1',
  `name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `mobile` int NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(45) NOT NULL,
  `marital_status` enum('Single','Married','Domestic Partnership','Divorced') NOT NULL,
  `siblings` tinyint NOT NULL DEFAULT '0',
  `email` varchar(120) NOT NULL,
  `password` varchar(14) NOT NULL,
  `deceased` tinyint NOT NULL DEFAULT '0',
  `deceased_date` datetime DEFAULT NULL,
  `photo` longblob,
  `general_practitioner` int DEFAULT NULL,
  `managed_organization` varchar(45) DEFAULT NULL,
  `communitcation` enum('English','Maltese','Italian','French') NOT NULL DEFAULT 'English',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `mobile_UNIQUE` (`mobile`),
  KEY `doctor_idx` (`general_practitioner`),
  CONSTRAINT `doctor` FOREIGN KEY (`general_practitioner`) REFERENCES `doctor` (`doctorId`),
  CONSTRAINT `ifDeceased` CHECK ((((`deceased` = 1) and (`deceased_date` is not null)) or ((`deceased` = 0) and (`deceased_date` is null))))
) ENGINE=InnoDB DEFAULT CHARSET=ascii;
SELECT * FROM `health-kiosk`.patients;