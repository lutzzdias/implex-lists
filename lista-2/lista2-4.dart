List<int> fibonacci(int n) {
  List<int> result = [0, 1];

  for (var i = 2; i < n; i++) {
    int next = result[i - 2] + result[i - 1];
    result.add(next);
  }

  return result;
}

// Complexidade de tempo = O(n)
// Há um laço que se repete por n vezes, as outras operações são todas constantes e,
// portanto, são ignoradas na notação O.