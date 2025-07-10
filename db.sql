/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - testingdb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`testingdb` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `testingdb`;

/*Table structure for table `register_data` */

DROP TABLE IF EXISTS `register_data`;

CREATE TABLE `register_data` (
  `id` int(255) NOT NULL,
  `name` varchar(255) default NULL,
  `location` varchar(255) default NULL,
  `degree` varchar(255) default NULL,
  `mobile` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `feedback` longtext,
  `note` longtext,
  `action` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `register_data` */

insert  into `register_data`(`id`,`name`,`location`,`degree`,`mobile`,`email`,`feedback`,`note`,`action`) values (101,'roshan','aroli','MSC CS','9561161391','mundekarroshan566@gmail.com','proper','proper','proper'),(102,'sahil','thurbhe','MSC CS','9632587414','shivam@gmail.com','add data here','add data here','add data here'),(103,'harishwar','aroli','MSC CS','9633258741','hari@gmail.com',NULL,NULL,NULL),(104,'shivam','ghansoli','MSC IT','1478523698','shiva@gmail.com',NULL,NULL,NULL),(105,'ketan','digha','MSC IT','9658741235','ketan@gmail.com','update data','update data','update data');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
