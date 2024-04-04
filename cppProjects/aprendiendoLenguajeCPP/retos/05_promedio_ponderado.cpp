#include <iostream>

using namespace std;

float promedio_ponderado()
{
    float nota_practicas, nota_teorica, nota_participacion, promedio_ponderado;

    cout << "Ingrese la nota de practicas (30%): ";
    cin >> nota_practicas;

    cout << "Ingrese la nota teorica (60%): ";
    cin >> nota_teorica;

    cout << "Ingrese la nota de participacion (10%): ";
    cin >> nota_participacion;

    promedio_ponderado = (nota_practicas * 0.30) + (nota_teorica * 0.60) + (nota_participacion * 0.10);

    return promedio_ponderado;
}

int main()
{
    float promedio_notas_ponderado = promedio_ponderado();
    cout << endl
         << "Su media ponderada es igual a: " << promedio_notas_ponderado;
    return 0;
}