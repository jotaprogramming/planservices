-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-08-2021 a las 20:11:43
-- Versión del servidor: 10.4.20-MariaDB
-- Versión de PHP: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestionclientes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `city`
--

CREATE TABLE `city` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT 'Nombre del municipio',
  `idDepart` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `city`
--

INSERT INTO `city` (`id`, `name`, `idDepart`) VALUES
(1, 'Leticia', 1),
(2, 'Medellín', 2),
(3, 'Arauca', 3),
(4, 'Barranquilla', 4),
(9, 'Cartagena de Indias', 5),
(10, 'Tunja', 6),
(11, 'Manizales', 7),
(12, 'Florencia', 8),
(13, 'Yopal', 9),
(14, 'Popayán', 10),
(15, 'Valledupar', 11),
(16, 'Quibdó', 12),
(17, 'Montería', 13),
(18, 'Bogotá', 14),
(19, 'Inírida', 15),
(20, 'San José del Guaviare', 16),
(21, 'Neiva', 17),
(22, 'Riohacha', 18),
(23, 'Santa Marta', 19),
(24, 'Villavicencio', 20),
(25, 'Pasto', 21),
(26, 'San José de Cúcuta', 22),
(27, 'Mocoa', 23),
(28, 'Armenia', 24),
(29, 'Pereira', 25),
(30, 'San Andrés', 26),
(31, 'Bucaramanga', 27),
(32, 'Sincelejo', 28),
(33, 'Ibagué', 29),
(34, 'Cali', 30),
(35, 'Mitú', 31),
(36, 'Puerto Carreño', 32),
(37, 'Piedecuesta', 27),
(38, 'Girón', 27);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `client`
--

CREATE TABLE `client` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT 'Nombre(s) del cliente',
  `lastname` varchar(255) NOT NULL COMMENT 'Apellidos del cliente',
  `dni` varchar(10) NOT NULL COMMENT 'Número de identificación',
  `date` date NOT NULL COMMENT 'Fecha de nacimiento',
  `idGender` int(11) NOT NULL COMMENT 'Género',
  `tel` varchar(7) NOT NULL COMMENT 'Número del teléfono fijo',
  `phone` varchar(10) NOT NULL COMMENT 'Número del teléfono celular',
  `email` varchar(255) NOT NULL COMMENT 'Correo electrónico',
  `address` varchar(255) NOT NULL COMMENT 'Dirección de la residencia',
  `idDepart` int(11) NOT NULL COMMENT 'Departamento',
  `idMuni` int(11) NOT NULL COMMENT 'Municipio',
  `idPlan` int(11) NOT NULL COMMENT 'Plan adquirido por el usuario.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `client`
--

