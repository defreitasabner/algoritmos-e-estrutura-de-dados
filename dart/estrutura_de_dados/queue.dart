class Queue {

  List<dynamic> _data = [];

  void insert({ required dynamic item }) {
    this._data.add(item);
  }

  void remove() {
    this._data.removeAt(0);
  }

  bool empty() {
    return this._data.isEmpty;
  }

}