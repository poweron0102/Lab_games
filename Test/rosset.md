Seguem alguns exercícios de revisão da matéria para a nossa aula de laboratório:

(1) Inserir o elemento (x - 1) antes e o elemento (x + 1) depois de cada ocorrência de x dentro de um vetor de resposta.
Se o seu vetor original é formado pelos elementos {1, 3, 1, 5, 1} (com o tamanho n igual a 5), e se x for igual a 1, seu
vetor de resposta será {0, 1, 2, 3, 0, 1, 2, 5, 0, 1, 2}, com tamanho igual a 11. O protótipo dessa função é o que segue:
int* ins_antes_depois_x(int *vet, int n, int x, int *tam_vet_resposta).

```c
int* ins_antes_depois_x(int *vet, int n, int x, int *tam_vet_resposta) {
        int cont_xis = 0;
        for (int cont = 0; cont < n; cont++) {
                if (vet[cont] == x) {
                        cont_xis++;
                }
        }
        *tam_vet_resposta = n + (2 * cont_xis);
        int *resp = malloc(sizeof(int) * (*tam_vet_resposta));
        int *resp_p = resp;

        while (resp_p < &resp[*tam_vet_resposta]) {
                //printf("%p\n", resp_p);
                if (*vet == x) {
                        *resp_p = x - 1; resp_p++;
                        *resp_p = x    ; resp_p++;
                        *resp_p = x + 1; resp_p++;
                }
                else {
                        *resp_p = *vet ; resp_p++;
                }
                vet++;
        }

        return resp;
}

int main(void) {
        int vet[] = {1, 2, 5, 6, 2, 5, 3};
        int n = 7;
        int x = 2;

        int n_resp;
        int *resp = ins_antes_depois_x(vet, n, x, &n_resp);

        for (int cont = 0; cont < n_resp; cont++) {printf("%d ", resp[cont]);}
        printf("\n");

        return 0;
}
```

(2) Escreva uma função para ordenar os caracteres de uma String, levando-se em consideração os seus respectivos valores 
na tabela ASCII. Se sua string for "amoR", a resposta será "Ramo". O protótipo dessa função é o que segue:
void ordena(char *str). NÃO PODEMOS CRIAR VETORES E STRINGS AUXILIARES PRA RESOLVER ESSA QUESTÃO!!!

(3) Retirar todos os múltiplos de k de um vetor de inteiros. Se o seu vetor é composto por {2, 3, 5, 4, 6, 8, 7, 9, 1},
com tamanho 9, e k = 2, seu vetor deve se transformar em {3, 5, 7, 9, 1}, com tamanho igual a 5.  
O protótipo dessa função é o que segue: void retira_mult_k(int *vet, int *novo_tam_vet, int k). NÃO PODEMOS CRIAR VETORES
AUXILIARES PRA RESOLVER ESSA QUESTÃO: USE SOMENTE ÍNDICES!!!

(4) Escreva o método k_str que retorna todas as k strings, onde k é menor que o tamanho da String original.
Se sua string é "abc" e k for igual a 2, seu código deve imprimir na tela as substrings "aa", "ba", "ca", "ab", "bb",
"cb", "ac", "bc" e "cc". Se sua string for "abc" e k for igual a 1, seu código deve imprimir na tela as substrings
"a", "b", "c". O protótipo dessa função é o que segue: void k_str(char *str, int k). DICA: USE RECURSÃO PARA RESOLVER
ESSE PROBLEMA!!!