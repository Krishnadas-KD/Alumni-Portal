-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 01, 2022 at 07:49 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alumniportal`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `Email` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Pass` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`Email`, `Name`, `Pass`) VALUES
('Ad@gmail.com', 'Admin', '123');

-- --------------------------------------------------------

--
-- Table structure for table `event`
--

CREATE TABLE `event` (
  `id` int(10) NOT NULL,
  `eventname` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `lastdate` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `event`
--

INSERT INTO `event` (`id`, `eventname`, `description`, `lastdate`, `author`, `status`) VALUES
(2, 'add', 'fbn fghbfghfghfg', '2022-06-24', 'sreejithasreenivas@gmail.com', 'Approved'),
(3, 'add', 'fbn fghbfghfghfg', '2022-06-24', 'sreejithasreenivas@gmail.com', 'rejected');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `Email` varchar(50) NOT NULL,
  `Pass` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Regno` int(9) NOT NULL,
  `Admissionno` int(9) NOT NULL,
  `Phoneno` varchar(13) NOT NULL,
  `Department` varchar(50) NOT NULL,
  `academicYear` int(4) NOT NULL,
  `Active` varchar(10) NOT NULL,
  `photo` varchar(500) NOT NULL,
  `id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`Email`, `Pass`, `Name`, `Gender`, `Regno`, `Admissionno`, `Phoneno`, `Department`, `academicYear`, `Active`, `photo`, `id`) VALUES
('kd@gamil.com', '123', 'Krishnadas P V', 'Male', 194654, 4565, '8943114039', 'cio', 2015, 'Active', '../static/profileimage/Untitled\\ design.png', 1),
('sreejithasreenivas@gmail.com', '', 'Krishnadas P V', 'Male', 19130388, 1234, '8943114039', '123', 2312, 'Active', '../static/profileimage/WhatsApp Image 2022-05-19 at 8.54.22 PM.jpeg', 8);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`Email`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `event`
--
ALTER TABLE `event`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
