List<int> merge(List<int> a, List<int> b) {
  List<int> c = [];
  int i = 0;
  int j = 0;

  while (i != a.length || j != b.length) {
    if (i == a.length) {
      c.add(b[j]);
      j++;
    } else if (j == b.length) {
      c.add(a[i]);
      i++;
    } else if (a[i] < b[j]) {
      c.add(a[i]);
      i++;
    } else if (b[j] < a[i]) {
      c.add(b[j]);
      j++;
    }
  }

  return c;
}

// A complexidade de pior caso desse algoritmo é O(n) pois, mesmo em seu pior caso,
// ele irá percorrer a lista a e a lista b apenas uma vez. Portanto, no fim das contas
// sua performance será +/- 2n. Mas como na notação O() as constantes são desconsideradas,
// pode-se dizer que a complexidade de pior caso desse algoritmo é O(n).
