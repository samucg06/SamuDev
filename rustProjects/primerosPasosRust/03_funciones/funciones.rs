fn suma(a: i32, b: i32) -> i32 {
    let suma_parametros = a + b;

    return suma_parametros;
}

fn main() {
    let resultado_suma = suma(2, 2);
    println!(
        "El resultado de la suma de los parametros es: {}",
        resultado_suma
    );
}
