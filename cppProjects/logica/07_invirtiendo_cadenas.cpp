/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */

#include <iostream>
#include <string>

using namespace std;

string invertirCadena(const string &cadena)
{
    string cadenaInvertida;

    // Iterar sobre la cadena de texto de atrás hacia adelante
    for (int i = cadena.length() - 1; i >= 0; --i)
    {
        cadenaInvertida += cadena[i];
    }

    return cadenaInvertida;
}

int main()
{
    string cadena;

    cout << endl
         << "Ingrese una cadena de texto: ";
    getline(cin, cadena); // Utilizamos getline para capturar espacios en blanco

    string cadenaInvertida = invertirCadena(cadena);
    cout << "Cadena invertida: " << cadenaInvertida << endl;

    return 0;
}
