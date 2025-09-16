<?php
// 1. Conectar ao banco de dados
$servername = "localhost";
$username = "root";
$password = "unicid";
$dbname = "Livraria";

// Criar conexão
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexão
if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

// 2. Inserir um novo livro
$titulo = "Dom Casmurro";
$autor = "Machado de Assis";
$preco = 59.90;

$sql = "INSERT INTO Livros (titulo, autor, preco) VALUES ('$titulo', '$autor', $preco)";

if ($conn->query($sql) === TRUE) {
    echo "Livro inserido com sucesso!<br><br>";
} else {
    echo "Erro ao inserir livro: " . $conn->error;
}

// 3. Exibir todos os livros cadastrados
$result = $conn->query("SELECT * FROM livros");

if ($result->num_rows > 0) {
    echo "<h3>Livros cadastrados:</h3>";
    echo "<ul>";
    while ($row = $result->fetch_assoc()) {
        echo "<li><strong>" . $row["titulo"] . "</strong> - " . $row["autor"] . " - R$ " . number_format($row["preco"], 2, ',', '.') . "</li>";
    }
    echo "</ul>";
} else {
    echo "Nenhum livro encontrado.";
}

// Fechar conexão
$conn->close();
?>
