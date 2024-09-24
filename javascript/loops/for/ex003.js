let funcionarios = [
  { id: 1, nome: 'César', habilitado: false },
  { id: 2, nome: 'Jéssica', habilitado: false },
  { id: 3, nome: 'Renan', habilitado: true },
  { id: 4, nome: 'Marlon', habilitado: false },
  { id: 5, nome: 'Ana', habilitado: false },
];

let encontrou_Habilitado = false;

for (let contador = 0; contador < funcionarios.length; contador++) {
  let funcionario = funcionarios[contador];

  if (funcionario.habilitado == true) {
    console.log('Funcionario habilitado encontrado: ' + funcionario.nome);
    encontrou_Habilitado = true;
    break;
  }
}

if (!encontrou_Habilitado) {
  console.log('Nenhum funcionário habilitado encontrado');
}
