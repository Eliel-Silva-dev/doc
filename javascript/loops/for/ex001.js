let multiplicador = 8;

console.log('Tabuada de multiplicação do Nº ' + multiplicador);
// não é necessario declarar o contador antes pois ele já esta incluso na sintaxe do for.
for (let contador = 0; contador <= 10; contador++) {
  let resultdo = multiplicador * contador;

  console.log(multiplicador + ' x ' + contador + ' = ' + resultdo);
}
