// Operaciones matemáticas básicas en C++

// Incluimos la biblioteca iostream para usar las funciones cout y cin
#include <iostream>

// Usamos el espacio de nombres std
using namespace std;

int main()
{
    // Declaramos variables para almacenar los números y los resultados
    float numero_uno, numero_dos, suma, resta, multiplicacion, division;

    // Solicitamos al usuario que ingrese el valor del primer número
    cout << "Ingrese el valor del primer número: ";
    cin >> numero_uno;

    // Solicitamos al usuario que ingrese el valor del segundo número
    cout << "Ingrese el valor del segundo número: ";
    cin >> numero_dos;

    // Realizamos las operaciones matemáticas
    suma = numero_uno + numero_dos;
    resta = numero_uno - numero_dos;
    multiplicacion = numero_uno * numero_dos;
    division = numero_uno / numero_dos;

    // Imprimimos los resultados
    cout << endl
         << "Suma: " << suma << endl
         << "Resta: " << resta << endl
         << "Multiplicación: " << multiplicacion << endl
         << "División: " << division << endl;

    // Indicamos que el programa termina correctamente
    return 0;
}
