CREATE DATABASE Livraria;
USE Livraria;
CREATE TABLE Livros( id INT AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(255), autor VARCHAR(100), preco DECIMAL(10,2));
INSERT INTO Livros (titulo,autor,preco) VALUES('Dom casmurro', 'Machado de Assis',33.30);
INSERT INTO Livros (titulo,autor,preco) VALUES('Metamorfose', 'Frankz Kafka',40.50);
INSERT INTO Livros (titulo,autor,preco) VALUES('Os Miseraveis', 'Victor Hugo',35.40);
SELECT id, titulo, autor, preco FROM Livros;
SELECT * FROM livros
WHERE preco > 35.00;

SELECT * FROM livros
ORDER BY titulo ASC;
