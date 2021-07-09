#include <stdio.h>
#include <stdlib.h>

__attribute__((constructor))
void setup() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

int ai_calculate() {
    return rand() % 20;
}

void ai_debug() {
    system("/bin/sh");
}

void vuln() {
    char stock_ticker[16]; // max length is 5 letters in the US
    printf("Please enter the stock ticker symbol: ");
    gets(stock_ticker);

    int calculation = ai_calculate(); // advanced algorithm

    printf("%s will increase by $%d today!\n", stock_ticker, calculation);
}

int main() {
    printf("Advanced AI Stock Price Predictor\n");
    vuln();
    printf("Thanks for using the Advanced AI Stock Price Predictor!\n");
}
