int max(List<int> array) {
  int result = array.first;
  for (var i = 1; i < array.length; i++) {
    if (array[i] > result) result = array[i];
  }
  return result;
}

// Sua complexidade de tempo é O(n). O algoritmo precisará percorrer o vetor por inteiro
// comparando os itens uns com os outros para definir qual deles é o maior. Sendo assim,
// a grandeza que define a complexidade de tempo final desse vetor é n. Por isso, O(n).