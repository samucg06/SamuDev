// Tipos de datos básicos de C++

// Incluimos la biblioteca iostream para usar la función cout
#include <iostream>

// Usamos el espacio de nombres std
using namespace std;

int main()
{
    // Definimos algunas variables con diferentes tipos de datos
    int numero = 15;        // Variable de tipo entero (int)
    float decimal = 85.75;  // Variable de tipo flotante (float)
    double mayor = 16.3456; // Variable de tipo double (doble precisión)
    char letra = 'S';       // Variable de tipo carácter (char)

    // Imprimimos los valores de las variables
    cout << "Número: " << numero << endl;
    cout << "Decimal: " << decimal << endl;
    cout << "Mayor: " << mayor << endl;
    cout << "Letra: " << letra << endl;

    // Indicamos que el programa termina correctamente
    return 0;
}
