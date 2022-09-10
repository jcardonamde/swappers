-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema swappers
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema swappers
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `swappers` DEFAULT CHARACTER SET utf8 ;
USE `swappers` ;

-- -----------------------------------------------------
-- Table `swappers`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `swappers`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `nickname` VARCHAR(100) NULL,
  `email` VARCHAR(100) NULL,
  `city` TINYINT NULL,
  `password` VARCHAR(255) NULL,
  `image` VARCHAR(150) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `swappers`.`services`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `swappers`.`services` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `type_service` TINYINT NULL,
  `description` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_services_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_services_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `swappers`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `swappers`.`users_want_services`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `swappers`.`users_want_services` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `service_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_want_services_services1_idx` (`service_id` ASC) VISIBLE,
  INDEX `fk_users_want_services_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_want_services_services1`
    FOREIGN KEY (`service_id`)
    REFERENCES `swappers`.`services` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_want_services_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `swappers`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
