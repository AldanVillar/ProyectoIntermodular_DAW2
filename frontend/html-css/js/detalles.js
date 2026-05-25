const API = 'http://127.0.0.1:8000/api';

function getIdFromURL() {
    return new URLSearchParams(window.location.search).get('id');
}

function precioHTML(juego) {
    if (juego.precio_original) {
        return `<span class="precio-tachado">${juego.precio_original} €</span>
                <strong class="precio-actual">${juego.precio} €</strong>`;
    }
    return `<strong class="precio-actual">${juego.precio} €</strong>`;
}

async function cargarDetalles() {
    const id = getIdFromURL();
    const url = id ? `${API}/juegos/${id}/` : `${API}/juegos/?destacado=true`;

    let juego;
    const res = await fetch(url);
    if (id) {
        if (!res.ok) { mostrarError(); return; }
        juego = await res.json();
    } else {
        const lista = await res.json();
        if (!lista.length) { mostrarError(); return; }
        juego = lista[0];
    }

    renderJuego(juego);
    if (juego.genero) {
        cargarSimilares(juego.genero.id, juego.id);
    }
}

function renderJuego(j) {
    document.getElementById('titulo-juego').textContent = j.titulo.toUpperCase();

    document.getElementById('img-principal').src = `img/${j.imagen}`;
    document.getElementById('img-principal').alt = j.titulo;

    document.getElementById('info-lateral').innerHTML = `
        <img src="img/${j.imagen}" alt="${j.titulo}" class="mini-logo">
        <p>${j.descripcion}</p>
        <p><strong>Género:</strong> ${j.genero ? j.genero.nombre : '—'}</p>
        <p><strong>Plataforma:</strong> ${j.plataforma ? j.plataforma.nombre : '—'}</p>
        <p><strong>Lanzamiento:</strong> ${j.fecha_lanzamiento}</p>
    `;

    document.getElementById('opciones-compra').innerHTML = `
        <div class="item-compra">
            <span>Comprar ${j.titulo} &nbsp; ${precioHTML(j)}</span>
            <button class="btn-comprar">COMPRAR</button>
        </div>
    `;

    document.getElementById('descripcion-contenido').innerHTML = `
        <h3>• Descripción</h3>
        <p>${j.descripcion}</p>
        <p><strong>Stock disponible:</strong> ${j.stock} unidades</p>
    `;
}

async function cargarSimilares(generoId, juegoActualId) {
    const res = await fetch(`${API}/juegos/?genero=${generoId}`);
    const juegos = await res.json();
    const similares = juegos.filter(j => j.id !== juegoActualId).slice(0, 3);

    document.getElementById('similares-imgs').innerHTML = similares.map(j => `
        <a href="GamekeyDetalles.html?id=${j.id}">
            <img src="img/${j.imagen}" alt="${j.titulo}" title="${j.titulo}">
        </a>
    `).join('');
}

function mostrarError() {
    document.querySelector('.main').innerHTML = `
        <div style="text-align:center; padding:4rem;">
            <h2>Juego no encontrado</h2>
            <a href="GamekeyInicio.html">← Volver al inicio</a>
        </div>
    `;
}

cargarDetalles();
