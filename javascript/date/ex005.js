const dataUltimoAcesso = new Date('2023/10/16 06:00:00');
const dataAtual = new Date();

const hora = dataAtual.getHours();

const timeUltimoAcesso = dataUltimoAcesso.getTime();
const timeAtual = dataAtual.getTime();

const diferencaTime = timeAtual - timeUltimoAcesso;

const milissegundosHora = 1000 * 60 * 60;
const milissegundosDia = milissegundosHora * 24;

let dias = Math.ceil(diferencaTime / milissegundosDia);
let horas = Math.ceil(diferencaTime / milissegundosHora);

let msg = '';

if (hora < 6 || hora >= 18) {
  // boa noite
  msg = `Boa noite`;
} else if (hora > 6 && hora < 12) {
  // bom dia
  msg = `Bom dia`;
} else {
  // boa tarde
  msg = `Boa tarde`;
}

if (diferencaTime > milissegundosDia) {
  msg += ` voce esta ausente a ${dias} dias!!`;
} else if (diferencaTime > milissegundosHora) {
  msg += ` voce esta ausente a ${horas} horas!`;
} else {
  msg += ' que bom que ainda está aqui!';
}

console.log(msg);
