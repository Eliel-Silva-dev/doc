const dataAtual = new Date();

console.log(dataAtual.getFullYear());
console.log(dataAtual.getMonth()); //* 0-11
console.log(dataAtual.getDate()); //* 1-31
console.log(dataAtual.getHours()); //* 0-23
console.log(dataAtual.getMinutes()); //* 0-59
console.log(dataAtual.getSeconds());
console.log(dataAtual.getMilliseconds());
console.log(dataAtual.getDay()); //* 0-6

//----------------------------------------
//metodos utc

console.log(dataAtual.getUTCFullYear());
console.log(dataAtual.getUTCMonth());
console.log(dataAtual.getUTCDate());
console.log(dataAtual.getUTCHours());
console.log(dataAtual.getUTCMinutes());
console.log(dataAtual.getUTCSeconds());
console.log(dataAtual.getUTCMilliseconds());
console.log(dataAtual.getUTCDay());

//----------------------------------------

//parametros possiveis para o method .toLocaleString()

const personalizandoData = {
  weekday: 'long', // segunda-feira
  weekday: 'short', // seg.
  weekday: 'narrow', // S

  month: 'numeric', // 2
  month: '2-digit', // 02
  month: 'long', // Março
  month: 'short', // Mar
  month: 'narrow', // M

  year: 'numeric', // 2020
  year: '2-digit', // 20

  day: 'numeric', // 1
  day: '2-digit', // 01
};
console.log(dataAtual.toLocaleDateString('pt-BR', personalizandoData));

//----------------------------------------

const personalizandoTempo = {
  hour: 'numeric', // 1
  hour: '2-digit', // 01,

  minute: 'numeric', // 1
  minute: '2-digit', // 01,

  second: 'numeric', // 1
  second: '2-digit', // 01,
};
console.log(dataAtual.toLocaleTimeString('pt-BR', personalizandoTempo));

const personalizandoDataTempo = {
  dateStyle: 'full', // segunda-feira, 9 de novembro de 2020
  dateStyle: 'long', // 9 de novembro de 2020
  dateStyle: 'medium', // 9 de nov. de 2020
  dateStyle: 'short', // 09/11/2020

  timeStyle: 'full', // 01:05:09 Horário Padrão de Brasília
  timeStyle: 'long', // 01:05:09 BRT
  timeStyle: 'medium', // 01:05:09
  timeStyle: 'short', // 01:05
};
console.log(dataAtual.toLocaleString('pt-BR', personalizandoDataTempo));
