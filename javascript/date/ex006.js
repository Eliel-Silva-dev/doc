//calculando a dif de dias

let diaAtual = new Date();
let diaPassado = new Date('2023/09/30 00:00:00');
let dataMilissegundos = Math.abs(diaAtual.getTime() - diaPassado.getTime());

let dif = Math.ceil(dataMilissegundos / (1000 * 60 * 60 * 24));

console.log(dif);
