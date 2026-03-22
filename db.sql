/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.27 : Database - doc_tag
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`doc_tag` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `doc_tag`;

/*Table structure for table `acces rights` */

DROP TABLE IF EXISTS `acces rights`;

CREATE TABLE `acces rights` (
  `Ar_id` int NOT NULL AUTO_INCREMENT,
  `User_lid` int NOT NULL,
  `Doc_lid` int NOT NULL,
  PRIMARY KEY (`Ar_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `acces rights` */

insert  into `acces rights`(`Ar_id`,`User_lid`,`Doc_lid`) values 
(1,2,3);

/*Table structure for table `authority` */

DROP TABLE IF EXISTS `authority`;

CREATE TABLE `authority` (
  `Authority_id` int NOT NULL AUTO_INCREMENT,
  `Authority_name` varchar(50) NOT NULL,
  `Place` varchar(50) NOT NULL,
  `Post` varchar(50) NOT NULL,
  `Pin` int NOT NULL,
  `District` varchar(50) NOT NULL,
  `State` varchar(50) NOT NULL,
  `Latitude` varchar(15) NOT NULL,
  `Longitude` varchar(15) NOT NULL,
  `Authority_lid` int NOT NULL,
  `Category` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `Phone` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Description` varchar(50) DEFAULT NULL,
  `Logo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Authority_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `authority` */

insert  into `authority`(`Authority_id`,`Authority_name`,`Place`,`Post`,`Pin`,`District`,`State`,`Latitude`,`Longitude`,`Authority_lid`,`Category`,`City`,`Phone`,`Email`,`Description`,`Logo`) values 
(3,'kottol','kottol','Thrisur',0,'680514','pazhanji','ll','gg',2,'liscence','afsalali350@gmail.com','7902201667','afsalali350@gmail.com','hdhska','/static/Logo/20221203131438.jpg'),
(4,'D','ry','0',0,'0','ry','jtg','hjfg',3,'gtjt','afsalali350@gmail.com','435636363','afsalali350@gmail.com','ytio','/static/Logo/20221205012017.jpg'),
(6,'sanal','admin','h',680514,'Thrisur','kerala','pu','k',7,'aut','dubai','2466865','sanalsuper@gmail.com','sgsdg','/static/Logo/20221217132235.jpg'),
(7,'afsal','1234','',0,'Thrisur','kerala','','k',8,'','kunnamkulam','7902201667','afsalali350@gmail.com','sgsdg','/static/Logo/20221217132551.jpg'),
(8,'afsal','1234','',0,'Thrisur','kerala','','k',9,'','kunnamkulam','7902201667','afsalali350@gmail.com','sgsdg','/static/Logo/20221217132657.jpg'),
(9,'afsal','1234','',0,'Thrisur','kerala','','k',10,'','kunnamkulam','7902201667','afsalali350@gmail.com','sgsdg','/static/Logo/20221217132700.jpg'),
(10,'afsal','1234','',0,'Thrisur','kerala','','k',11,'','kunnamkulam','7902201667','afsalali350@gmail.com','sgsdg','/static/Logo/20221217132704.jpg'),
(11,'naana','ted','ws',0,'123s','dooo','lexde','iugisds',12,'leaderee','sususususu','1234','sususususu','oeded','/static/Logo/20221217133435.jpg'),
(13,'sanal','t','d',123,'w','kerala','l','iugi',14,'leader','dubai','2466865','sanalsuper@gmail.com','o','/static/Logo/20221217133018.jpg'),
(14,'njaasn','t','rdyh',12345,'Thrisur','kerala','ew','we',15,'liscence','kunnamkulam','5675898','afsalali350@gmail.com','sgsdg','/static/Logo/20221217133117.jpg'),
(15,'njaasn','t','rdyh',12345,'Thrisur','kerala','ew','we',16,'liscence','kunnamkulam','5675898','afsalali350@gmail.com','sgsdg','/static/Logo/20221217133219.jpg'),
(16,'kalpana','neythallur','udembalpetta',6795786,'malappuram','kerala','east','west',17,'girl','ponnani','9846760389','kalpanaactor@gmail.com','filimstar','/static/Logo/20221226130243.jpg');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `Complaint_id` int NOT NULL AUTO_INCREMENT,
  `User_lid` int NOT NULL,
  `Date` varchar(20) NOT NULL,
  `Complaint` varchar(200) NOT NULL,
  `Reply` varchar(1000) DEFAULT NULL,
  `Status` varchar(10) NOT NULL,
  PRIMARY KEY (`Complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`Complaint_id`,`User_lid`,`Date`,`Complaint`,`Reply`,`Status`) values 
(1,1,'2022-01-12','nm,lm','helllooooo','Replied'),
(2,2,'2022-01-15','egywew','hiii guys\r\n','Replied'),
(3,2,'2022-12-22','kjgikg','hlh','pending'),
(4,19,'2023-03-14','need some improvement ','pending','pending');

/*Table structure for table `document` */

DROP TABLE IF EXISTS `document`;

CREATE TABLE `document` (
  `Doc_id` int NOT NULL AUTO_INCREMENT,
  `User_lid` int NOT NULL,
  `Authority_lid` int NOT NULL,
  `Document_name` varchar(250) DEFAULT NULL,
  `Description` varchar(50) DEFAULT NULL,
  `Path` varchar(500) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `Date_of_issuing` varchar(20) DEFAULT NULL,
  `Valid_till` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Doc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `document` */

insert  into `document`(`Doc_id`,`User_lid`,`Authority_lid`,`Document_name`,`Description`,`Path`,`Status`,`Date_of_issuing`,`Valid_till`) values 
(1,1,3,'liscenece','jfjdjkd','wgfrg','blocked','1970-01-08','2023-01-06'),
(2,1,17,'afsal','hhh','/static/document/221226-152908Screenshot (5).png','blocked','2022-12-01','2022-12-10'),
(3,19,17,'Document','Medical Report of this person','/static/document/230314-011848An Incremental Training on Deep Learning Face Recognition for M-Learning Online Exam Proctoring.pdf','available','2023-03-14','2024-12-01');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `Feedback_id` int NOT NULL AUTO_INCREMENT,
  `User_lid` int NOT NULL,
  `Date` varchar(20) NOT NULL,
  `Feedback` varchar(200) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`Feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`Feedback_id`,`User_lid`,`Date`,`Feedback`) values 
(1,1,'2022-12-03','gdjhfkjxhlx'),
(2,19,'2023-03-14','goood');

/*Table structure for table `history` */

DROP TABLE IF EXISTS `history`;

CREATE TABLE `history` (
  `History_id` int DEFAULT NULL,
  `Doc_id` int DEFAULT NULL,
  `Viewer_id` int DEFAULT NULL,
  `Date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `history` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `Login_id` bigint NOT NULL AUTO_INCREMENT,
  `Username` varchar(30) NOT NULL,
  `Password` varchar(16) NOT NULL,
  `Login_type` varchar(15) NOT NULL,
  PRIMARY KEY (`Login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`Login_id`,`Username`,`Password`,`Login_type`) values 
(1,'hyguyf','6652','authority'),
(2,'af','7261','user'),
(3,'afsalali350@gmail.com','4321','authority'),
(4,'admin@gmail.com','1234','admin'),
(5,'sanalsuper@gmail.com','9107','authority'),
(6,'afsal','1234','user'),
(7,'sanalsuper@gmail.com','3049','authority'),
(8,'afsalali350@gmail.com','8475','authority'),
(9,'afsalali350@gmail.com','6209','authority'),
(10,'afsalali350@gmail.com','9993','authority'),
(11,'afsalali350@gmail.com','9570','authority'),
(12,'sanalsuper@gmail.com','9913','authority'),
(13,'sanalsuper@gmail.com','4403','authority'),
(14,'sanalsuper@gmail.com','3936','authority'),
(15,'afsalali350@gmail.com','7271','authority'),
(16,'afsalali350@gmail.com','1917','authority'),
(17,'kalpanaactor@gmail.com','kalpu','authority'),
(19,'sam@gmail.com','123','user');

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `Report_id` int NOT NULL AUTO_INCREMENT,
  `User_lid` int NOT NULL,
  `Authority_lid` int NOT NULL,
  `Document_lid` int DEFAULT NULL,
  `Date` date NOT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `Report` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `report` */

insert  into `report`(`Report_id`,`User_lid`,`Authority_lid`,`Document_lid`,`Date`,`Status`,`Report`) values 
(1,3,3,2,'2022-12-21','viewed','xfjkfg'),
(2,1,3,1,'2022-12-08','pending','adfbfb'),
(3,2,3,2,'2022-12-14','viewed','sadfbsfb'),
(4,2,3,2,'2022-12-30','pending',NULL);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `User_id` int NOT NULL AUTO_INCREMENT,
  `User_lid` int DEFAULT NULL,
  `First_name` varchar(50) DEFAULT NULL,
  `Last_name` varchar(50) NOT NULL,
  `Mother's_name` varchar(50) DEFAULT NULL,
  `Father's_name` varchar(50) DEFAULT NULL,
  `Gender` varchar(50) NOT NULL,
  `Dob` varchar(20) NOT NULL,
  `Blood_group` varchar(50) DEFAULT NULL,
  `Nationality` varchar(50) DEFAULT NULL,
  `Place_of_birth` varchar(50) DEFAULT NULL,
  `Place` varchar(50) NOT NULL,
  `Pin` varchar(50) NOT NULL,
  `Post` varchar(50) NOT NULL,
  `City` varchar(50) NOT NULL,
  `State` varchar(50) NOT NULL,
  `Mail_id` varchar(50) NOT NULL,
  `Phone` varchar(50) DEFAULT NULL,
  `Adhar_no` varchar(50) DEFAULT NULL,
  `Pancard_no` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`User_id`,`User_lid`,`First_name`,`Last_name`,`Mother's_name`,`Father's_name`,`Gender`,`Dob`,`Blood_group`,`Nationality`,`Place_of_birth`,`Place`,`Pin`,`Post`,`City`,`State`,`Mail_id`,`Phone`,`Adhar_no`,`Pancard_no`) values 
(1,2,'afsal','ali','ramla','ali','male','2002-10-31','0+','india','kottol','kottol','680542','pazhanji','kunnamkulam','kerala','afs@gmail.comalali35','567476473','7585','534563'),
(2,6,'af','fbh','fgjf','jk','hj','1970-01-14',NULL,NULL,NULL,'','','dfj','jgdf','','eruetuj','9876543555',NULL,NULL),
(3,19,'sam','sepiol ','mrs sepiol ','sepiol ','Male','01-01-2000','A+','Indian','Ramanattukara','Calicut University ','123456','C University ','Calicut ','Kerala ','sam@gmail.com','9876543210','123456789012','1234567890');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
