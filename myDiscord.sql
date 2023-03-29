-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: mydiscord
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `channel`
--

DROP TABLE IF EXISTS `channel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `channel` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `port` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `port` (`port`),
  UNIQUE KEY `nom` (`nom`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `channel`
--

LOCK TABLES `channel` WRITE;
/*!40000 ALTER TABLE `channel` DISABLE KEYS */;
INSERT INTO `channel` VALUES (1,'public',1025),(6,'Swag',1227);
/*!40000 ALTER TABLE `channel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `public`
--

DROP TABLE IF EXISTS `public`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `public` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `public`
--

LOCK TABLES `public` WRITE;
/*!40000 ALTER TABLE `public` DISABLE KEYS */;
INSERT INTO `public` VALUES (1,'[27/03/2023] [11:27:38] Abdul Gaming: bonjour'),(2,'[27/03/2023] [11:29:25] Abdul Gaming: a+'),(3,'[27/03/2023] [11:30:02] test test: salut abdul'),(4,'[27/03/2023] [12:30:57] Abdul Gaming: Oui'),(5,'[27/03/2023] [12:50:28] Abdul Gaming: /liste'),(6,'[27/03/2023] [16:01:46] Abdul Gaming: dd'),(7,'[27/03/2023] [16:46:33] Abdul Gaming: Bonsoir'),(8,'[29/03/2023] [11:18:16] Abdul Gaming: Salutation'),(9,'[29/03/2023] [11:19:12] Abdul Gaming: Salut'),(10,'[29/03/2023] [12:05:33] Abdul Gaming: Boom'),(11,'[29/03/2023] [15:58:00] Abdul Gaming: test'),(12,'[29/03/2023] [16:15:24] Abdul Gaming: Poulet'),(13,'[29/03/2023] [16:50:17] Abdul Gaming: Salutations');
/*!40000 ALTER TABLE `public` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `swag`
--

DROP TABLE IF EXISTS `swag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `swag` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `swag`
--

LOCK TABLES `swag` WRITE;
/*!40000 ALTER TABLE `swag` DISABLE KEYS */;
INSERT INTO `swag` VALUES (1,'[29/03/2023] [16:56:44] Abdul Gaming: Swag');
/*!40000 ALTER TABLE `swag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utilisateurs`
--

DROP TABLE IF EXISTS `utilisateurs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `utilisateurs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `mdp` varchar(255) NOT NULL,
  `id_channel` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mail` (`mail`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilisateurs`
--

LOCK TABLES `utilisateurs` WRITE;
/*!40000 ALTER TABLE `utilisateurs` DISABLE KEYS */;
INSERT INTO `utilisateurs` VALUES (17,'test','test','test','9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08',NULL),(18,'Abdul','Gaming','abab','a667282675f4876021d392aa6592f39dabf718748c4b738563cb9d5dc8f21f24',NULL),(20,'Aziz','Ziz','ziz@mail.fr','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',NULL),(22,'Aziz','Farouk','farouk@mail.fr','863bba74ea78b2b913311420656dedf7603a07ff65ebf0aeb9f15bf27a698838',NULL),(23,'Fab','Rice','rice@mail.fr','1b9bc7b7376e6c5c0f1042dfdd42ac68017d8cee72988967d7c670d40c466c85',NULL),(26,'Paul','Polo','polo@gmail.com','e48d077f523063e4b5652e7a5b2e01eb1fc68f3c4adabcc17d5ec5207ad4536f',NULL),(30,'pipe','pope','pipepope@mail.fr','2a3108c4e5af4b0bbca73901ab25587038583d5161d52f1f4a48998820a5d129',NULL),(33,'pomme','pomme','pomme','9169bf3e501fea19614cacd6d646b50b63aa822bc2360a4db06aee4cd504cb4f',NULL),(34,'poire','poire','poire','e7854e19683638ef65a69119df52e9ae775fecddf0eddcde81d8fc000aa24797',NULL),(38,'poire','poire','poired','e7854e19683638ef65a69119df52e9ae775fecddf0eddcde81d8fc000aa24797',NULL),(39,'ze','ze','ze','33129567e0bd787efb15a26307e5311e06ba66e3b8dbc2206ad59f99780a4d78',NULL),(40,'abc','abc','abc','ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad',NULL),(41,'pol','pol','pol','ae1cd33015b06703de2302e02280e51085c5a1748a8404f5a51ff3f239891d36',NULL),(44,'zo','zo','zo','ed4771b3e3a8fe6f0a67cf467cee229f1ef032354c734a7d2241443ffe780660',NULL),(46,'so','so','so','a1d9890884c1b4b960c279cfe7554a900d169422d6cec980beef67761487d3b9',NULL);
/*!40000 ALTER TABLE `utilisateurs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-29 17:00:09
