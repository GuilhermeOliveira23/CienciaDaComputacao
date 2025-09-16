<?php
// DESAFIO 1: Crie uma matriz associativa com informações de um livro
$livro = array(
"nome" => "Dom Casmurro",
"autor" => "Machado de Assis",
"preco" => 29.90,
"qnt" => 10
);
echo "<h2>Informações do Livro</h2>";
echo "<table border='1'>";
// DESAFIO 2: Complete o loop para exibir todas as informações
foreach ($livro as $chave => $valor) {
echo "<tr>";
echo "<td><strong>" . $chave . "</strong></td>";
echo "<td>" . $valor . "</td>";
echo "</tr>";
}
echo "</table>";
$livro["preco"] = 20.90;
echo "<p>Novo preço: R$ " . $livro['preco'] . "</p>";
?>