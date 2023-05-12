class Stack {

    private data: any[];

    constructor(){}

    push(item: any): void {
        this.data.push(item);
    }

    pop(): any {
        return this.data.pop();
    }

    top(): any {
        return this.data[0];
    }

    empty(): boolean {
        return this.data.length === 0;
    }
}