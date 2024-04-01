#include <iostream>

using namespace std;

int main()
{
    float precio_producto, valor_iva = 0.19, precio_producto_iva;

    cout << "Ingrese el valor del producto: ";
    cin >> precio_producto;

    precio_producto_iva = precio_producto * valor_iva;
    precio_producto_iva = precio_producto + precio_producto_iva;

    cout << endl
         << "El valor del producto incluido el IVA es: " << precio_producto_iva << " pesos";

    return 0;
}