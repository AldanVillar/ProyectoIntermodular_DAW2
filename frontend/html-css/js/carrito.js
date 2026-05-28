const STORAGE_KEY = 'gamekey_carrito';

function getCarrito() {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
}

function guardarCarrito(carrito) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(carrito));
}

function precioHTML(item) {
    if (item.precio_original) {
        return `<span class="precio-tachado">${parseFloat(item.precio_original).toFixed(2)} €</span>
                <strong class="precio-actual">${parseFloat(item.precio).toFixed(2)} €</strong>`;
    }
    return `<strong class="precio-actual">${parseFloat(item.precio).toFixed(2)} €</strong>`;
}

function renderCarrito() {
    const carrito = getCarrito();
    const lista = document.getElementById('lista-carrito');
    const resumen = document.getElementById('resumen-carrito');

    if (carrito.length === 0) {
        lista.innerHTML = `
            <div class="carrito-vacio">
                <i class="fas fa-shopping-cart icono-vacio"></i>
                <h2>Tu carrito está vacío</h2>
                <a href="GamekeyInicio.html" class="btn-seguir">Explorar juegos</a>
            </div>
        `;
        resumen.innerHTML = '';
        return;
    }

    lista.innerHTML = carrito.map((item, i) => `
        <div class="carrito-item">
            <img src="img/${item.imagen}" alt="${item.titulo}" class="carrito-item-img">
            <div class="carrito-item-info">
                <h3>${item.titulo}</h3>
                <p class="carrito-plataforma">${item.plataforma}</p>
            </div>
            <div class="carrito-item-precio">
                ${precioHTML(item)}
            </div>
            <button class="btn-eliminar" onclick="eliminarItem(${i})" title="Eliminar">
                <i class="fas fa-trash"></i>
            </button>
        </div>
    `).join('');

    const total = carrito.reduce((acc, item) => acc + parseFloat(item.precio), 0);

    resumen.innerHTML = `
        <div class="resumen-box">
            <h2>Resumen del pedido</h2>
            <div class="resumen-linea">
                <span>${carrito.length} juego${carrito.length !== 1 ? 's' : ''}</span>
                <span>${total.toFixed(2)} €</span>
            </div>
            <div class="resumen-total">
                <span>Total</span>
                <span class="total-precio">${total.toFixed(2)} €</span>
            </div>
            <button class="btn-finalizar" onclick="finalizarCompra()">Finalizar Compra</button>
            <a href="GamekeyInicio.html" class="btn-seguir">Seguir comprando</a>
        </div>
    `;
}

function eliminarItem(index) {
    const carrito = getCarrito();
    carrito.splice(index, 1);
    guardarCarrito(carrito);
    actualizarBadgeCarrito();
    renderCarrito();
}

function finalizarCompra() {
    localStorage.removeItem(STORAGE_KEY);
    actualizarBadgeCarrito();
    document.getElementById('overlay-compra').classList.add('visible');
}

renderCarrito();
