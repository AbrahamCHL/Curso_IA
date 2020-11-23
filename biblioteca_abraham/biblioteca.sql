-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 23-11-2020 a las 09:56:34
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
-- Base de datos: `biblioteca`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `copia_libros`
--

CREATE TABLE `copia_libros` (
  `id` int(11) NOT NULL,
  `isbn_libro` varchar(100) NOT NULL,
  `deteriodado` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `copia_libros`
--

INSERT INTO `copia_libros` (`id`, `isbn_libro`, `deteriodado`) VALUES
(1, '1232', 'no'),
(2, '4565', 'si'),
(3, '1232', 'si'),
(4, '4565', 'no'),
(5, '7898', 'no'),
(6, '7898', 'si');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `editorial`
--

CREATE TABLE `editorial` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `editorial`
--

INSERT INTO `editorial` (`id`, `nombre`) VALUES
(1, 'Alianza'),
(2, 'Ariel'),
(3, 'Catedra'),
(4, 'Tecnos'),
(5, 'plesa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `ISBN` varchar(100) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `editorial` int(11) NOT NULL,
  `anio_creacion` date NOT NULL,
  `autor` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`ISBN`, `titulo`, `editorial`, `anio_creacion`, `autor`) VALUES
('1232', 'Rey blanco', 3, '2019-11-12', 'Juan Gomez Jurado'),
('4565', 'Aquitania', 5, '2020-05-05', 'Eva Garcia Saenz de urturi'),
('7898', 'La ciudad de vapor', 5, '2020-11-08', 'Carlos Ruiz Zafon');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prestamos`
--

CREATE TABLE `prestamos` (
  `id_copia_libro` int(11) NOT NULL,
  `codigo_socio` varchar(100) NOT NULL,
  `fecha_prestamo` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `fecha_devolucion` date NOT NULL,
  `fecha_real_devolucion` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `prestamos`
--

INSERT INTO `prestamos` (`id_copia_libro`, `codigo_socio`, `fecha_prestamo`, `fecha_devolucion`, `fecha_real_devolucion`) VALUES
(1, '4565', '2020-11-23 09:38:43', '2020-10-14', '2020-11-25'),
(1, '7898', '2020-11-23 09:38:43', '2020-10-13', '2020-10-29'),
(5, '8525', '2020-11-23 09:39:04', '2020-10-12', '2020-11-12');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `socio`
--

CREATE TABLE `socio` (
  `codigo` varchar(100) NOT NULL,
  `dni` varchar(9) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono` varchar(9) NOT NULL,
  `fecha_alta` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `socio`
--

INSERT INTO `socio` (`codigo`, `dni`, `direccion`, `telefono`, `fecha_alta`, `nombre`, `apellidos`) VALUES
('1232', 'a', 'barcelona', '789456123', '2020-11-23 09:28:38', 'Abraham', 'Chasing Luzón'),
('4565', 'b', 'hospitalet', '789456123', '2020-11-23 09:28:38', 'Jorge', 'Miralles'),
('7898', 'c', 'Santa Coloma', '456789123', '2020-11-23 09:29:18', 'Bryan', 'Chalan'),
('8525', 'd', 'Roma', '852741963', '2020-11-23 09:30:00', 'Ronald', 'Sotelo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `copia_libros`
--
ALTER TABLE `copia_libros`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_isbn_copia_libros` (`isbn_libro`);

--
-- Indices de la tabla `editorial`
--
ALTER TABLE `editorial`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`ISBN`),
  ADD KEY `fk_editorial_libros` (`editorial`);

--
-- Indices de la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD PRIMARY KEY (`id_copia_libro`,`codigo_socio`),
  ADD KEY `fk_codigo_socio_prestamos` (`codigo_socio`);

--
-- Indices de la tabla `socio`
--
ALTER TABLE `socio`
  ADD PRIMARY KEY (`codigo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `copia_libros`
--
ALTER TABLE `copia_libros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `editorial`
--
ALTER TABLE `editorial`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `copia_libros`
--
ALTER TABLE `copia_libros`
  ADD CONSTRAINT `fk_isbn_copia_libros` FOREIGN KEY (`isbn_libro`) REFERENCES `libros` (`ISBN`);

--
-- Filtros para la tabla `libros`
--
ALTER TABLE `libros`
  ADD CONSTRAINT `fk_editorial_libros` FOREIGN KEY (`editorial`) REFERENCES `editorial` (`id`);

--
-- Filtros para la tabla `prestamos`
--
ALTER TABLE `prestamos`
  ADD CONSTRAINT `fk_codigo_socio_prestamos` FOREIGN KEY (`codigo_socio`) REFERENCES `socio` (`codigo`),
  ADD CONSTRAINT `fk_copia_libro_prestamo` FOREIGN KEY (`id_copia_libro`) REFERENCES `copia_libros` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
