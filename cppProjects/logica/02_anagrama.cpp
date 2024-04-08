/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

#include <iostream>
#include <algorithm>
#include <string>
#include <cctype>

using namespace std;

bool sonAnagramas(const string &palabraUno, const string &palabraDos)
{
    // Dos palabras exactamente iguales no son anagramas
    if (palabraUno == palabraDos)
    {
        return false;
    }

    // Crear copias de las palabras para no modificar las originales
    string copiaPalabraUno = palabraUno;
    string copiaPalabraDos = palabraDos;

    // Ordenar las copias de las palabras
    sort(copiaPalabraUno.begin(), copiaPalabraUno.end());
    sort(copiaPalabraDos.begin(), copiaPalabraDos.end());

    // Comparar las palabras ordenadas
    return copiaPalabraUno == copiaPalabraDos;
}

int main()
{
    string palabraUno, palabraDos;
    cout << "Ingrese la primera palabra: ";
    cin >> palabraUno;
    cout << "Ingrese la segunda palabra: ";
    cin >> palabraDos;

    // De esta manera se convierten las cadenas de texto a minúsculas
    for (char &c : palabraUno)
    {
        c = tolower(c);
    }
    for (char &c : palabraDos)
    {
        c = tolower(c);
    }

    bool anagrama = sonAnagramas(palabraUno, palabraDos);
    if (anagrama)
    {
        cout << "Las palabras son anagramas." << endl;
    }
    else
    {
        cout << "Las palabras no son anagramas." << endl;
    }
    return 0;
}
