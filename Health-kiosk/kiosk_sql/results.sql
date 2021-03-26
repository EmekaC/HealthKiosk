CREATE TABLE `results` (
  `resultNo` int NOT NULL AUTO_INCREMENT,
  `temperature` decimal(4,2) NOT NULL,
  `weight` decimal(5,2) NOT NULL,
  `bloodOx` int NOT NULL,
  `heartRate` int NOT NULL,
  `patientId` varchar(8) NOT NULL,
  PRIMARY KEY (`resultNo`),
  UNIQUE KEY `resultNo_UNIQUE` (`resultNo`),
  KEY `patientID_idx` (`patientId`),
  CONSTRAINT `patientID` FOREIGN KEY (`patientId`) REFERENCES `patient` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=ascii;
