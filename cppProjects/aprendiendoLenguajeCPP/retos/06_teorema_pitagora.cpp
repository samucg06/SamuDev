#include <iostream>
#include <cmath>

using namespace std;

int procedimiento_pitagorico()
{
    int procedimiento;

    cout << "Desea encontrar:\n\n1. Hipotenusa\n2. Cateto\n\n==> ";
    cin >> procedimiento;

    return procedimiento;
}

float encontrar_cateto()
{
    float hipotenusa, cateto_a, cateto_b;

    cout << "Ingresa el valor de la hipotenusa: ";
    cin >> hipotenusa;

    cout << "Ingresa el valor del cateto dado: ";
    cin >> cateto_a;

    cateto_b = pow(hipotenusa, 2) - pow(cateto_a, 2);
    cateto_b = sqrt(cateto_b);

    return cateto_b;
}

float encontrar_hipotenusa()
{
    float cateto_a, cateto_b, hipotenusa;

    cout << "Ingrese el valor del cateto a: ";
    cin >> cateto_a;

    cout << "Ingrese el valor del cateto b: ";
    cin >> cateto_b;

    hipotenusa = pow(cateto_a, 2) + pow(cateto_b, 2);
    hipotenusa = sqrt(hipotenusa);

    return hipotenusa;
}

int main()
{
    int procedimiento = procedimiento_pitagorico();

    if (procedimiento == 1)
    {
        cout.precision(3);
        float hipotenusa = encontrar_hipotenusa();
        cout << endl
             << "El valor de la hipotenusa del triangulo es: " << hipotenusa;
    }
    else if (procedimiento == 2)
    {
        cout.precision(3);
        float cateto = encontrar_cateto();
        cout << endl
             << "El valor del cateto faltante del triangulo es: " << cateto;
    }

    return 0;
}