#include <iostream>
#include <cmath>

using namespace std;

float expresion_uno()
{
    float a, b;
    cout << "Digita el valor de a: ";
    cin >> a;

    cout << "Digita el valor de b: ";
    cin >> b;

    float expresion_uno = (a / b) + 1;
    float expresion_uno_redondeada = round(expresion_uno * 100) / 100;

    return expresion_uno_redondeada;
}

float expresion_dos()
{
    float a, b, c, d;
    cout << "Digita el valor de a: ";
    cin >> a;

    cout << "Digita el valor de b: ";
    cin >> b;

    cout << "Digita el valor de c: ";
    cin >> c;

    cout << "Digita el valor de d: ";
    cin >> d;

    float expresion_dos = (a + b) / (c + d);
    float expresion_dos_redondeada = round(expresion_dos * 100) / 100;

    return expresion_dos_redondeada;
}

int main()
{
    int expresion_usuario;
    float resultado;

    cout << "¿Cual expresion deseas implementar?" << endl
         << "1. (a / b) + 1" << endl
         << "2. (a + b) / (c + d)" << endl
         << "==> ";
    cin >> expresion_usuario;

    if (expresion_usuario == 1)
    {
        resultado = expresion_uno();
    }
    else
    {
        resultado = expresion_dos();
    }

    cout << "El resultado de la operacion es: " << resultado << endl;

    return 0;
}
