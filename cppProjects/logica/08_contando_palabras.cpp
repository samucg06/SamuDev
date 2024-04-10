/*
 * Crea un programa en que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */

#include <iostream>
#include <map>
#include <string>
#include <cctype>

using namespace std;

// Función para eliminar los signos de puntuación de una palabra
string eliminarPuntuacion(string palabra)
{
    string palabraLimpia = "";
    for (char caracter : palabra)
    {
        if (isalpha(caracter) || caracter == '-')
        {                                       // Conserva letras y guiones
            palabraLimpia += tolower(caracter); // Convierte a minúsculas
        }
    }
    return palabraLimpia;
}

int main()
{
    string texto;
    cout << "\nIntroduce el texto: ";
    getline(cin, texto);

    map<string, int> conteoPalabras; // Mapa para almacenar el recuento de cada palabra

    // Procesar el texto palabra por palabra
    string palabraActual = "";
    for (char caracter : texto)
    {
        if (isalnum(caracter) || caracter == '-')
        { // Si es alfanumérico o guion
            palabraActual += caracter;
        }
        else if (!palabraActual.empty())
        {
            palabraActual = eliminarPuntuacion(palabraActual); // Eliminar puntuación y convertir a minúsculas
            if (!palabraActual.empty())
            {
                conteoPalabras[palabraActual]++; // Incrementar el recuento de la palabra
            }
            palabraActual = ""; // Reiniciar palabraActual
        }
    }

    // Procesar la última palabra
    if (!palabraActual.empty())
    {
        palabraActual = eliminarPuntuacion(palabraActual); // Eliminar puntuación y convertir a minúsculas
        if (!palabraActual.empty())
        {
            conteoPalabras[palabraActual]++; // Incrementar el recuento de la palabra
        }
    }

    // Mostrar el recuento final de palabras
    cout << "\nRecuento final de palabras:\n";
    for (const auto &par : conteoPalabras)
    {
        cout << par.first << ": " << par.second << endl;
    }

    return 0;
}
