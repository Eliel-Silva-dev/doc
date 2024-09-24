let capital_emprestado = 3000;
let taxa_juros = 0.02; // 2%

let contador = 1;
let parcelas_totais = 5;

while (contador <= parcelas_totais) {
  // enquanto tiver parcelas:
  let numero_parcela = contador;
  let juros_emprestimo = capital_emprestado * taxa_juros * numero_parcela;

  console.log(
    'A taxa de juros no periodo de ' +
      numero_parcela +
      ' mes(es) é de R$' +
      juros_emprestimo +
      ',00',
  );

  contador++; // incrementa o loop
}
