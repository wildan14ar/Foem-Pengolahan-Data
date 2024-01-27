-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 03 Jan 2023 pada 04.37
-- Versi server: 10.4.21-MariaDB
-- Versi PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `formdata`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `ID` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Gender` varchar(8) NOT NULL,
  `Birth` varchar(10) NOT NULL,
  `Religion` varchar(20) NOT NULL,
  `Address` text NOT NULL,
  `Username` varchar(20) NOT NULL,
  `Password` varchar(30) NOT NULL,
  `Note` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`ID`, `Name`, `Gender`, `Birth`, `Religion`, `Address`, `Username`, `Password`, `Note`) VALUES
(306, 'SALSABILLA LARAS SITA', 'Female', '2000-01-01', 'Islam', '', '1002220006', '1002220006', 'Mahasiswa ITTS Prodi TI'),
(307, 'ANA\'LLHAQQ SURYANING', 'Male', '2000-01-01', 'Islam', '', '1002220002', '1002220002', 'Mahasiswa ITTS Prodi TI'),
(308, 'KHAWARIZMI BILHAQIE', 'Male', '2000-01-01', 'Islam', '', '1002220012', '1002220012', 'Mahasiswa ITTS Prodi TI'),
(309, 'HAIQAL AL ISRAQI SUN', 'Male', '2000-01-01', 'Islam', '', '1002220003', '1002220003', 'Mahasiswa ITTS Prodi TI'),
(310, 'WILDAN ABDURRASYID', 'Male', '2000-01-01', 'Islam', 'Klaten', '1002220011', '1002220011', 'Mahasiswa ITTS Prodi TI'),
(319, 'admin', 'Male', '2000-01-01', 'Islam', 'klaten', 'admin', 'admin', '');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `Username` (`Username`),
  ADD UNIQUE KEY `Password` (`Password`),
  ADD UNIQUE KEY `Name` (`Name`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=320;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
