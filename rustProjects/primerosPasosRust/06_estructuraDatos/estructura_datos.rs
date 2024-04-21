fn main() {
    let tupla_a = ('S', 6i32, true);
    println!(
        "¿{}amuel tiene {} letras? {}",
        // Se puede acceder a los elementos de una tupla por la posición del índice, a partir de cero.
        tupla_a.0,
        tupla_a.1,
        tupla_a.2
    );

    // Estructura clasica con campos de nombre
    struct Estudiante {
        nombre: String,
        nivel: u8,
        remoto: bool,
    }

    // Estructura tupla sólo con tipos de datos
    struct Grados(char, char, char, char, f32);
}
