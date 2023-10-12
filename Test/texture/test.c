#include <stdio.h>

int main() {
	printf("Entre com o numero: \n");
	int num;
	scanf("%d", &num);

	char resp[100];
	char *resp_p = resp;

	unsigned char cont = 0;
	while (num) {
	    *resp_p = (num % 2) + '0';
	    num /= 2;

	    resp_p++;
	    cont++;
	}
	for (; cont != 0; cont--) {
	    printf("%c", *--resp_p);
	}
	printf("\n");

	return 0;
}
