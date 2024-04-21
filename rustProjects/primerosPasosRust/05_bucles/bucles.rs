fn main() {
    // Función que ejecuta un bucle 'loop'
    fn loops() {
        let mut contador = 0;

        loop {
            println!("{}", contador);
            contador += 1;

            if contador == 6 {
                break; // Rompe el bucle cuando contador alcanza 6
            }
        }
    }

    // Función que ejecuta un bucle 'while'
    fn whiles() {
        let mut contador = 0;

        while contador != 10 {
            println!("{}", contador);
            contador += 1;
        }
    }

    // Función que ejecuta un bucle 'for'
    fn fors() {
        // Bucle 'for' para iterar sobre un rango de números
        for num in 1..=5 {
            println!("{}", num);
        }

        // Bucle 'for' para iterar sobre los elementos de un arreglo
        let arreglo = [1, 2, 3, 4, 5];
        for elemento in arreglo.iter() {
            println!("{}", elemento);
        }
    }

    // Llama a las funciones que contienen los bucles
    loops();
    whiles();
    fors();
}
