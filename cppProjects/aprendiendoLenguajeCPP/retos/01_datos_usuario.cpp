#include <iostream>

using namespace std;

int main()
{
    int edad_usuario;
    string sexo_usuario;
    float altura_usuario;

    cout << "Digite su edad: ";
    cin >> edad_usuario;

    cout << "Digite su sexo: ";
    cin >> sexo_usuario;

    cout << "Digite su altura en metros: ";
    cin >> altura_usuario;

    cout << endl
         << "Su edad: " << edad_usuario << endl
         << "Su sexo: " << sexo_usuario << endl
         << "Su altura: " << altura_usuario << endl;

    return 0;
}