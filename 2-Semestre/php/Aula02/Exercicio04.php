<?php
// DESAFIO 1: Crie uma matriz com 5 frutas diferentes
$frutas = array("banana","uva","pera","abacate","tomate");
echo "<h2>Lista de Frutas</h2>";
echo "<ul>";
// DESAFIO 2: Complete o loop para exibir todas as frutas
foreach ($frutas as $fruta) {
echo "<li>" . $fruta . "</li>";
}
echo "</ul>";
// DESAFIO 3: Adicione duas novas frutas à matriz
array_push($frutas,"maçã", "laranja");
echo "<h3>Frutas Atualizadas</h3>";
echo "<ul>";
foreach ($frutas as $fruta) {
echo "<li>$fruta</li>";
}
echo "</ul>";
?>