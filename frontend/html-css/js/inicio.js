const API = 'http://127.0.0.1:8000/api';

function truncar(texto, max = 150) {
    return texto.length > max ? texto.slice(0, max) + '...' : texto;
}

function precioHTML(juego) {
    if (juego.precio_original) {
        return `<span class="precio-tachado">${juego.precio_original} €</span>
                <span class="precio-actual">${juego.precio} €</span>`;
    }
    return `<span class="precio-actual">${juego.precio} €</span>`;
}

async function cargarDestacado() {
    const res = await fetch(`${API}/juegos/?destacado=true`);
    const juegos = await res.json();
    if (!juegos.length) return;
    const j = juegos[0];
    document.getElementById('juego-destacado').innerHTML = `
        <a href="GamekeyDetalles.html?id=${j.id}">
            <img src="img/${j.imagen}" alt="${j.titulo}">
        </a>
        <div>
            <h3>${j.titulo}</h3>
            <p>${truncar(j.descripcion)}</p>
            <p>${precioHTML(j)}</p>
        </div>
    `;
}

async function cargarDescuentos() {
    const res = await fetch(`${API}/juegos/?en_descuento=true`);
    const juegos = await res.json();
    document.getElementById('juegos-descuento').innerHTML = juegos.slice(0, 3).map(j => `
        <a href="GamekeyDetalles.html?id=${j.id}">
            <img src="img/${j.imagen}" alt="${j.titulo}" title="${j.titulo}">
        </a>
    `).join('');
}

async function cargarNovedades() {
    const res = await fetch(`${API}/juegos/?novedad=true`);
    const juegos = await res.json();
    document.getElementById('lista-novedades').innerHTML = juegos.map(j => `
        <li>
            <a href="GamekeyDetalles.html?id=${j.id}">
                <img src="img/${j.imagen}" alt="${j.titulo}">
            </a>
            <p><strong>${j.titulo}:</strong><br>${truncar(j.descripcion)}</p>
        </li>
    `).join('');
}

cargarDestacado();
cargarDescuentos();
cargarNovedades();
