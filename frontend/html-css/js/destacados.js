const API = 'http://127.0.0.1:8000/api';

function truncar(texto, max = 130) {
    return texto.length > max ? texto.slice(0, max) + '...' : texto;
}

async function cargarDestacados() {
    const res = await fetch(`${API}/juegos/?destacado=true`);
    const juegos = await res.json();
    if (!juegos.length) return;

    const grande = juegos[0];
    const pequenos = juegos.slice(1, 4);

    document.getElementById('juegos-destacados-grid').innerHTML = `
        <a href="GamekeyDetalles.html?id=${grande.id}">
            <img src="img/${grande.imagen}" alt="${grande.titulo}">
        </a>
        <div>
            ${pequenos.map(j => `
                <a href="GamekeyDetalles.html?id=${j.id}">
                    <img src="img/${j.imagen}" alt="${j.titulo}">
                </a>
            `).join('')}
        </div>
    `;
}

async function cargarPopular() {
    const res = await fetch(`${API}/juegos/?top_ventas=true`);
    const juegos = await res.json();
    if (!juegos.length) return;

    const conDescripcion = juegos.slice(0, 5);
    const portadas = juegos.slice(5, 10);

    document.getElementById('completos').innerHTML = conDescripcion.map(j => `
        <div>
            <a href="GamekeyDetalles.html?id=${j.id}">
                <img src="img/${j.imagen}" alt="${j.titulo}">
            </a>
            <p><strong>${j.titulo}:</strong><br>${truncar(j.descripcion)}</p>
        </div>
    `).join('');

    document.getElementById('portadas').innerHTML = portadas.map(j => `
        <a href="GamekeyDetalles.html?id=${j.id}">
            <img src="img/${j.imagen}" alt="${j.titulo}" title="${j.titulo}">
        </a>
    `).join('');
}

cargarDestacados();
cargarPopular();
