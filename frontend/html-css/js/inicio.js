const API = 'http://127.0.0.1:8000/api';

function precioHTML(juego) {
    if (juego.precio_original) {
        return `<span class="item-precio">
            <span class="precio-tachado-lista">${juego.precio_original} €</span>
            ${juego.precio} €
        </span>`;
    }
    return `<span class="item-precio">${juego.precio} €</span>`;
}

function filaJuego(j) {
    return `<li>
        <a class="item-fila" href="GamekeyDetalles.html?id=${j.id}">
            <img src="img/${j.imagen}" alt="${j.titulo}">
            <div class="item-info">
                <span class="item-titulo">${j.titulo}</span>
                <span class="item-meta">${j.genero ? j.genero.nombre : ''} · ${j.plataforma ? j.plataforma.nombre : ''}</span>
            </div>
            ${precioHTML(j)}
        </a>
    </li>`;
}

function filaNoticia(n) {
    const fecha = new Date(n.fecha).toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' });
    return `<li>
        <a class="item-fila" href="GamekeyNoticias.html">
            ${n.imagen ? `<img src="img/${n.imagen}" alt="${n.titulo}">` : ''}
            <div class="item-info">
                <span class="item-titulo">${n.titulo}</span>
                <span class="item-fecha">${fecha}</span>
            </div>
        </a>
    </li>`;
}

function setLista(id, html) {
    const el = document.getElementById(id);
    if (el) el.innerHTML = html;
}

window.addEventListener('load', async function () {
    try {
        const resDestacados = await fetch(`${API}/juegos/?destacado=true`);
        const destacados = await resDestacados.json();
        if (destacados.length) {
            setLista('lista-destacados', destacados.slice(0, 6).map(filaJuego).join(''));
        } else {
            setLista('lista-destacados', '<li style="padding:14px;color:#aaa;">No hay juegos destacados.</li>');
        }
    } catch (e) {
        setLista('lista-destacados', `<li style="padding:14px;color:#f88;">Error: ${e.message}</li>`);
    }

    try {
        const resDescuentos = await fetch(`${API}/juegos/?en_descuento=true`);
        const descuentos = await resDescuentos.json();
        if (descuentos.length) {
            setLista('lista-descuentos', descuentos.slice(0, 6).map(filaJuego).join(''));
        } else {
            setLista('lista-descuentos', '<li style="padding:14px;color:#aaa;">No hay juegos en descuento.</li>');
        }
    } catch (e) {
        setLista('lista-descuentos', `<li style="padding:14px;color:#f88;">Error: ${e.message}</li>`);
    }

    try {
        const resNoticias = await fetch(`${API}/noticias/`);
        const noticias = await resNoticias.json();
        if (noticias.length) {
            setLista('lista-noticias-inicio', noticias.slice(0, 4).map(filaNoticia).join(''));
        } else {
            setLista('lista-noticias-inicio', '<li style="padding:14px;color:#aaa;">No hay noticias.</li>');
        }
    } catch (e) {
        setLista('lista-noticias-inicio', `<li style="padding:14px;color:#f88;">Error: ${e.message}</li>`);
    }
});
