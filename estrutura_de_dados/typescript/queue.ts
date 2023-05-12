class Queue {

    private data: any[];

    constructor(){}

    insert(item: any): void {
        this.data.push(item);
    }

    remove(): any {
        return this.data.shift();
    }

    empty(): boolean {
        return this.data.length === 0;
    }

}