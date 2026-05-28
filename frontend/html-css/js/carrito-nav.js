function actualizarBadgeCarrito() {
    const badge = document.getElementById('cart-count');
    if (!badge) return;
    const carrito = JSON.parse(localStorage.getItem('gamekey_carrito') || '[]');
    badge.textContent = carrito.length > 0 ? carrito.length : '';
}

actualizarBadgeCarrito();
