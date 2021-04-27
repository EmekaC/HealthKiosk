CREATE TABLE `results` (
  `resultNo` int NOT NULL AUTO_INCREMENT,
  `temperature` decimal(4,2) NOT NULL,
  `weight` decimal(5,2) NOT NULL,
  `bloodOx` int NOT NULL,
  `heartRate` int NOT NULL,
  `taken_on` datetime NOT NULL,
  `patientId` varchar(8) NOT NULL,
  `remarks` mediumtext,
  PRIMARY KEY (`resultNo`),
  KEY `patientID_idx` (`patientId`),
  CONSTRAINT `patientId` FOREIGN KEY (`patientId`) REFERENCES `patients` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=ascii;
