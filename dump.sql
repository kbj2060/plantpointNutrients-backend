-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        8.0.27 - MySQL Community Server - GPL
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  10.3.0.5771
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- nutrient 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `nutrient` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `nutrient`;

-- 테이블 nutrient.humidity 구조 내보내기
CREATE TABLE IF NOT EXISTS `humidity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` varchar(45) DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 테이블 데이터 nutrient.humidity:~32 rows (대략적) 내보내기
DELETE FROM `humidity`;
/*!40000 ALTER TABLE `humidity` DISABLE KEYS */;
INSERT INTO `humidity` (`id`, `value`, `createdAt`) VALUES
	(1, '21', '2021-12-06 01:52:57'),
	(2, '21', '2021-12-06 06:32:28'),
	(3, '21', '2021-12-10 16:51:50'),
	(4, '21', '2021-12-10 16:51:51'),
	(5, '21', '2021-12-10 16:51:52'),
	(6, '21', '2021-12-09 19:52:17'),
	(7, '21', '2021-12-09 19:52:17'),
	(8, '21', '2021-12-09 19:52:17'),
	(9, '21', '2021-12-09 19:52:17'),
	(10, '21', '2021-12-09 19:52:17'),
	(11, '21', '2021-12-09 19:52:17'),
	(12, '21', '2021-12-09 19:52:17'),
	(13, '21', '2021-12-09 19:52:17'),
	(14, '21', '2021-12-09 19:52:17'),
	(15, '21', '2021-12-09 19:52:17'),
	(16, '21', '2021-12-09 19:52:17'),
	(17, '21', '2021-12-09 19:52:17'),
	(18, '21', '2021-12-09 19:52:17'),
	(19, '21', '2021-12-09 19:52:17'),
	(20, '21', '2021-12-09 19:52:17'),
	(21, '21', '2021-12-09 19:52:17'),
	(22, '21', '2021-12-09 19:52:17'),
	(23, '21', '2021-12-09 19:52:17'),
	(24, '21', '2021-12-09 19:52:17'),
	(25, '21', '2021-12-10 00:06:31'),
	(26, '21', '2021-12-10 00:06:31'),
	(27, '21', '2021-12-10 00:06:31'),
	(28, '14', '2021-12-13 00:10:32'),
	(29, '13', '2021-12-13 00:10:33'),
	(30, '145', '2021-12-13 00:10:38'),
	(31, '145', '2021-12-13 00:10:38'),
	(32, '41', '2021-12-14 21:57:03');
/*!40000 ALTER TABLE `humidity` ENABLE KEYS */;

-- 테이블 nutrient.machine 구조 내보내기
CREATE TABLE IF NOT EXISTS `machine` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='					';

-- 테이블 데이터 nutrient.machine:~10 rows (대략적) 내보내기
DELETE FROM `machine`;
/*!40000 ALTER TABLE `machine` DISABLE KEYS */;
INSERT INTO `machine` (`id`, `name`, `createdAt`) VALUES
	(1, 'valve_1', '2021-12-04 16:46:40'),
	(2, 'valve_2', '2021-12-04 16:47:07'),
	(3, 'valve_3', '2021-12-04 16:49:23'),
	(4, 'waterpump_sprayer', '2021-12-05 03:22:51'),
	(5, 'led', '2021-12-05 03:59:25'),
	(6, 'valve_in', '2021-12-06 06:38:18'),
	(7, 'valve_out', '2021-12-14 10:29:04'),
	(8, 'waterpump_a', '2021-12-14 10:29:50'),
	(9, 'waterpump_b', '2021-12-14 10:30:03'),
	(10, 'waterpump_center', '2021-12-19 19:16:02');
/*!40000 ALTER TABLE `machine` ENABLE KEYS */;

