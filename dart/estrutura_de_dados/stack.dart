class Stack {
  
  List<dynamic> _data = [];

  void push({ required dynamic item }) {
    this._data.add(item);
  }

  void pop() {
    return this._data.removeLast();
  }

  dynamic top() {
    return this._data.last;
  }

  bool empty() {
    return this._data.isEmpty;
  }

}