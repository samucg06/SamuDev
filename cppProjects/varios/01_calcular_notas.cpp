#include <iostream>
#include <cstdlib> // para system("cls")

using namespace std;

void clear()
{
    system("cls");
}

float calcularNotaFinal()
{
    float cantidadNotasUsuario, porcentajeNota, valorNota, notaFinal = 0; // Inicializar notaFinal a 0

    cout << "Cuantas notas tienes? ";
    cin >> cantidadNotasUsuario;

    clear();

    for (int i = 1; i <= cantidadNotasUsuario; i++)
    {
        cout << "Ingrese el valor de la Nota " << i << ": ";
        cin >> valorNota;

        cout << "Ingrese el porcentaje de la Nota " << i << ": ";
        cin >> porcentajeNota;
        porcentajeNota = porcentajeNota / 100;

        notaFinal += valorNota * porcentajeNota;

        clear();
    }

    return notaFinal;
}

float notaParaPasar()
{
    float notaNecesaria, notaMinima, porcentajeAprobacion;

    cout << "Ingrese la nota mínima requerida para aprobar: ";
    cin >> notaMinima;

    cout << "Ingrese el porcentaje de aprobación del curso: ";
    cin >> porcentajeAprobacion;
    porcentajeAprobacion /= 100;

    // Calcular la nota necesaria para pasar
    notaNecesaria = (notaMinima / porcentajeAprobacion) - calcularNotaFinal();

    return notaNecesaria;
}

int main()
{
    clear();
    int programa;

    cout << "Que desea hacer?" << endl
         << endl
         << "1. Calcular su nota final." << endl
         << "2. Calcular cuanto necesita para pasar." << endl
         << "==> ";
    cin >> programa;

    if (programa == 1)
    {
        float notaFinal = calcularNotaFinal();
        cout << "Su nota final es: " << notaFinal;
    }
    else if (programa == 2)
    {
        float notaFaltante = notaParaPasar();
        cout << "Necesitas obtener al menos " << notaFaltante << " para pasar.";
    }

    return 0;
}