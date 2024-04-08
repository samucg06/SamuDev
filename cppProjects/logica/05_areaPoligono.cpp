/*
 * Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */

#include <iostream>

using namespace std;

float areaPoligono(int poligono)
{
    float base, altura, area;
    if (poligono == 1)
    {
        cout << "Ingrese la base del Triangulo: ";
        cin >> base;

        cout << "Ingrese la altura del Triangulo: ";
        cin >> altura;

        area = (base * altura) / 2;

        cout << "El area del Triangulo es: " << area;
    }
    else if (poligono == 2 || poligono == 3)
    {
        cout << "Ingrese la base del cuadrado o Rectangulo: ";
        cin >> base;

        cout << "Ingrese la altura del cuadrado o Rectangulo: ";
        cin >> altura;

        area = base * altura;

        cout << "El area del cuadrado o Rectangulo es: " << area;
    }
    else
    {
        cout << "poligono no admitido";
    }
}

int main()
{
    int poligono;
    cout << "A que poligono le deseas sacar el area?" << endl;
    cout << "1. Triangulo" << endl;
    cout << "2. Cuadrado" << endl;
    cout << "3. Rectangulo" << endl;
    cout << "==> ";
    cin >> poligono;

    areaPoligono(poligono);
    return 0;
}
