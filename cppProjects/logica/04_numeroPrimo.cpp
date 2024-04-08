#include <iostream>
#include <cmath>

using namespace std;

bool numeroPrimo()
{
    int numeroUsuario;
    bool esPrimo = true; // Inicialmente asumimos que el número es primo

    cout << "Ingrese un numero: ";
    cin >> numeroUsuario;

    for (int i = 2; i <= sqrt(numeroUsuario); ++i)
    {
        if (numeroUsuario % i == 0)
        {
            esPrimo = false; // Si encontramos un divisor, el número no es primo
            break;           // Salimos del bucle ya que ya no necesitamos comprobar más divisores
        }
    }

    return esPrimo; // Devolvemos el resultado
}

int main()
{
    bool primo = numeroPrimo();

    if (primo)
    {
        cout << "El numero es Primo";
    }
    else
    {
        cout << "El numero no es primo";
    }
    return 0;
}