-- 테이블 nutrient.nutrientsupply 구조 내보내기
CREATE TABLE IF NOT EXISTS `nutrientsupply` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` float DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 테이블 데이터 nutrient.nutrientsupply:~4 rows (대략적) 내보내기
DELETE FROM `nutrientsupply`;
/*!40000 ALTER TABLE `nutrientsupply` DISABLE KEYS */;
INSERT INTO `nutrientsupply` (`id`, `quantity`, `createdAt`) VALUES
	(1, 12, '2021-12-06 14:31:41'),
	(2, 12, '2021-12-16 00:41:43'),
	(3, 19, '2021-12-16 00:44:40'),
	(4, 30, '2021-12-16 00:57:01');
/*!40000 ALTER TABLE `nutrientsupply` ENABLE KEYS */;

-- 테이블 nutrient.report 구조 내보내기
CREATE TABLE IF NOT EXISTS `report` (
  `id` int NOT NULL AUTO_INCREMENT,
  `level` int DEFAULT NULL,
  `problem` longtext,
  `isFixed` tinyint(1) unsigned zerofill DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 테이블 데이터 nutrient.report:~17 rows (대략적) 내보내기
DELETE FROM `report`;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
INSERT INTO `report` (`id`, `level`, `problem`, `isFixed`, `createdAt`) VALUES
	(12, 3, 'Switch data related to machine data is not existed in AppDevices component.', 0, '2021-12-23 23:33:51'),
	(13, 2, 'Machine or User data are not fit into switches data or switch history are less than 5 in AppTimeline page', 0, '2021-12-24 00:16:30'),
	(14, 2, 'Machine or User data are not fit into switches data or switch history are less than 5 in AppTimeline page', 0, '2021-12-24 00:16:39'),
	(15, 2, 'Machine or User data are not fit into switches data in History page.', 0, '2021-12-24 00:16:47'),
	(16, 2, 'Machine or User data are not fit into switches data in History page.', 0, '2021-12-24 00:16:52'),
	(17, 2, 'Machine or User data are not fit into switches data or switch history are less than 5 in AppTimeline page', 0, '2021-12-24 00:16:55'),
	(18, 2, 'Machine or User data are not fit into switches data or switch history are less than 5 in AppTimeline page', 0, '2021-12-24 00:17:05'),
	(19, 2, 'Machine or User data are not fit into switches data in History page.', 0, '2021-12-24 00:17:09'),
	(20, 2, 'Machine or User data are not fit into switches data or switch history are less than 5 in AppTimeline page', 0, '2021-12-24 00:17:15'),
	(21, 2, 'Machine or User data are not fit into switches data or switch history are less than 5 in AppTimeline page', 0, '2021-12-24 00:17:17'),
	(22, 2, 'Machine or User data are not fit into switches data or switch history are less than 5 in AppTimeline page', 0, '2021-12-24 00:21:38'),
	(23, 2, 'Machine or User data are not fit into switches data in History page.', 0, '2021-12-24 00:21:40'),
	(24, 2, 'Machine or User data are not fit into switches data or switch history are less than 5 in AppTimeline page', 0, '2021-12-24 00:21:54'),
	(25, 2, 'Machine or User data are not fit into switches data or switch history are less than 5 in AppTimeline page', 0, '2021-12-24 00:22:17'),
	(26, 2, 'Machine or User data are not fit into switches data in History page.', 0, '2021-12-24 00:22:23'),
	(27, 2, 'Machine or User data are not fit into switches data or switch history are less than 5 in AppTimeline page', 0, '2021-12-24 00:23:30'),
	(28, 2, 'Machine or User data are not fit into switches data or switch history are less than 5 in AppTimeline page', 0, '2021-12-24 00:23:32');
/*!40000 ALTER TABLE `report` ENABLE KEYS */;

-- 테이블 nutrient.section 구조 내보내기
CREATE TABLE IF NOT EXISTS `section` (
  `id` int NOT NULL,
  `main` varchar(45) DEFAULT NULL,
  `sub` varchar(45) DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='		';

-- 테이블 데이터 nutrient.section:~4 rows (대략적) 내보내기
DELETE FROM `section`;
/*!40000 ALTER TABLE `section` DISABLE KEYS */;
INSERT INTO `section` (`id`, `main`, `sub`, `createdAt`) VALUES
	(1, 's1', 'd1', '2021-12-05 01:47:03'),
	(2, 's1', 'd2', '2021-12-12 22:43:00'),
	(3, 's1', 'd3', '2021-12-12 22:43:00'),
	(4, 's1', 'd4', '2021-12-12 22:43:00');
/*!40000 ALTER TABLE `section` ENABLE KEYS */;

-- 테이블 nutrient.sensor 구조 내보내기
CREATE TABLE IF NOT EXISTS `sensor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='	';

