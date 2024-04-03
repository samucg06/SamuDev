#include <iostream>

using namespace std;

float expresion_uno()
{
    float a, b;
    cout << "Digita el valor de a: ";
    cin >> a;

    cout << "Digita el valor de b: ";
    cin >> b;

    float expresion_uno = (a / b) + 1;

    return expresion_uno;
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

    return expresion_dos;
}

float expresion_tres()
{
    float a, b, c, d, e, f;
    cout << "Digita el valor de a: ";
    cin >> a;

    cout << "Digita el valor de b: ";
    cin >> b;

    cout << "Digita el valor de c: ";
    cin >> c;

    cout << "Digita el valor de d: ";
    cin >> d;

    cout << "Digita el valor de e: ";
    cin >> e;

    cout << "Digita el valor de f: ";
    cin >> f;

    float expresion_tres = (a + (b / c)) / (d + (e / f));

    return expresion_tres;
}

float expresion_cuatro()
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

    float expresion_cuatro = a + (b / (c - d));

    return expresion_cuatro;
}

int main()
{
    int expresion_usuario;
    float resultado;

    cout << "Cual expresion deseas implementar?" << endl
         << "1. (a / b) + 1" << endl
         << "2. (a + b) / (c + d)" << endl
         << "3. (a + (b / c)) / (d + (e / f))" << endl
         << "4. a + (b / (c - d))" << endl
         << "==> ";
    cin >> expresion_usuario;

    if (expresion_usuario == 1)
    {
        resultado = expresion_uno();
    }
    else if (expresion_usuario == 2)
    {
        resultado = expresion_dos();
    }
    else if (expresion_usuario == 3)
    {
        resultado = expresion_tres();
    }
    else
    {
        resultado = expresion_cuatro();
    }

    cout.precision(3);
    cout << endl
         << "El resultado de la operacion es: " << resultado << endl;

    return 0;
}