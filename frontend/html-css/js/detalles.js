const API = 'http://127.0.0.1:8000/api';

let juegoActual = null;

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
    juegoActual = j;

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
            <button class="btn-comprar" id="btn-comprar">COMPRAR</button>
        </div>
    `;

    document.getElementById('btn-comprar').addEventListener('click', () => agregarAlCarrito(juegoActual));

    document.getElementById('descripcion-contenido').innerHTML = `
        <h3>• Descripción</h3>
        <p>${j.descripcion}</p>
        <p><strong>Stock disponible:</strong> ${j.stock} unidades</p>
    `;
}

function agregarAlCarrito(juego) {
    const carrito = JSON.parse(localStorage.getItem('gamekey_carrito') || '[]');
    const yaExiste = carrito.some(j => j.id === juego.id);

    if (yaExiste) {
        mostrarNotificacion(`"${juego.titulo}" ya está en tu carrito`);
        return;
    }

    carrito.push({
        id: juego.id,
        titulo: juego.titulo,
        precio: juego.precio,
        precio_original: juego.precio_original || null,
        imagen: juego.imagen,
        plataforma: juego.plataforma ? juego.plataforma.nombre : 'PC'
    });

    localStorage.setItem('gamekey_carrito', JSON.stringify(carrito));
    actualizarBadgeCarrito();
    mostrarNotificacion(`"${juego.titulo}" añadido al carrito`);
}

function mostrarNotificacion(mensaje) {
    const notif = document.createElement('div');
    notif.className = 'notif-carrito';
    notif.textContent = mensaje;
    document.body.appendChild(notif);
    setTimeout(() => notif.classList.add('visible'), 10);
    setTimeout(() => {
        notif.classList.remove('visible');
        setTimeout(() => notif.remove(), 400);
    }, 2500);
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
