<!DOCTYPE html>
<html>
<head>
<title>Formulário de Contato</title>
</head>
<body>
<h2>Formulário de Contato</h2>
<!-- DESAFIO 1: Complete o formulário com os campos necessários -->
<form action="Exercicio06.php" method="Post">
Nome: <input type="text" name="nome" required><br><br>

Email: <input type="email" name="email" required><br
><br>
Idade: <input type="number" name="idade" min="1" max
="120"><br><br>
<input type="submit" value="Enviar">
</form>
</body>
</html>
<?php
// DESAFIO 2: Verifique se o formulário foi submetido
if ($_SERVER["REQUEST_METHOD"] == "POST") {
// DESAFIO 3: Capture os dados do formulário
$nome = $_POST['nome'];
$email = $_POST['email'];
$idade = $_POST['idade'];
echo "<h2>Dados Recebidos</h2>";
echo "Nome: $nome<br>";
echo "Email: $email<br>";
echo "Idade: $idade anos<br>";
// DESAFIO 4: Verifique se a idade é maior que 18 anos
if ($idade >= 18) {
echo "<p>Você é maior de idade!</p>";
} else {
echo "<p>Você é menor de idade!</p>";
}
} else {
echo "Acesso não permitido.";
}
?>