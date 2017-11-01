-- MySQL dump 10.13  Distrib 5.7.20, for osx10.12 (x86_64)
--
-- Host: localhost    Database: Sweety
-- ------------------------------------------------------
-- Server version	5.7.20

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
-- Table structure for table `vocabulary`
--

DROP TABLE IF EXISTS `vocabulary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vocabulary` (
  `No` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(200) DEFAULT NULL,
  `hiragana` varchar(200) DEFAULT NULL,
  `romaji` varchar(200) DEFAULT NULL,
  `kanji` varchar(200) DEFAULT NULL,
  `category` varchar(200) DEFAULT NULL,
  `example` varchar(1000) DEFAULT NULL,
  `imageUrl` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`No`),
  UNIQUE KEY `constr_ID` (`hiragana`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vocabulary`
--

LOCK TABLES `vocabulary` WRITE;
/*!40000 ALTER TABLE `vocabulary` DISABLE KEYS */;
INSERT INTO `vocabulary` VALUES (1,'to learn, study\n','べんきょう',NULL,NULL,'Suru Verbs',NULL,NULL),(2,'to investigate, inquire\n','ちょうさ',NULL,NULL,'Suru Verbs',NULL,NULL),(3,'to order (goods)\n','ちゅうもん',NULL,NULL,'Suru Verbs',NULL,NULL),(4,'to phone, call\n','でんわ',NULL,NULL,'Suru Verbs',NULL,NULL),(5,'to decrease, drop\n','げんしょう',NULL,NULL,'Suru Verbs',NULL,NULL),(6,'to oppose, be against\n','はんたい',NULL,NULL,'Suru Verbs',NULL,NULL),(7,'to announce\n','はっぴょう',NULL,NULL,'Suru Verbs',NULL,NULL),(8,'to release, be on sale\n','はつばい',NULL,NULL,'Suru Verbs',NULL,NULL),(9,'to reply, answer\n','へんじ',NULL,NULL,'Suru Verbs',NULL,NULL),(10,'to change\n','へんか',NULL,NULL,'Suru Verbs',NULL,NULL),(11,'to translate\n','ほんやく',NULL,NULL,'Suru Verbs',NULL,NULL),(12,'to report\n','ほうこく',NULL,NULL,'Suru Verbs',NULL,NULL),(13,'to print\n','いんさつ',NULL,NULL,'Suru Verbs',NULL,NULL),(14,'to develop\n','かいはつ',NULL,NULL,'Suru Verbs',NULL,NULL),(15,'to check, confirm\n','かくにん',NULL,NULL,'Suru Verbs',NULL,NULL),(16,'to manage, control\n','かんり',NULL,NULL,'Suru Verbs',NULL,NULL),(17,'to complete\n','かんせい',NULL,NULL,'Suru Verbs',NULL,NULL),(18,'to calculate\n','けいさん',NULL,NULL,'Suru Verbs',NULL,NULL),(19,'to get married\n','けっこん',NULL,NULL,'Suru Verbs',NULL,NULL),(20,'to study, research\n','けんきゅう',NULL,NULL,'Suru Verbs',NULL,NULL),(21,'to check, test, inspect\n','けんさ',NULL,NULL,'Suru Verbs',NULL,NULL),(22,'to search\n','けんさく',NULL,NULL,'Suru Verbs',NULL,NULL),(23,'to discuss, study, think over\n','けんとう',NULL,NULL,'Suru Verbs',NULL,NULL),(24,'be absent from\n','けっせき',NULL,NULL,'Suru Verbs',NULL,NULL),(25,'to exchange, replace\n','こうかん',NULL,NULL,'Suru Verbs',NULL,NULL),(26,'to be broken\n','こしょう',NULL,NULL,'Suru Verbs',NULL,NULL),(27,'to contact, get in touch, inform\n','れんらく',NULL,NULL,'Suru Verbs',NULL,NULL),(28,'to practice, drill\n','れんしゅう',NULL,NULL,'Suru Verbs',NULL,NULL),(29,'to divorce\n','りこん',NULL,NULL,'Suru Verbs',NULL,NULL),(30,'to use\n','りよう',NULL,NULL,'Suru Verbs',NULL,NULL),(31,'to travel, make a trip\n','りょこう',NULL,NULL,'Suru Verbs',NULL,NULL),(32,'to cook\n','りょうり',NULL,NULL,'Suru Verbs',NULL,NULL),(33,'to agree, support\n','さんせい',NULL,NULL,'Suru Verbs',NULL,NULL),(34,'to work\n','しごと',NULL,NULL,'Suru Verbs',NULL,NULL),(35,'to have a meal\n','しょくじ',NULL,NULL,'Suru Verbs',NULL,NULL),(36,'to go on a business trip\n','しゅっちょう',NULL,NULL,'Suru Verbs',NULL,NULL),(37,'to get job\n','しゅうしょく',NULL,NULL,'Suru Verbs',NULL,NULL),(38,'to attend\n','しゅっせき',NULL,NULL,'Suru Verbs',NULL,NULL),(39,'to repair, fix\n','しゅうり',NULL,NULL,'Suru Verbs',NULL,NULL),(40,'to consult, discuss, talk with\n','そうだん',NULL,NULL,'Suru Verbs',NULL,NULL),(41,'to graduate\n','そつぎょう',NULL,NULL,'Suru Verbs',NULL,NULL),(42,'to take exercise\n','うんどう',NULL,NULL,'Suru Verbs',NULL,NULL),(43,'to drive\n','うんてん',NULL,NULL,'Suru Verbs',NULL,NULL),(44,'to promise, make an appointment\n','やくそく',NULL,NULL,'Suru Verbs',NULL,NULL),(45,'to reserve, book\n','よやく',NULL,NULL,'Suru Verbs',NULL,NULL),(46,'to import\n','ゆにゅう',NULL,NULL,'Suru Verbs',NULL,NULL),(47,'to export\n','ゆしゅつ',NULL,NULL,'Suru Verbs',NULL,NULL),(48,'to win championship\n','ゆうしょう',NULL,NULL,'Suru Verbs',NULL,NULL),(49,'to increase, grow\n','ぞうか',NULL,NULL,'Suru Verbs',NULL,NULL),(50,'to eat\n','たべます',NULL,NULL,'Regular Verbs',NULL,NULL),(51,'to drink\n','のみます',NULL,NULL,'Regular Verbs',NULL,NULL),(52,'to buy\n','かいます',NULL,NULL,'Regular Verbs',NULL,NULL),(53,'to watch, look, see\n','みます',NULL,NULL,'Regular Verbs',NULL,NULL),(54,'to show\n','みせます',NULL,NULL,'Regular Verbs',NULL,NULL),(55,'to write, draw, paint\n','かきます',NULL,NULL,'Regular Verbs',NULL,NULL),(56,'to send\n','おくります',NULL,NULL,'Regular Verbs',NULL,NULL),(57,'to make, produce, cook\n','つくります',NULL,NULL,'Regular Verbs',NULL,NULL),(58,'to use\n','つかいます',NULL,NULL,'Regular Verbs',NULL,NULL),(59,'to meet / to match, fit\n','あいます',NULL,NULL,'Regular Verbs',NULL,NULL),(60,'to go\n','いきます',NULL,NULL,'Regular Verbs',NULL,NULL),(61,'to come\n','きます',NULL,NULL,'Regular Verbs',NULL,NULL),(62,'to return\n','かえります',NULL,NULL,'Regular Verbs',NULL,NULL),(63,'to have, be at, exist (inanimate object)\n','あります',NULL,NULL,'Regular Verbs',NULL,NULL),(64,'to have, be at, exist (animate object)\n','います',NULL,NULL,'Regular Verbs',NULL,NULL),(65,'to talk, speak\n','はなします',NULL,NULL,'Regular Verbs',NULL,NULL),(66,'to translate\n','やくします',NULL,NULL,'Regular Verbs',NULL,NULL),(67,'to lie down, go to bed\n','ねます',NULL,NULL,'Regular Verbs',NULL,NULL),(68,'to get up, wake up, happen, occur\n','おきます',NULL,NULL,'Regular Verbs',NULL,NULL),(69,'to be broken\n','こわれます',NULL,NULL,'Regular Verbs',NULL,NULL),(70,'to repair, fix\n','なおします',NULL,NULL,'Regular Verbs',NULL,NULL),(71,'to give, present / to raise, lift up\n','あげます',NULL,NULL,'Regular Verbs',NULL,NULL),(72,'to receive, be given\n','もらいます',NULL,NULL,'Regular Verbs',NULL,NULL),(73,'to borrow, rent\n','かります',NULL,NULL,'Regular Verbs',NULL,NULL),(74,'to go up, rise\n','あがります',NULL,NULL,'Regular Verbs',NULL,NULL),(75,'to go down, drop\n','さがります',NULL,NULL,'Regular Verbs',NULL,NULL),(76,'to increase\n','ふえます',NULL,NULL,'Regular Verbs',NULL,NULL),(77,'to decrease\n','へります',NULL,NULL,'Regular Verbs',NULL,NULL),(78,'to learn\n','ならいます',NULL,NULL,'Regular Verbs',NULL,NULL),(79,'to memorize, learn, master\n','おぼえます',NULL,NULL,'Regular Verbs',NULL,NULL),(80,'to teach, inform, notice, let somebody know\n','おしえます',NULL,NULL,'Regular Verbs',NULL,NULL),(81,'to check, investigate\n','しらべます',NULL,NULL,'Regular Verbs',NULL,NULL),(82,'to forget\n','わすれます',NULL,NULL,'Regular Verbs',NULL,NULL),(83,'to begin, start, open\n','はじまります',NULL,NULL,'Regular Verbs',NULL,NULL),(84,'to finish, end\n','おわります',NULL,NULL,'Regular Verbs',NULL,NULL),(85,'to open\n','あけます',NULL,NULL,'Regular Verbs',NULL,NULL),(86,'to close\n','しめます',NULL,NULL,'Regular Verbs',NULL,NULL),(87,'to win\n','かちます',NULL,NULL,'Regular Verbs',NULL,NULL),(88,'to lose (a game)\n','まけます',NULL,NULL,'Regular Verbs',NULL,NULL),(89,'to turn, curve\n','まがります',NULL,NULL,'Regular Verbs',NULL,NULL),(90,'to stop / to stay (the night), lodge\n','とまります',NULL,NULL,'Regular Verbs',NULL,NULL),(91,'to get on, ride\n','のります',NULL,NULL,'Regular Verbs',NULL,NULL),(92,'to get off\n','おります',NULL,NULL,'Regular Verbs',NULL,NULL),(93,'to sit, have a seat\n','すわります',NULL,NULL,'Regular Verbs',NULL,NULL),(94,'to wash\n','あらいます',NULL,NULL,'Regular Verbs',NULL,NULL),(95,'to grill, bake, roast, toast\n','やきます',NULL,NULL,'Regular Verbs',NULL,NULL),(96,'to cut\n','きります',NULL,NULL,'Regular Verbs',NULL,NULL),(98,'to take off (shoes, clothes)\n','ぬぎます',NULL,NULL,'Regular Verbs',NULL,NULL),(99,'to take, get / to take a picture\n','とります',NULL,NULL,'Regular Verbs',NULL,NULL),(100,'to do, play (something)\n','します',NULL,NULL,'Regular Verbs',NULL,NULL);
/*!40000 ALTER TABLE `vocabulary` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-22 16:33:07