-- 테이블 데이터 nutrient.sensor:~2 rows (대략적) 내보내기
DELETE FROM `sensor`;
/*!40000 ALTER TABLE `sensor` DISABLE KEYS */;
INSERT INTO `sensor` (`id`, `name`, `createdAt`) VALUES
	(1, 'temperature', '2021-12-06 06:37:56'),
	(2, 'humidity', '2021-12-06 06:38:06');
/*!40000 ALTER TABLE `sensor` ENABLE KEYS */;

-- 테이블 nutrient.switch 구조 내보내기
CREATE TABLE IF NOT EXISTS `switch` (
  `id` int NOT NULL AUTO_INCREMENT,
  `machine_id` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `controlledBy_id` int DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=115 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='		';

-- 테이블 데이터 nutrient.switch:~104 rows (대략적) 내보내기
DELETE FROM `switch`;
/*!40000 ALTER TABLE `switch` DISABLE KEYS */;
INSERT INTO `switch` (`id`, `machine_id`, `status`, `controlledBy_id`, `createdAt`) VALUES
	(2, 1, 0, 1, '2021-12-06 05:58:15'),
	(3, 1, 0, 1, '2021-12-06 05:58:35'),
	(4, 1, 0, 1, '2021-12-06 06:32:52'),
	(6, 2, 1, 1, '2021-12-12 00:39:19'),
	(7, 1, 0, 1, '2021-12-12 01:51:46'),
	(8, 1, 1, 1, '2021-12-12 01:51:46'),
	(9, 1, 0, 3, '2021-12-12 01:56:47'),
	(10, 2, 1, 2, '2021-12-12 01:57:13'),
	(11, 1, 0, 1, '2021-12-13 00:30:24'),
	(12, 1, 0, 1, '2021-12-13 00:52:02'),
	(13, 1, 1, 1, '2021-12-13 00:52:29'),
	(14, 2, 0, 2, '2021-12-13 00:52:37'),
	(15, 2, 1, 1, '2021-12-13 00:54:34'),
	(16, 1, 0, 1, '2021-12-13 00:54:43'),
	(17, 2, 0, 1, '2021-12-13 23:17:16'),
	(18, 2, 1, 1, '2021-12-13 23:18:18'),
	(19, 2, 0, 1, '2021-12-13 23:26:36'),
	(20, 1, 1, 1, '2021-12-13 23:31:36'),
	(21, 2, 1, 1, '2021-12-13 23:31:37'),
	(22, 1, 0, 1, '2021-12-13 23:31:40'),
	(23, 2, 0, 1, '2021-12-13 23:31:43'),
	(24, 1, 1, 1, '2021-12-13 23:31:46'),
	(25, 2, 1, 1, '2021-12-13 23:31:50'),
	(26, 2, 0, 1, '2021-12-14 19:16:38'),
	(27, 3, 1, 1, '2021-12-14 19:56:46'),
	(28, 2, 1, 1, '2021-12-14 19:56:47'),
	(30, 6, 1, 1, '2021-12-14 19:56:49'),
	(31, 10, 1, 1, '2021-12-14 19:56:54'),
	(32, 8, 1, 1, '2021-12-14 19:56:54'),
	(33, 5, 1, 1, '2021-12-14 19:56:55'),
	(34, 7, 1, 1, '2021-12-14 19:56:55'),
	(35, 9, 1, 1, '2021-12-14 19:56:56'),
	(36, 2, 0, 1, '2021-12-14 19:57:06'),
	(37, 1, 0, 1, '2021-12-14 19:57:07'),
	(38, 3, 0, 1, '2021-12-14 19:57:07'),
	(40, 5, 0, 1, '2021-12-14 20:14:41'),
	(41, 7, 0, 1, '2021-12-14 20:14:41'),
	(42, 9, 0, 1, '2021-12-14 20:14:42'),
	(43, 1, 1, 1, '2021-12-14 21:27:11'),
	(45, 5, 1, 1, '2021-12-14 21:39:40'),
	(46, 2, 1, 1, '2021-12-14 21:39:53'),
	(48, 3, 1, 1, '2021-12-14 21:39:56'),
	(49, 7, 1, 1, '2021-12-14 21:39:58'),
	(50, 9, 1, 1, '2021-12-14 21:39:59'),
	(51, 10, 0, 1, '2021-12-14 21:40:01'),
	(52, 8, 0, 1, '2021-12-14 21:40:02'),
	(53, 6, 0, 1, '2021-12-14 21:40:03'),
	(55, 2, 0, 1, '2021-12-14 21:40:04'),
	(56, 1, 0, 1, '2021-12-14 21:40:06'),
	(57, 3, 0, 1, '2021-12-14 21:40:06'),
	(58, 5, 0, 1, '2021-12-14 21:40:07'),
	(59, 7, 0, 1, '2021-12-14 21:40:07'),
	(60, 9, 0, 1, '2021-12-14 21:40:08'),
	(61, 1, 1, 1, '2021-12-14 21:58:19'),
	(62, 3, 1, 1, '2021-12-14 21:58:19'),
	(63, 5, 1, 1, '2021-12-14 21:58:20'),
	(64, 7, 1, 1, '2021-12-14 21:58:20'),
	(65, 7, 0, 1, '2021-12-14 22:08:26'),
	(66, 5, 0, 1, '2021-12-14 22:08:27'),
	(67, 3, 0, 1, '2021-12-14 22:08:27'),
	(68, 1, 0, 1, '2021-12-14 22:08:27'),
	(69, 1, 1, 1, '2021-12-14 23:47:48'),
	(70, 3, 1, 1, '2021-12-14 23:47:48'),
	(71, 5, 1, 1, '2021-12-14 23:47:49'),
	(72, 7, 1, 1, '2021-12-14 23:47:49'),
	(73, 9, 1, 1, '2021-12-14 23:47:50'),
	(74, 10, 1, 1, '2021-12-14 23:47:51'),
	(75, 8, 1, 1, '2021-12-14 23:47:51'),
	(76, 6, 1, 1, '2021-12-14 23:47:51'),
	(78, 2, 1, 1, '2021-12-14 23:47:52'),
	(79, 1, 0, 1, '2021-12-16 00:57:39'),
	(80, 3, 0, 1, '2021-12-16 00:57:39'),
	(81, 5, 0, 1, '2021-12-16 00:57:39'),
	(82, 10, 0, 1, '2021-12-18 11:58:11'),
	(83, 10, 1, 1, '2021-12-18 11:58:27'),
	(84, 10, 0, 1, '2021-12-18 12:00:21'),
	(85, 10, 1, 1, '2021-12-21 23:29:19'),
	(86, 5, 1, 1, '2021-12-21 23:29:20'),
	(87, 3, 1, 1, '2021-12-21 23:29:20'),
	(88, 1, 1, 1, '2021-12-21 23:29:21'),
	(89, 7, 0, 1, '2021-12-23 00:26:46'),
	(90, 7, 1, 1, '2021-12-23 00:27:27'),
	(91, 3, 0, 1, '2021-12-23 00:27:43'),
	(92, 7, 0, 1, '2021-12-23 00:28:08'),
	(93, 7, 1, 1, '2021-12-23 00:28:49'),
	(94, 3, 1, 1, '2021-12-23 00:29:08'),
	(95, 7, 0, 1, '2021-12-23 00:29:41'),
	(96, 7, 1, 1, '2021-12-23 00:30:12'),
	(97, 5, 0, 1, '2021-12-23 00:48:49'),
	(98, 3, 0, 1, '2021-12-23 00:48:50'),
	(99, 1, 0, 1, '2021-12-23 00:48:50'),
	(100, 7, 0, 1, '2021-12-23 00:48:51'),
	(101, 9, 0, 1, '2021-12-23 00:48:51'),
	(102, 10, 0, 1, '2021-12-23 00:48:52'),
	(103, 8, 0, 1, '2021-12-23 00:48:53'),
	(104, 6, 0, 1, '2021-12-23 00:48:53'),
	(106, 2, 0, 1, '2021-12-23 00:48:54'),
	(107, 3, 1, 1, '2021-12-23 00:50:16'),
	(108, 1, 1, 1, '2021-12-23 00:50:17'),
	(109, 1, 0, 1, '2021-12-23 23:10:43'),
	(110, 3, 0, 1, '2021-12-23 23:10:44'),
	(111, 9, 1, 1, '2021-12-23 23:11:01'),
	(112, 10, 1, 1, '2021-12-23 23:11:02'),
	(114, 4, 1, 1, '2021-12-23 23:39:40');
/*!40000 ALTER TABLE `switch` ENABLE KEYS */;

-- 테이블 nutrient.temperature 구조 내보내기
CREATE TABLE IF NOT EXISTS `temperature` (
  `id` int NOT NULL AUTO_INCREMENT,
  `value` varchar(45) DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 테이블 데이터 nutrient.temperature:~75 rows (대략적) 내보내기
DELETE FROM `temperature`;
/*!40000 ALTER TABLE `temperature` DISABLE KEYS */;
INSERT INTO `temperature` (`id`, `value`, `createdAt`) VALUES
	(1, '21', '2021-12-06 06:31:54'),
	(2, '21', '2021-12-06 06:31:56'),
	(3, '21', '2021-12-06 06:33:57'),
	(4, '21', '2021-12-10 11:43:23'),
	(5, '21', '2021-12-10 11:43:23'),
	(6, '21', '2021-12-10 11:43:23'),
	(7, '21', '2021-12-10 11:43:23'),
	(8, '21', '2021-12-10 11:43:23'),
	(9, '21', '2021-12-10 11:43:23'),
	(10, '21', '2021-12-10 13:49:01'),
	(11, '21', '2021-12-10 13:49:01'),
	(12, '21', '2021-12-10 13:49:01'),
	(13, '21', '2021-12-10 13:49:01'),
	(14, '21', '2021-12-10 13:56:53'),
	(15, '21', '2021-12-10 13:56:53'),
	(16, '21', '2021-12-10 13:57:03'),
	(17, '1', '2021-12-13 16:46:48'),
	(18, '1', '2021-12-13 16:47:12'),
	(19, '11', '2021-12-14 16:30:40'),
	(20, '21', '2021-12-08 15:34:40'),
	(21, '21', '2021-12-08 15:34:41'),
	(22, '21', '2021-12-08 15:39:00'),
	(23, '21', '2021-12-09 00:41:38'),
	(24, '21', '2021-12-09 00:41:38'),
	(25, '21', '2021-12-09 00:42:22'),
	(26, '21', '2021-12-09 00:42:22'),
	(27, '21', '2021-12-09 00:42:22'),
	(28, '32', '2021-12-09 19:52:17'),
	(29, '32', '2021-12-09 19:52:17'),
	(30, '32', '2021-12-09 19:52:17'),
	(31, '32', '2021-12-09 19:52:17'),
	(32, '32', '2021-12-09 19:52:17'),
	(33, '32', '2021-12-09 19:52:17'),
	(34, '32', '2021-12-09 19:52:17'),
	(35, '32', '2021-12-09 19:52:17'),
	(36, '32', '2021-12-09 19:52:17'),
	(37, '32', '2021-12-09 19:52:17'),
	(38, '32', '2021-12-10 00:06:31'),
	(39, '32', '2021-12-10 00:06:31'),
	(40, '11', '2021-12-12 22:56:26'),
	(41, '11', '2021-12-12 22:56:31'),
	(42, '11', '2021-12-12 22:56:41'),
	(43, '11', '2021-12-12 22:57:50'),
	(44, '11', '2021-12-12 23:03:13'),
	(45, '11', '2021-12-12 23:04:29'),
	(46, '11', '2021-12-12 23:05:12'),
	(47, '11', '2021-12-12 23:05:49'),
	(48, '11', '2021-12-12 23:06:42'),
	(49, '11', '2021-12-12 23:07:23'),
	(50, '11', '2021-12-12 23:08:01'),
	(51, '11', '2021-12-12 23:12:45'),
	(52, '14', '2021-12-12 23:13:23'),
	(53, '14', '2021-12-12 23:14:02'),
	(54, '14', '2021-12-12 23:17:29'),
	(55, '14', '2021-12-12 23:17:40'),
	(56, '14', '2021-12-12 23:17:51'),
	(57, '14', '2021-12-12 23:18:24'),
	(58, '16', '2021-12-12 23:26:13'),
	(59, '16', '2021-12-12 23:28:49'),
	(60, '16', '2021-12-12 23:29:51'),
	(61, '16', '2021-12-12 23:30:08'),
	(62, '16', '2021-12-12 23:30:34'),
	(63, '16', '2021-12-12 23:30:40'),
	(64, '16', '2021-12-12 23:30:49'),
	(65, '16', '2021-12-12 23:33:55'),
	(66, '16', '2021-12-12 23:36:14'),
	(67, '1', '2021-12-12 23:40:57'),
	(68, '1', '2021-12-12 23:41:01'),
	(69, '14', '2021-12-13 00:10:22'),
	(70, '14', '2021-12-13 00:10:25'),
	(71, '11', '2021-12-13 19:21:48'),
	(72, '11', '2021-12-13 19:23:02'),
	(73, '15', '2021-12-13 19:23:33'),
	(74, '14', '2021-12-14 21:52:04'),
	(75, '30', '2021-12-14 21:57:58');
/*!40000 ALTER TABLE `temperature` ENABLE KEYS */;

-- 테이블 nutrient.user 구조 내보내기
CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 테이블 데이터 nutrient.user:~1 rows (대략적) 내보내기
DELETE FROM `user`;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `name`, `email`, `password`, `createdAt`) VALUES
	(1, 'llewyn', 'kbj2060@naver.com', '$2b$12$uz89FGbxgG5RbAN3wFGzAuD1MpyNiULuQhdFuD0aeHJrfKDp2tltC', '2021-12-21 22:36:06');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

-- 테이블 nutrient.watercycle 구조 내보내기
CREATE TABLE IF NOT EXISTS `watercycle` (
  `id` int NOT NULL AUTO_INCREMENT,
  `period` int DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 테이블 데이터 nutrient.watercycle:~2 rows (대략적) 내보내기
DELETE FROM `watercycle`;
/*!40000 ALTER TABLE `watercycle` DISABLE KEYS */;
INSERT INTO `watercycle` (`id`, `period`, `createdAt`) VALUES
	(1, 3, '2021-12-16 00:51:08'),
	(2, 4, '2021-12-16 00:56:40');
/*!40000 ALTER TABLE `watercycle` ENABLE KEYS */;

-- 테이블 nutrient.waterspray 구조 내보내기
CREATE TABLE IF NOT EXISTS `waterspray` (
  `id` int NOT NULL AUTO_INCREMENT,
  `period` int DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 테이블 데이터 nutrient.waterspray:~4 rows (대략적) 내보내기
DELETE FROM `waterspray`;
/*!40000 ALTER TABLE `waterspray` DISABLE KEYS */;
INSERT INTO `waterspray` (`id`, `period`, `createdAt`) VALUES
	(1, 12, '2021-12-06 14:50:32'),
	(2, 12, '2021-12-06 14:51:06'),
	(3, 15, '2021-12-16 00:44:35'),
	(4, 10, '2021-12-16 00:56:55');
/*!40000 ALTER TABLE `waterspray` ENABLE KEYS */;

-- 테이블 nutrient.watersupply 구조 내보내기
CREATE TABLE IF NOT EXISTS `watersupply` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity` float DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 테이블 데이터 nutrient.watersupply:~3 rows (대략적) 내보내기
DELETE FROM `watersupply`;
/*!40000 ALTER TABLE `watersupply` DISABLE KEYS */;
INSERT INTO `watersupply` (`id`, `quantity`, `createdAt`) VALUES
	(1, 12, '2021-12-06 14:22:19'),
	(2, 30, '2021-12-16 00:56:38'),
	(3, 25, '2021-12-16 23:22:48');
/*!40000 ALTER TABLE `watersupply` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
