function geradorArrayExemplo(tamanhoLista: number) {
    
    let listaExemplo: number[] = [];
    for(let tamanho: number = 0; tamanho < tamanhoLista; tamanho++) {
        const valorAleatorio: number = Math.floor((Math.random() * 99) % 100);
        listaExemplo.push(valorAleatorio);
    }
    return listaExemplo
}