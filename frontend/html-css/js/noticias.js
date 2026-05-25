const API = 'http://127.0.0.1:8000/api';

function formatearFecha(fechaISO) {
    const fecha = new Date(fechaISO);
    return fecha.toLocaleDateString('es-ES', { year: 'numeric', month: 'long', day: 'numeric' });
}

async function cargarNoticias() {
    const res = await fetch(`${API}/noticias/`);
    const noticias = await res.json();
    if (!noticias.length) return;

    document.getElementById('noticias-container').innerHTML = noticias.map(n => `
        <article class="noticia-card">
            ${n.imagen ? `<img src="img/${n.imagen}" alt="${n.titulo}">` : ''}
            <div class="noticia-info">
                <span class="fecha">${formatearFecha(n.fecha)}</span>
                <h2>${n.titulo}</h2>
                <p>${n.contenido}</p>
                <a href="#" class="leer-mas">Leer más...</a>
            </div>
        </article>
    `).join('');
}

cargarNoticias();
