#include <iostream>
#include <utility>

using namespace std;

// Función para intercambiar los valores de dos variables
pair<int, int> intercambio_valor_variables()
{
    int a, b;

    cout << "Ingrese el valor de a: ";
    cin >> a;

    cout << "Ingrese el valor de b: ";
    cin >> b;

    int c;

    c = a; // Guardamos el valor de 'a' en 'c'
    a = b; // Asignamos el valor de 'b' a 'a'
    b = c; // Asignamos el valor original de 'a' (guardado en 'c') a 'b'

    return make_pair(a, b); // Devolvemos el par (a, b)
}

int main()
{
    auto valores_variables = intercambio_valor_variables();

    cout << "El valor de a es: " << valores_variables.first << endl;
    cout << "El valor de b es: " << valores_variables.second << endl;

    return 0;
}
