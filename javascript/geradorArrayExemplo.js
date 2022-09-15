function geradorArrayExemplo(tamanhoLista) {
    
    let listaExemplo = [];

    for(let tamanho = 0; tamanho < tamanhoLista; tamanho++) {

        const valorAleatorio = parseInt((Math.random() * 99) % 100);

        listaExemplo.push(valorAleatorio);
    }

    console.log(`Array de Exemplo: ${listaExemplo}`);

    return listaExemplo
}