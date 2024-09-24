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
