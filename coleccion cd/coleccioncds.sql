-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 06-11-2020 a las 08:19:27
-- Versión del servidor: 10.5.6-MariaDB-1:10.5.6+maria~focal
-- Versión de PHP: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `coleccioncds`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autores`
--

CREATE TABLE `autores` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `id_nacionalidad` int(11) NOT NULL,
  `id_discografica` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `autores`
--

INSERT INTO `autores` (`id`, `nombre`, `id_nacionalidad`, `id_discografica`) VALUES
(1, 'David Guetta', 4, 3),
(2, 'Kid Cudi', 3, 2),
(3, 'Andrea Bocelli', 2, 1),
(4, 'Julio Jaramillo', 5, 2),
(5, 'Shakira', 6, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cds`
--

CREATE TABLE `cds` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `id_idioma` int(11) NOT NULL,
  `año_compra` year(4) NOT NULL,
  `id_persona` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `cds`
--

INSERT INTO `cds` (`id`, `nombre`, `id_idioma`, `año_compra`, `id_persona`) VALUES
(1, 'memories', 3, 2010, 3),
(2, 'Donde estan los ladrones', 1, 1998, 1),
(3, 'La historia', 1, 2000, 4),
(4, 'Aria', 2, 2005, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `discografica`
--

CREATE TABLE `discografica` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `discografica`
--

INSERT INTO `discografica` (`id`, `nombre`) VALUES
(1, 'universal music'),
(2, 'sony music'),
(3, 'warner music'),
(4, 'pina records');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `generos`
--

CREATE TABLE `generos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `generos`
--

INSERT INTO `generos` (`id`, `nombre`) VALUES
(1, 'rock'),
(2, 'hip hop'),
(3, 'pasillo'),
(4, 'vallenato'),
(5, 'pop'),
(6, 'bachata'),
(7, 'clasico');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `idiomas`
--

CREATE TABLE `idiomas` (
  `id` int(11) NOT NULL,
  `lengua` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `idiomas`
--

INSERT INTO `idiomas` (`id`, `lengua`) VALUES
(1, 'castellano'),
(2, 'italiano'),
(3, 'ingles'),
(4, 'frances');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nacionalidades`
--

CREATE TABLE `nacionalidades` (
  `id` int(11) NOT NULL,
  `nacionalidad` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `nacionalidades`
--

INSERT INTO `nacionalidades` (`id`, `nacionalidad`) VALUES
(1, 'español'),
(2, 'italiano'),
(3, 'estadounidense'),
(4, 'frances'),
(5, 'ecuatoriano'),
(6, 'colombiano');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

CREATE TABLE `persona` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `persona`
--

INSERT INTO `persona` (`id`, `nombre`) VALUES
(1, 'Erica'),
(2, 'Julio'),
(3, 'Arnold'),
(4, 'Sofia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiene_autor`
--

CREATE TABLE `tiene_autor` (
  `id_autor` int(11) NOT NULL,
  `id_cd` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `tiene_autor`
--

INSERT INTO `tiene_autor` (`id_autor`, `id_cd`) VALUES
(1, 1),
(2, 1),
(3, 4),
(4, 3),
(5, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiene_generos`
--

CREATE TABLE `tiene_generos` (
  `id_cd` int(11) NOT NULL,
  `id_genero` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `tiene_generos`
--

INSERT INTO `tiene_generos` (`id_cd`, `id_genero`) VALUES
(1, 2),
(1, 5),
(2, 1),
(2, 5),
(3, 3),
(4, 7);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_id_nacionalidad_autor` (`id_nacionalidad`),
  ADD KEY `fk_id_discografica_autor` (`id_discografica`);

--
-- Indices de la tabla `cds`
--
ALTER TABLE `cds`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_id_idioma_cd` (`id_idioma`),
  ADD KEY `fk_id_persona` (`id_persona`);

--
-- Indices de la tabla `discografica`
--
ALTER TABLE `discografica`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `generos`
--
ALTER TABLE `generos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `idiomas`
--
ALTER TABLE `idiomas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `nacionalidades`
--
ALTER TABLE `nacionalidades`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `persona`
--
ALTER TABLE `persona`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tiene_autor`
--
ALTER TABLE `tiene_autor`
  ADD PRIMARY KEY (`id_autor`,`id_cd`),
  ADD KEY `fk_id_cd_tiene_autor` (`id_cd`);

--
-- Indices de la tabla `tiene_generos`
--
ALTER TABLE `tiene_generos`
  ADD PRIMARY KEY (`id_cd`,`id_genero`),
  ADD KEY `fk_id_genero_tiene_generos` (`id_genero`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autores`
--
ALTER TABLE `autores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `cds`
--
ALTER TABLE `cds`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `discografica`
--
ALTER TABLE `discografica`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `generos`
--
ALTER TABLE `generos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `idiomas`
--
ALTER TABLE `idiomas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `nacionalidades`
--
ALTER TABLE `nacionalidades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `persona`
--
ALTER TABLE `persona`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `autores`
--
ALTER TABLE `autores`
  ADD CONSTRAINT `fk_id_discografica_autor` FOREIGN KEY (`id_discografica`) REFERENCES `discografica` (`id`),
  ADD CONSTRAINT `fk_id_nacionalidad_autor` FOREIGN KEY (`id_nacionalidad`) REFERENCES `nacionalidades` (`id`);

--
-- Filtros para la tabla `cds`
--
ALTER TABLE `cds`
  ADD CONSTRAINT `fk_id_idioma_cd` FOREIGN KEY (`id_idioma`) REFERENCES `idiomas` (`id`),
  ADD CONSTRAINT `fk_id_persona` FOREIGN KEY (`id_persona`) REFERENCES `persona` (`id`);

--
-- Filtros para la tabla `tiene_autor`
--
ALTER TABLE `tiene_autor`
  ADD CONSTRAINT `fk_id_autores_tiene_autor` FOREIGN KEY (`id_autor`) REFERENCES `autores` (`id`),
  ADD CONSTRAINT `fk_id_cd_tiene_autor` FOREIGN KEY (`id_cd`) REFERENCES `cds` (`id`);

--
-- Filtros para la tabla `tiene_generos`
--
ALTER TABLE `tiene_generos`
  ADD CONSTRAINT `fk_id_cd_tiene_generos` FOREIGN KEY (`id_cd`) REFERENCES `cds` (`id`),
  ADD CONSTRAINT `fk_id_genero_tiene_generos` FOREIGN KEY (`id_genero`) REFERENCES `generos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