INSERT INTO `client` (`id`, `name`, `lastname`, `dni`, `date`, `idGender`, `tel`, `phone`, `email`, `address`, `idDepart`, `idMuni`, `idPlan`) VALUES
(21, 'Karen', 'Pineda', '1001123123', '2001-07-12', 1, '6408578', '3019876537', 'karen@gmail.com', 'Cra. 5 # 1 - 3', 30, 34, 8),
(25, 'test', 'test', '123', '2001-07-13', 3, '123', '123', 'test@gmail.com', 'Av. Test # 1-3', 14, 18, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `company`
--

CREATE TABLE `company` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT 'Nombre de la empresa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `company`
--

INSERT INTO `company` (`id`, `name`) VALUES
(1, 'Test'),
(2, 'TIGO'),
(3, 'Claro'),
(4, 'Movistar'),
(5, 'Avantel'),
(6, 'Avantel');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `department`
--

CREATE TABLE `department` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT 'Nombre del departamento'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `department`
--

INSERT INTO `department` (`id`, `name`) VALUES
(1, 'Amazonas'),
(2, 'Antioquia'),
(3, 'Arauca'),
(4, 'Atlántico'),
(5, 'Bolívar'),
(6, 'Boyacá'),
(7, 'Caldas'),
(8, 'Caquetá'),
(9, 'Casanare'),
(10, 'Cauca'),
(11, 'Cesar'),
(12, 'Chocó'),
(13, 'Córdoba'),
(14, 'Cundinamarca'),
(15, 'Guainía'),
(16, 'Guaviare'),
(17, 'Huila'),
(18, 'La Guajira'),
(19, 'Magdalena'),
(20, 'Meta'),
(21, 'Nariño'),
(22, 'Norte de Santander'),
(23, 'Putumayo'),
(24, 'Quindío'),
(25, 'Risaralda'),
(26, 'San Andrés y Providencia'),
(27, 'Santander'),
(28, 'Sucre'),
(29, 'Tolima'),
(30, 'Valle del Cauca'),
(31, 'Vaupés'),
(32, 'Vichada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genre`
--

CREATE TABLE `genre` (
  `id` int(11) NOT NULL,
  `gender` varchar(20) NOT NULL COMMENT 'Género de una persona'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `genre`
--

INSERT INTO `genre` (`id`, `gender`) VALUES
(1, 'Femenino'),
(2, 'Masculino'),
(3, 'No Binario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plans`
--

CREATE TABLE `plans` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL COMMENT 'Nombre del plan',
  `description` varchar(1000) NOT NULL COMMENT 'Descripción del plan',
  `idComp` int(11) NOT NULL COMMENT 'Empresa que ofrece el servicio'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `plans`
--

INSERT INTO `plans` (`id`, `name`, `description`, `idComp`) VALUES
(8, 'Triple Play', 'ARMA TU PLAN\r\nRECIBE MAS BENEFICIOS PARA TU HOGAR Con 3 meses de cortesía Amazon Prime Video\r\n\r\nRecibe 500 min a móviles TIGO y 50 min LDN y otros operadores en tu Telefonía fija\r\n\r\nNuestra comunidad: Llamadas de LDN ilimitadas entre líneas fijas TIGO y EDATEL a nivel nacional sin costo adicional, marcando con el 05.\r\n\r\nElige el plan de TV que más se ajuste a tus necesidades:\r\n\r\nPlanes ONEtv, para que disfrutes contenido en streaming y TV lineal, Decos con funcionalidades premium. Planes con 101 HD + 133 SD + 50 audio\r\n\r\nPlan TV CLASICA HD con 65 canales HD + 133 en SD + 50 audio', 2),
(9, 'DUO PLAY', 'ARMA TU PLAN\r\nRECIBE MAS BENEFICIOS PARA TU HOGAR Con 3 meses de cortesía Amazon Prime Video\r\n\r\nElige el plan de TV que más se ajuste a tus necesidades:\r\n\r\nPlanes ONEtv, para que disfrutes contenido en streaming y TV lineal, Decos con funcionalidades premium. Planes con 101 HD + 133 SD + 50 audio\r\n\r\nPlan TV CLASICA HD con 65 canales HD + 133 en SD + 50 audio', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `user_login` varchar(50) NOT NULL,
  `user_pass` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `user_login`, `user_pass`) VALUES
(1, 'root', 'fed873cb09555c8468abe665ef5221f0'),
(2, 'admin', 'c72c1c1b2d63498df52a9e8e4efc8fa3');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fkiddepart` (`idDepart`);

--
-- Indices de la tabla `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fkiddepart` (`idDepart`),
  ADD KEY `fkidmuni` (`idMuni`),
  ADD KEY `fkidgender` (`idGender`),
  ADD KEY `fkidplans` (`idPlan`);

--
-- Indices de la tabla `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `plans`
--
ALTER TABLE `plans`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fkidcomp` (`idComp`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `city`
--
ALTER TABLE `city`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de la tabla `client`
--
ALTER TABLE `client`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `company`
--
ALTER TABLE `company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `department`
--
ALTER TABLE `department`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT de la tabla `genre`
--
ALTER TABLE `genre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `plans`
--
ALTER TABLE `plans`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `city`
--
ALTER TABLE `city`
  ADD CONSTRAINT `city_ibfk_1` FOREIGN KEY (`idDepart`) REFERENCES `department` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `client`
--
ALTER TABLE `client`
  ADD CONSTRAINT `client_ibfk_1` FOREIGN KEY (`idMuni`) REFERENCES `city` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `client_ibfk_3` FOREIGN KEY (`idDepart`) REFERENCES `department` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `client_ibfk_4` FOREIGN KEY (`idGender`) REFERENCES `genre` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `client_ibfk_5` FOREIGN KEY (`idPlan`) REFERENCES `plans` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `plans`
--
ALTER TABLE `plans`
  ADD CONSTRAINT `plans_ibfk_1` FOREIGN KEY (`idComp`) REFERENCES `company` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
