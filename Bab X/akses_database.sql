-- MySQL dump 10.11
--
-- Host: localhost    Database: akses_database
-- ------------------------------------------------------
-- Server version	5.0.41-community-nt

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `benua_negara`
--

DROP TABLE IF EXISTS `benua_negara`;
CREATE TABLE `benua_negara` (
  `benua` varchar(25) collate latin1_general_ci NOT NULL,
  `negara` varchar(25) collate latin1_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Dumping data for table `benua_negara`
--

LOCK TABLES `benua_negara` WRITE;
/*!40000 ALTER TABLE `benua_negara` DISABLE KEYS */;
INSERT INTO `benua_negara` VALUES ('ASIA','INDONESIA'),('AFRIKA','NIGERIA'),('AFRIKA','PANTAI GADING'),('EROPA','ALBANIA'),('AUSTRALIA','SELANDIA BARU'),('AMERIKA','SURINAME'),('ASIA','JEPANG');
/*!40000 ALTER TABLE `benua_negara` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biodata_radio`
--

DROP TABLE IF EXISTS `biodata_radio`;
CREATE TABLE `biodata_radio` (
  `nim` varchar(8) collate latin1_general_ci NOT NULL,
  `nama` varchar(25) collate latin1_general_ci NOT NULL,
  `jns_klm` varchar(1) collate latin1_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Dumping data for table `biodata_radio`
--

LOCK TABLES `biodata_radio` WRITE;
/*!40000 ALTER TABLE `biodata_radio` DISABLE KEYS */;
INSERT INTO `biodata_radio` VALUES ('09010250','HILMAN HUDAYA','L'),('09010251','AMBAR NAURA','P'),('09010252','ATTAR RAYHAN','L');
/*!40000 ALTER TABLE `biodata_radio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buku`
--

DROP TABLE IF EXISTS `buku`;
CREATE TABLE `buku` (
  `kd_buku` varchar(5) collate latin1_general_ci NOT NULL,
  `judul` varchar(40) collate latin1_general_ci NOT NULL,
  `penulis` varchar(25) collate latin1_general_ci NOT NULL,
  `penerbit` varchar(25) collate latin1_general_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Dumping data for table `buku`
--

LOCK TABLES `buku` WRITE;
/*!40000 ALTER TABLE `buku` DISABLE KEYS */;
INSERT INTO `buku` VALUES ('001','BELAJAR PYTHON','HILMAN HUDAYA','KOMPUTIKA'),('002','BELAJAR JAVA','HIBBAN HUDAYA','SMART PRESS'),('003','METODE NUMERIK DENGAN JAVA','ABDURRAHMAN','PUSTAKA KREATIF'),('004','METODE NUMERIK DENGAN PYTHON','ABDUR ROFIQ','SMART PRESS'),('005','MOBILE COMPUTING DENGAN PYTHON','ABDUL MUHSIN','KOMPUTIKA'),('006','MOBILE COMPUTING DENGAN C++','ZAKARIYA','SMART PRESS');
/*!40000 ALTER TABLE `buku` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buku_gambar`
--

DROP TABLE IF EXISTS `buku_gambar`;
CREATE TABLE `buku_gambar` (
  `kd_buku` varchar(3) character set latin1 NOT NULL,
  `judul` varchar(25) collate latin1_general_ci NOT NULL,
  `penulis` varchar(25) collate latin1_general_ci NOT NULL,
  `penerbit` varchar(25) collate latin1_general_ci NOT NULL,
  `gambar` varchar(60) character set latin1 NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Dumping data for table `buku_gambar`
--

LOCK TABLES `buku_gambar` WRITE;
/*!40000 ALTER TABLE `buku_gambar` DISABLE KEYS */;
/*!40000 ALTER TABLE `buku_gambar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipk`
--

DROP TABLE IF EXISTS `ipk`;
CREATE TABLE `ipk` (
  `nim` varchar(3) collate latin1_general_ci NOT NULL,
  `nama` varchar(25) collate latin1_general_ci NOT NULL,
  `ipk` float NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Dumping data for table `ipk`
--

LOCK TABLES `ipk` WRITE;
/*!40000 ALTER TABLE `ipk` DISABLE KEYS */;
INSERT INTO `ipk` VALUES ('001','AHMAD',2.7),('002','BUDI',3.32),('003','HILMAN',4);
/*!40000 ALTER TABLE `ipk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operasi_tanggal`
--

DROP TABLE IF EXISTS `operasi_tanggal`;
CREATE TABLE `operasi_tanggal` (
  `nama` varchar(25) collate latin1_general_ci NOT NULL,
  `tgl_lahir` date NOT NULL,
  `tgl_daftar` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

--
-- Dumping data for table `operasi_tanggal`
--

LOCK TABLES `operasi_tanggal` WRITE;
/*!40000 ALTER TABLE `operasi_tanggal` DISABLE KEYS */;
INSERT INTO `operasi_tanggal` VALUES ('ATTAR RAYHAN','2005-01-01','2012-03-24'),('HIBBAN','2011-08-17','2012-03-24');
/*!40000 ALTER TABLE `operasi_tanggal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-04-04  7:27:31
