CREATE TABLE `doctor_patient` (
  `doctorId` int NOT NULL,
  `patientId` varchar(8) NOT NULL,
  PRIMARY KEY (`doctorId`,`patientId`),
  UNIQUE KEY `doctorId_UNIQUE` (`doctorId`),
  KEY `patient_idx` (`patientId`),
  CONSTRAINT `doctorId` FOREIGN KEY (`doctorId`) REFERENCES `doctor` (`doctorId`),
  CONSTRAINT `patient` FOREIGN KEY (`patientId`) REFERENCES `patient` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=ascii;