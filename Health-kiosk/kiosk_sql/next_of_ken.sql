CREATE TABLE `nextofken` (
  `id` int NOT NULL AUTO_INCREMENT,
  `relationship` enum('mother','father','parent','brother','sister','son','daughter','child','friend','spouse','partner','family member','carer','social worker','guardian','other') NOT NULL,
  `patient_id` varchar(8) NOT NULL,
  `name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  `mobile` int NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `address` varchar(100) NOT NULL,
  `city` varchar(45) NOT NULL,
  `contact_hrs` mediumtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `patient_id_UNIQUE` (`patient_id`),
  UNIQUE KEY `mobile_UNIQUE` (`mobile`),
  CONSTRAINT `patient_id` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=ascii;
