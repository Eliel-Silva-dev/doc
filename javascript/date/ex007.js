// função para formar datas:

const data = new Date();

function formatarData(data) {
  let newData = new Date(data);
  return `${newData.getDate()}/${newData.getMonth() + 1}/${newData.getFullYear()} `;
}

console.log(formatarData(data));

//----------------------------------------------
