#include "stddef.h"
#include "stdio.h"
int main() {
  int arr[8];
  int i, j;
  int sum;
  arr[0] = 0x79;
  arr[1] = 0x12c97f;
  arr[2] = 0x135f0f8;
  arr[3] = 0x74acbc6;
  arr[4] = 0x56c614e;
  arr[5] = 0xffffffe2;

  srand(time(0));
  for (i = 0; i < 6; i = i + 1) {
    int r = rand();
    arr[i] = arr[i] - (r % 10 + -1);
  }
  sum = 0;
  for (j = 0; j < 6; j = j + 1) {
    sum = sum + arr[j];
  }
  printf("%d", sum);
}
