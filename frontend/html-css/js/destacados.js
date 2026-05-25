const API = 'http://127.0.0.1:8000/api';

function truncar(texto, max = 130) {
    return texto.length > max ? texto.slice(0, max) + '...' : texto;
}

function precioHTML(juego) {
    if (juego.precio_original) {
        return `<span class="precio-tachado">${juego.precio_original} €</span>
                <span class="precio-actual">${juego.precio} €</span>`;
    }
    return `<span class="precio-actual">${juego.precio} €</span>`;
}

async function cargarDestacados() {
    const res = await fetch(`${API}/juegos/?destacado=true`);
    const juegos = await res.json();
    if (!juegos.length) return;

    const j = juegos[0];

    document.getElementById('juegos-destacados-grid').innerHTML = `
        <a href="GamekeyDetalles.html?id=${j.id}">
            <img src="img/${j.imagen}" alt="${j.titulo}">
        </a>
        <div class="info-destacado">
            <h3>${j.titulo}</h3>
            <p>${truncar(j.descripcion, 220)}</p>
            <p>${precioHTML(j)}</p>
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
