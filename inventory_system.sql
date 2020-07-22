-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 22, 2020 at 03:13 PM
-- Server version: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `inventory_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE IF NOT EXISTS `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `loc_name` varchar(11) NOT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=20 ;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`location_id`, `loc_name`) VALUES
(14, 'Pune'),
(15, 'Mumbai'),
(16, 'Bangalore'),
(17, 'Hyderabad'),
(18, 'Nagpur'),
(19, 'Nanded');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE IF NOT EXISTS `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `p_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=42 ;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `p_name`) VALUES
(31, 'Laptop'),
(32, 'Mouse'),
(33, 'Keyboard'),
(34, 'Pendrive'),
(35, 'Mobile'),
(39, 'Router'),
(40, 'Charger'),
(41, 'Charger');

-- --------------------------------------------------------

--
-- Table structure for table `productmovement`
--

CREATE TABLE IF NOT EXISTS `productmovement` (
  `movement_id` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `from_location` varchar(11) DEFAULT NULL,
  `to_location` varchar(11) DEFAULT NULL,
  `qty` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  PRIMARY KEY (`movement_id`),
  KEY `product_id` (`product_id`),
  KEY `location_id` (`location_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=57 ;

--
-- Dumping data for table `productmovement`
--

INSERT INTO `productmovement` (`movement_id`, `timestamp`, `from_location`, `to_location`, `qty`, `product_id`, `location_id`) VALUES
(18, '2020-03-20 17:18:23', 'Pune', 'Mumbai', 1200, 31, 14),
(19, '2020-03-20 17:18:45', 'Bangalore', 'Pune', 2500, 33, 16),
(21, '2020-03-20 17:21:34', 'Hyderabad', 'Bangalore', 1700, 35, 17),
(22, '2020-03-20 18:11:36', NULL, 'Nagpur', 4000, 34, 18),
(23, '2020-03-20 18:15:01', 'Bangalore', NULL, 500, 35, 16),
(26, '2020-03-20 18:18:34', NULL, 'Nagpur', 3200, 34, 18),
(27, '2020-03-20 18:18:52', 'Pune', 'Hyderabad', 2000, 32, 14),
(28, '2020-03-20 18:19:09', 'Nagpur', 'Mumbai', 5000, 33, 15),
(29, '2020-03-21 09:40:29', 'Hyderabad', NULL, 1400, 34, 17),
(30, '2020-03-21 09:41:19', NULL, 'Mumbai', 700, 31, 15),
(31, '2020-03-21 09:41:35', NULL, 'Pune', 8000, 33, 14),
(32, '2020-03-21 09:42:01', 'Nagpur', NULL, 4500, 32, 18),
(33, '2020-03-21 09:42:15', NULL, 'Pune', 8500, 34, 14),
(34, '2020-03-21 09:43:11', NULL, 'Bangalore', 4500, 35, 16),
(35, '2020-03-21 09:43:25', NULL, 'Pune', 7500, 35, 14),
(36, '2020-03-21 09:43:35', 'Bangalore', 'Mumbai', 3000, 34, 16),
(37, '2020-03-21 09:43:57', NULL, 'Nagpur', 5400, 32, 18),
(38, '2020-03-21 09:44:13', NULL, 'Hyderabad', 1100, 32, 17),
(39, '2020-03-21 09:45:22', 'Nagpur', NULL, 3100, 33, 18),
(40, '2020-03-21 09:45:34', 'Pune', 'Mumbai', 2300, 31, 15),
(41, '2020-03-21 11:34:54', NULL, 'Pune', 7800, 34, 14),
(42, '2020-03-21 11:55:10', NULL, 'Hyderabad', 234, 31, 17),
(43, '2020-03-21 12:04:17', 'Hyderabad', 'Pune', 11, 31, 14),
(44, '2020-03-21 12:04:41', NULL, 'Bangalore', 23, 31, 16),
(45, '2020-03-21 12:04:59', 'Bangalore', NULL, 500, 33, 16),
(46, '2020-03-21 12:05:57', 'Bangalore', NULL, 1700, 31, 16),
(47, '2020-03-21 12:11:22', NULL, 'Pune', 5000, 31, 14),
(48, '2020-03-21 12:11:42', 'Hyderabad', 'Bangalore', 4000, 31, 16),
(50, '2020-03-21 12:12:40', 'Mumbai', 'Hyderabad', 2000, 31, 17),
(51, '2020-03-21 12:13:02', 'Mumbai', 'Hyderabad', 2000, 31, 17),
(52, '2020-07-22 10:03:01', 'Nanded', 'Bangalore', 555, 39, 16),
(53, '2020-07-22 10:03:35', 'Bangalore', 'Hyderabad', 100, 39, 17),
(54, '2020-07-22 16:00:45', 'Hyderabad', 'Pune', 90, 39, 14),
(55, '2020-07-22 16:01:28', 'Pune', 'Nagpur', 40, 39, 18),
(56, '2020-07-22 16:02:10', 'Pune', 'Nagpur', 100, 39, 18);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `productmovement`
--
ALTER TABLE `productmovement`
  ADD CONSTRAINT `productmovement_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`),
  ADD CONSTRAINT `productmovement_ibfk_2` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
