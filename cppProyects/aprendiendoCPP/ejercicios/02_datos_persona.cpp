#include <iostream>

using namespace std;

int main()
{
    int edad;
    char sexo;
    float altura;

    cout << "Ingrese su edad: ";
    cin >> edad;

    cout << "Ingrese su sexo [M/F]: ";
    cin >> sexo;

    cout << "Ingrese su altura en m: ";
    cin >> altura;

    cout << endl
         << "Edad: " << edad << " primaveras" << endl
         << "Sexo: " << sexo << endl
         << "Altura: " << altura << " m" << endl;

    return 0;
}