-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: carnetapp
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `offlineconsults`
--

DROP TABLE IF EXISTS `offlineconsults`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `offlineconsults` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` varchar(45) NOT NULL,
  `TableName` varchar(100) NOT NULL,
  `ColumnName` varchar(1000) NOT NULL,
  `value` varchar(1000) NOT NULL,
  `execute` int NOT NULL,
  `InsertAt` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `offlineconsults`
--

LOCK TABLES `offlineconsults` WRITE;
/*!40000 ALTER TABLE `offlineconsults` DISABLE KEYS */;
INSERT INTO `offlineconsults` VALUES (20,'INSERT','SOLV','NumeroD,hasta,CodClie,CarnetNum2,status','~283263~,~01-01-2024~,~A-10225188~,~0008035590~,1',1,'2023-09-14 17:52:30');
/*!40000 ALTER TABLE `offlineconsults` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `savecarnets`
--

DROP TABLE IF EXISTS `savecarnets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `savecarnets` (
  `CodClie` varchar(10) NOT NULL,
  `template` varchar(100) NOT NULL,
  `apellidos` varchar(500) NOT NULL,
  `nombres` varchar(500) NOT NULL,
  `inpre` varchar(10) NOT NULL,
  `FechaInscripcion` datetime DEFAULT NULL,
  `NumeroInscripcion` varchar(10) DEFAULT NULL,
  `folio` varchar(10) DEFAULT NULL,
  `sangre` varchar(3) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `ImagePath` varchar(500) NOT NULL,
  PRIMARY KEY (`CodClie`),
  UNIQUE KEY `CodClie_UNIQUE` (`CodClie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `savecarnets`
--

LOCK TABLES `savecarnets` WRITE;
/*!40000 ALTER TABLE `savecarnets` DISABLE KEYS */;
INSERT INTO `savecarnets` VALUES ('10.225.188','AbgTemplate.png','LATUF RODRIGUEZ','WILLIAMS DE JESUS','54.668','1994-03-25 00:00:00','3.571','184',NULL,NULL,'ProfilePhotos/cropped/10225188.png'),('26.814.345','AbgTemplate.png','GARCIA GAVIDIA','YXBELY  FERNANDA','320.719','2023-09-12 00:00:00','25.386','14.506',NULL,NULL,'ProfilePhotos/cropped/26.814.345.png'),('27.669.317','AbgTemplate.png','FELIPE DEABREU','MARIA  VICTORIA','320.720','2023-09-12 00:00:00','25.387','14.507',NULL,NULL,'ProfilePhotos/cropped/27.669.317.png');
/*!40000 ALTER TABLE `savecarnets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-15  9:20:28
