CREATE TABLE `health-kiosk`.`temp` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `temperature` DECIMAL(4,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);