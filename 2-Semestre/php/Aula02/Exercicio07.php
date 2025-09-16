<?php
// DESAFIO 1: Inicialize a matriz de pessoas
$pessoas = array();
// DESAFIO 2: Adicione 3 pessoas à matriz (cada pessoa deve ter nome e idade)
$pessoas = [
["nome" => "Guilherme", "idade"=> 20],
["nome" => "Ana", "idade" => 20],
["nome" => "Maria", "idade" => 20]
];
// DESAFIO 3: Exiba a lista de pessoas em uma tabela HTML
echo "<h2>Lista de Pessoas Cadastradas</h2>";
echo "<table border='1'>";
echo "<tr><th>Nome</th><th>Idade</th></tr>";
foreach ($pessoas as $pessoa) {
echo "<tr>";
echo "<td>" . $pessoa["nome"] . "</td>";
echo "<td>" . $pessoa["idade"] . "</td>";
echo "</tr>";
}
echo "</table>";
// DESAFIO 4: Calcule e exiba a média de idade
$somaIdades = 0;
foreach ($pessoas as $pessoa) {
$somaIdades += $pessoa["idade"];
}
$mediaIdades = $somaIdades / count($pessoas);
echo "<p>Média de idade: " . number_format($mediaIdades, 1) . " anos</p>";
?>