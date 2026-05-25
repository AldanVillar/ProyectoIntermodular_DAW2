const BUSCADOR_API = 'http://127.0.0.1:8000/api';

let catalogoJuegos = [];

async function cargarCatalogo() {
    try {
        const res = await fetch(`${BUSCADOR_API}/juegos/`);
        catalogoJuegos = await res.json();
    } catch (e) {
        console.error('Buscador: no se pudo cargar el catálogo', e);
    }
}

function filtrar(query) {
    const q = query.trim().toLowerCase();
    if (!q) return [];
    return catalogoJuegos.filter(j => j.titulo.toLowerCase().startsWith(q));
}

function precioTexto(juego) {
    if (juego.precio_original) {
        return `<span style="text-decoration:line-through;color:#888;margin-right:6px">${juego.precio_original} €</span>${juego.precio} €`;
    }
    return `${juego.precio} €`;
}

function renderDropdown(resultados) {
    const dropdown = document.getElementById('buscador-dropdown');

    if (!resultados.length) {
        dropdown.innerHTML = '<p class="buscador-sin-resultados">Sin resultados</p>';
    } else {
        dropdown.innerHTML = resultados.slice(0, 8).map(j => `
            <a class="buscador-resultado" href="GamekeyDetalles.html?id=${j.id}">
                <img src="img/${j.imagen}" alt="${j.titulo}">
                <div class="buscador-info">
                    <span class="buscador-titulo">${j.titulo}</span>
                    <span class="buscador-meta">${j.genero ? j.genero.nombre : ''} · ${j.plataforma ? j.plataforma.nombre : ''}</span>
                </div>
                <span class="buscador-precio">${precioTexto(j)}</span>
            </a>
        `).join('');
    }

    dropdown.classList.add('visible');
}

function ocultarDropdown() {
    const dropdown = document.getElementById('buscador-dropdown');
    if (dropdown) dropdown.classList.remove('visible');
}

function iniciarBuscador() {
    const searchDiv = document.querySelector('.search');
    const input = searchDiv.querySelector('input');
    input.placeholder = 'Buscar juego...';

    const dropdown = document.createElement('div');
    dropdown.id = 'buscador-dropdown';
    dropdown.className = 'buscador-dropdown';
    searchDiv.appendChild(dropdown);

    input.addEventListener('input', () => {
        const query = input.value;
        if (!query.trim()) {
            ocultarDropdown();
            return;
        }
        renderDropdown(filtrar(query));
    });

    input.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            ocultarDropdown();
            input.value = '';
        }
        if (e.key === 'Enter') {
            const resultados = filtrar(input.value);
            if (resultados.length) {
                window.location.href = `GamekeyDetalles.html?id=${resultados[0].id}`;
            }
        }
    });

    const boton = searchDiv.querySelector('a');
    if (boton) {
        boton.addEventListener('click', (e) => {
            e.preventDefault();
            const resultados = filtrar(input.value);
            if (resultados.length) {
                window.location.href = `GamekeyDetalles.html?id=${resultados[0].id}`;
            }
        });
    }

    document.addEventListener('click', (e) => {
        if (!searchDiv.contains(e.target)) {
            ocultarDropdown();
        }
    });
}

cargarCatalogo();
iniciarBuscador();
