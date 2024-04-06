#include <iostream>

using namespace std;

float promedio_ponderado()
{
    float primer_parcial, segundo_parcial, talleres_quices, promedio_ponderado;

    cout << "Ingrese la nota del primer parcial (30%): ";
    cin >> primer_parcial;

    cout << "Ingrese la nota del segundo parcial (50%): ";
    cin >> segundo_parcial;

    cout << "Ingrese la nota de la nota de talleres / quices (20%): ";
    cin >> talleres_quices;

    promedio_ponderado = (primer_parcial * 0.30) + (segundo_parcial * 0.50) + (talleres_quices * 0.20);

    return promedio_ponderado;
}

int main()
{
    float promedio_notas_ponderado = promedio_ponderado();
    cout << endl
         << "Su media ponderada es igual a: " << promedio_notas_ponderado;
    return 0;
}