#include <iostream>
#include <cmath>

using namespace std;

float teorema_pitagoras()
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
    float hipotenusa = teorema_pitagoras();

    cout.precision(3);
    cout
        << "La longitud de la hipotenusa del triangulo rectangulo es: " << hipotenusa;
    return 0;
}