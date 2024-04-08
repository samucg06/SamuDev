#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    // Inicializa las variables para los dos primeros números de Fibonacci.
    long long int numeroAnterior = 0, numeroActual = 1, numeroSiguiente;

    // Imprime el primer número de Fibonacci.
    cout << numeroAnterior << ", ";

    // Bucle que se ejecuta 49 veces para imprimir los numeroSiguientes 49 números.
    for (int i = 1; i < 50; i++)
    {
        // Calcula el numeroSiguiente número de Fibonacci.
        numeroSiguiente = numeroAnterior + numeroActual;

        // Imprime el número de Fibonacci numeroActual.
        cout << numeroActual << (i < 49 ? ", " : "");

        // numeroActualiza las variables para la numeroSiguiente iteración.
        numeroAnterior = numeroActual;
        numeroActual = numeroSiguiente;
    }

    return 0;
}
