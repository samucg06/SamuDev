#include <iostream>

using namespace std;

float promedio_notas()
{
    float nota_uno, nota_dos, nota_tres, nota_cuatro, promedio_notas;

    cout << "Ingrese la nota del primer estudiante: ";
    cin >> nota_uno;

    cout << "Ingrese la nota del segundo estudiante: ";
    cin >> nota_dos;

    cout << "Ingrese la nota del tercer estudiante: ";
    cin >> nota_tres;

    cout << "Ingrese la nota del cuarto estudiante: ";
    cin >> nota_cuatro;

    promedio_notas = (nota_uno + nota_dos + nota_tres + nota_cuatro) / 4;

    return promedio_notas;
}

int main()
{
    double promedio_notas_estudiantes = promedio_notas();

    cout.precision(3);
    cout
        << endl
        << "El promedio de las notas de los estudiantes es: " << promedio_notas_estudiantes;

    return 0;
}