<?php
// DESAFIO 1: Defina 4 notas de 0 a 10
$nota1 = 5;
$nota2 = 7;
$nota3 = 8;
$nota4 = 8;
// DESAFIO 2: Calcule a média corretamente
$media = ($nota1 + $nota2 + $nota3 + $nota4) / 4;
// DESAFIO 3: Verifique a situação (aprovado se média ≥ 7)
$situacao = "Reprovado";
if ($media >= 7)
{
$situacao = "Aprovado";
}


echo "<h2>Resultado Escolar</h2>";
echo "Média: " . number_format($media, 2) . "<br>";
echo "Situação: $situacao";
?>