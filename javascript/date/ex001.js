const hoje = new Date();
const vencimento = new Date('2024-09-25');

let mensagem = '';

if (hoje.getTime() > vencimento.getTime()) {
  mensagem = 'Esta conta já venceu.';
} else {
  mensagem = 'Ufa, ainda não venceu.';
}

console.log(mensagem);
