const API = 'http://127.0.0.1:8000/api';

function truncar(texto, max = 100) {
    return texto.length > max ? texto.slice(0, max) + '...' : texto;
}

function precioHTML(juego) {
    if (juego.precio_original) {
        return `<span class="precio-tachado">${juego.precio_original} €</span>
                <span class="precio-actual">${juego.precio} €</span>`;
    }
    return `<span class="precio-actual">${juego.precio} €</span>`;
}

function tarjetaJuego(j) {
    return `
        <div class="juego">
            <a href="GamekeyDetalles.html?id=${j.id}">
                <img src="img/${j.imagen}" alt="${j.titulo}">
            </a>
            <div>
                <h3>${j.titulo}</h3>
                <p>${truncar(j.descripcion)}</p>
                <p>${precioHTML(j)}</p>
            </div>
        </div>
    `;
}

async function cargarTopVentas() {
    const res = await fetch(`${API}/juegos/?top_ventas=true`);
    const juegos = await res.json();
    if (!juegos.length) return;

    document.getElementById('ventas-mes').innerHTML = juegos.slice(0, 7).map(tarjetaJuego).join('');
    document.getElementById('ventas-anio').innerHTML = juegos.slice(7, 11).map(tarjetaJuego).join('');
}

cargarTopVentas();
