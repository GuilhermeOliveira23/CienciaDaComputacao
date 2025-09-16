<?php 
//DESAFIO 1: Declare variáveis com seus dados pessoais
$nome = "Guilherme";
$idade = 19;
$altura = 1.80;
$estudante = True;
// DESAFIO 2: Exiba as informações formatadas corretamente

echo "<h2>Informações Pessoais</h2>";
echo "Nome: $nome <br>";
echo "Idade: $idade anos <br>";
echo "Altura: $altura metros <br>";
echo "É estudante:" . ($estudante ? " Sim": " Não");
?>