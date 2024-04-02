// Lectura o Entrada de datos en C++

// Incluimos la biblioteca iostream para usar las funciones cout y cin
#include <iostream>

// Usamos el espacio de nombres std
using namespace std;

int main()
{
    // Declaramos una variable llamada "numero" de tipo float
    float numero;

    // Solicitamos al usuario que ingrese un número
    cout << "Digita un número: ";

    // Leemos el número ingresado por el usuario y lo almacenamos en la variable "numero"
    cin >> numero;

    // Imprimimos el número ingresado
    cout << endl
         << "El número que digitaste es: " << numero << endl;

    // Indicamos que el programa termina correctamente
    return 0;
}
