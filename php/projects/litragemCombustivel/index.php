<!DOCTYPE html>

<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial scale=1.0">
    <meta name="description" content="pagina de calculo de consumo de combustivel">
    <link rel="stylesheet" href="style.css">

    <title>Consumo de combustível</title>
</head>
<body>
    <main>
        <div class="painel">
            <h2>Instruções</h2>
            <div class="conteudo_painel">
                <p>Esta aplicação tem como finalidade demonstrar os valores que
					serão gastos com combustível durante uma viagem, com base no
				consumo do seu veículo, e com a distância determinada por você!
				</p>
                <p>Os combustíveis disponíveis para este cálculo são:</p>
                <ul>
                    <li>Álcool</li>
                    <li>Díesel</li>
                    <li>Gasolina</li>
                </ul>
            </div>
        </div>

        <div class="painel">
            <h2>Cálculo do valor (R$) do consumo</h2>
            <div class="conteudo_painel">
                <form action="calculo.php" method="post">
                    <label for="distancia">Distância em Quilômetros a ser percorrida</label>
                    <input type="number" class="campo_texto" name="distancia" required>

                    <label for="autonomia">Consumo de combustível do veículo (Km/l)</label>
                    <input type="number" class="campo_texto" name="autonomia" required>

                    <button class="botao" type="submit">Calcular</button>
                </form>
            </div>
        </div>
    </main>
</body>
</html>