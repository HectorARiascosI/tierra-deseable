// Selecciona el body para añadir hojas
const body = document.body;

// Número máximo de hojas visibles al mismo tiempo
const maxHojas = 10;

// Función para generar una hoja
function crearHoja() {
    const hoja = document.createElement('div');
    hoja.classList.add('hoja');

    // Posición horizontal aleatoria (dentro del ancho del viewport)
    const posicionX = Math.random() * window.innerWidth;

    // Retardo aleatorio para que no todas las hojas caigan al mismo tiempo
    const retraso = Math.random() * 5; // Máximo 5 segundos

    // Duración aleatoria para que las hojas caigan a diferentes velocidades
    const duracion = 5 + Math.random() * 5; // Entre 5 y 10 segundos

    // Asigna estilo dinámico
    hoja.style.left = `${posicionX}px`;
    hoja.style.animationDelay = `${retraso}s`;
    hoja.style.animationDuration = `${duracion}s`;

    // Añade la hoja al body
    body.appendChild(hoja);

    // Elimina la hoja una vez termine su animación
    hoja.addEventListener('animationend', () => {
        hoja.remove();
    });
}

// Generar hojas con un intervalo controlado
function generarHojas() {
    const interval = setInterval(() => {
        // Limita el número de hojas activas
        if (document.querySelectorAll('.hoja').length < maxHojas) {
            crearHoja();
        }
    }, 500); // Genera hojas cada 500ms (puedes ajustar este valor)
}

// Inicia la generación de hojas
generarHojas();
