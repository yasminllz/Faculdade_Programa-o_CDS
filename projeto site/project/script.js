// ===== PRODUCTS DATA =====
const PRODUCTS = [
  { id: 1, name: 'Bolo de Chocolate Belga', category: 'bolos', price: 180, desc: 'Camadas de chocolate belga com ganache aveludada', img: 'https://images.pexels.com/photos/291528/pexels-photo-291528.jpeg?auto=compress&cs=tinysrgb&w=400' },
  { id: 2, name: 'Bolo Red Velvet', category: 'bolos', price: 220, desc: 'Clássico red velvet com cream cheese artesanal', img: 'https://images.pexels.com/photos/1126359/pexels-photo-1126359.jpeg?auto=compress&cs=tinysrgb&w=400' },
  { id: 3, name: 'Bolo de Morango', category: 'bolos', price: 195, desc: 'Pão de ló leve com morangos frescos e chantilly', img: 'https://images.pexels.com/photos/1854652/pexels-photo-1854652.jpeg?auto=compress&cs=tinysrgb&w=400' },
  { id: 4, name: 'Rocambole Prestígio', category: 'bolos', price: 120, desc: 'Recheio cremoso de coco com cobertura de chocolate', img: 'https://images.pexels.com/photos/2144112/pexels-photo-2144112.jpeg?auto=compress&cs=tinysrgb&w=400' },
  { id: 5, name: 'Trufa de Chocolate', category: 'doces', price: 45, desc: 'Trufas artesanais de chocolate meio amargo', img: 'https://images.pexels.com/photos/918327/pexels-photo-918327.jpeg?auto=compress&cs=tinysrgb&w=400' },
  { id: 6, name: 'Brigadeiro Gourmet', category: 'doces', price: 40, desc: 'Caixa com 12 brigadeiros em sabores variados', img: 'https://images.pexels.com/photos/3776951/pexels-photo-3776951.jpeg?auto=compress&cs=tinysrgb&w=400' },
  { id: 7, name: 'Macaron Francês', category: 'doces', price: 80, desc: 'Macarons delicados em variados sabores franceses', img: 'https://images.pexels.com/photos/239578/pexels-photo-239578.jpeg?auto=compress&cs=tinysrgb&w=400' },
  { id: 8, name: 'Doce de Leite Artesanal', category: 'doces', price: 35, desc: 'Doce de leite cremoso feito no tacho de cobre', img: 'https://images.pexels.com/photos/1128678/pexels-photo-1128678.jpeg?auto=compress&cs=tinysrgb&w=400' },
  { id: 9, name: 'Donuts Gourmet', category: 'sobremesas', price: 60, desc: 'Donuts artesanais com coberturas especiais', img: 'https://images.pexels.com/photos/2955820/pexels-photo-2955820.jpeg?auto=compress&cs=tinysrgb&w=400' },
  { id: 10, name: 'Pudim Premium', category: 'sobremesas', price: 75, desc: 'Pudim de leite condensado com calda de caramelo', img: 'https://images.pexels.com/photos/3026802/pexels-photo-3026802.jpeg?auto=compress&cs=tinysrgb&w=400' },
  { id: 11, name: 'Brownie com Nozes', category: 'sobremesas', price: 55, desc: 'Brownie fudgy com nozes tostadas e flor de sal', img: 'https://images.pexels.com/photos/45202/brownie-dessert-cake-sweet-45202.jpeg?auto=compress&cs=tinysrgb&w=400' },
  { id: 12, name: 'Torta de Ricota', category: 'sobremesas', price: 150, desc: 'Torta de ricota italiana com calda de frutas vermelhas', img: 'https://images.pexels.com/photos/1099680/pexels-photo-1099680.jpeg?auto=compress&cs=tinysrgb&w=400' },
];

// ===== CART MANAGEMENT =====
function getCart() {
  return JSON.parse(localStorage.getItem('yas_cart') || '[]');
}

function saveCart(cart) {
  localStorage.setItem('yas_cart', JSON.stringify(cart));
  updateCartBadge();
}

function addToCart(productId) {
  const product = PRODUCTS.find(p => p.id === productId);
  if (!product) return;
  const cart = getCart();
  const existing = cart.find(item => item.id === productId);
  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({ ...product, qty: 1 });
  }
  saveCart(cart);
  showToast(`${product.name} adicionado ao carrinho!`, 'success');
}

function removeFromCart(productId) {
  const cart = getCart().filter(item => item.id !== productId);
  saveCart(cart);
}

function updateQty(productId, delta) {
  const cart = getCart();
  const item = cart.find(i => i.id === productId);
  if (!item) return;
  item.qty = Math.max(1, item.qty + delta);
  saveCart(cart);
  renderCart();
}

function getCartTotal() {
  return getCart().reduce((sum, item) => sum + item.price * item.qty, 0);
}

function getCartCount() {
  return getCart().reduce((sum, item) => sum + item.qty, 0);
}

function updateCartBadge() {
  const badges = document.querySelectorAll('.cart-badge');
  const count = getCartCount();
  badges.forEach(b => {
    b.textContent = count;
    b.style.display = count > 0 ? 'flex' : 'none';
  });
}

// ===== RENDER PRODUCTS =====
function renderProducts(container, filter = 'todos', limit = null) {
  if (!container) return;
  let filtered = filter === 'todos' ? PRODUCTS : PRODUCTS.filter(p => p.category === filter);
  if (limit) filtered = filtered.slice(0, limit);
  container.innerHTML = filtered.map(p => `
    <div class="product-card fade-in" data-category="${p.category}">
      <div class="product-img-wrap">
        <img src="${p.img}" alt="${p.name}" loading="lazy">
        <span class="product-category-badge">${categoryLabel(p.category)}</span>
      </div>
      <div class="product-info">
        <h3 class="product-name">${p.name}</h3>
        <p class="product-desc">${p.desc}</p>
        <div class="product-footer">
          <span class="product-price">R$ ${p.price.toFixed(2).replace('.', ',')}</span>
          <button class="add-cart-btn" onclick="handleAddToCart(${p.id}, this)">+ Carrinho</button>
        </div>
      </div>
    </div>
  `).join('');
  observeFadeIn();
}

function categoryLabel(cat) {
  const map = { bolos: 'Bolos', doces: 'Doces', sobremesas: 'Sobremesas' };
  return map[cat] || cat;
}

function handleAddToCart(id, btn) {
  addToCart(id);
  btn.textContent = '✓ Adicionado';
  btn.classList.add('added');
  setTimeout(() => {
    btn.textContent = '+ Carrinho';
    btn.classList.remove('added');
  }, 1800);
}

// ===== RENDER CART =====
function renderCart() {
  const container = document.getElementById('cart-items');
  const emptyState = document.getElementById('cart-empty');
  const summary = document.getElementById('cart-summary');
  if (!container) return;

  const cart = getCart();

  if (cart.length === 0) {
    container.innerHTML = '';
    if (emptyState) emptyState.style.display = 'block';
    if (summary) summary.style.display = 'none';
    return;
  }

  if (emptyState) emptyState.style.display = 'none';
  if (summary) summary.style.display = 'block';

  container.innerHTML = cart.map(item => `
    <div class="cart-item fade-in">
      <img class="cart-item-img" src="${item.img}" alt="${item.name}">
      <div class="cart-item-info">
        <div class="cart-item-name">${item.name}</div>
        <div class="cart-item-cat">${categoryLabel(item.category)}</div>
        <div class="cart-item-price">R$ ${(item.price * item.qty).toFixed(2).replace('.', ',')}</div>
      </div>
      <div class="cart-qty">
        <button class="qty-btn" onclick="updateQty(${item.id}, -1)">−</button>
        <span class="qty-display">${item.qty}</span>
        <button class="qty-btn" onclick="updateQty(${item.id}, 1)">+</button>
      </div>
      <button class="cart-remove" onclick="removeFromCart(${item.id}); renderCart();" title="Remover">✕</button>
    </div>
  `).join('');

  const total = getCartTotal();
  const subtotal = document.getElementById('cart-subtotal');
  const totalEl = document.getElementById('cart-total');
  const deliveryEl = document.getElementById('cart-delivery');
  const delivery = total > 150 ? 0 : 15;

  if (subtotal) subtotal.textContent = `R$ ${total.toFixed(2).replace('.', ',')}`;
  if (deliveryEl) deliveryEl.textContent = delivery === 0 ? 'Grátis' : `R$ ${delivery.toFixed(2).replace('.', ',')}`;
  if (totalEl) totalEl.textContent = `R$ ${(total + delivery).toFixed(2).replace('.', ',')}`;

  observeFadeIn();
}

// ===== AUTH =====
function getUsers() {
  return JSON.parse(localStorage.getItem('yas_users') || '[]');
}

function getCurrentUser() {
  return JSON.parse(localStorage.getItem('yas_current_user') || 'null');
}

function handleRegister(e) {
  e.preventDefault();
  const name = document.getElementById('reg-name').value.trim();
  const email = document.getElementById('reg-email').value.trim().toLowerCase();
  const password = document.getElementById('reg-password').value;
  const confirm = document.getElementById('reg-confirm').value;

  clearAlert('auth-alert');

  if (!name || !email || !password || !confirm) {
    showAlert('auth-alert', 'Por favor, preencha todos os campos.', 'error');
    return;
  }
  if (password.length < 6) {
    showAlert('auth-alert', 'A senha deve ter pelo menos 6 caracteres.', 'error');
    return;
  }
  if (password !== confirm) {
    showAlert('auth-alert', 'As senhas não conferem.', 'error');
    return;
  }

  const users = getUsers();
  if (users.find(u => u.email === email)) {
    showAlert('auth-alert', 'Este e-mail já está cadastrado.', 'error');
    return;
  }

  users.push({ name, email, password, createdAt: new Date().toISOString() });
  localStorage.setItem('yas_users', JSON.stringify(users));
  localStorage.setItem('yas_current_user', JSON.stringify({ name, email }));

  showAlert('auth-alert', 'Cadastro realizado com sucesso! Redirecionando...', 'success');
  setTimeout(() => { window.location.href = 'index.html'; }, 1500);
}

function handleLogin(e) {
  e.preventDefault();
  const email = document.getElementById('login-email').value.trim().toLowerCase();
  const password = document.getElementById('login-password').value;

  clearAlert('auth-alert');

  if (!email || !password) {
    showAlert('auth-alert', 'Por favor, preencha todos os campos.', 'error');
    return;
  }

  const users = getUsers();
  const user = users.find(u => u.email === email && u.password === password);

  if (!user) {
    showAlert('auth-alert', 'E-mail ou senha incorretos.', 'error');
    return;
  }

  localStorage.setItem('yas_current_user', JSON.stringify({ name: user.name, email: user.email }));
  showAlert('auth-alert', `Bem-vinda, ${user.name}! Redirecionando...`, 'success');
  setTimeout(() => { window.location.href = 'index.html'; }, 1200);
}

function handleLogout() {
  localStorage.removeItem('yas_current_user');
  window.location.reload();
}

function updateNavAuth() {
  const user = getCurrentUser();
  const authArea = document.getElementById('nav-auth');
  if (!authArea) return;

  if (user) {
    authArea.innerHTML = `
      <div class="user-menu">
        <button class="user-menu-btn">👤 ${user.name.split(' ')[0]} ▾</button>
        <div class="user-dropdown">
          <a href="reserva.html">Meus Pedidos</a>
          <a href="#" onclick="handleLogout(); return false;">Sair</a>
        </div>
      </div>
    `;
  } else {
    authArea.innerHTML = `<a href="login.html" class="btn-nav-cta">Entrar</a>`;
  }
}

// ===== PAYMENT =====
function initPaymentPage() {
  const total = getCartTotal();
  if (total === 0 && document.getElementById('payment-total')) {
    document.getElementById('payment-total').textContent = 'R$ 0,00';
  } else if (document.getElementById('payment-total')) {
    const delivery = total > 150 ? 0 : 15;
    document.getElementById('payment-total').textContent = `R$ ${(total + delivery).toFixed(2).replace('.', ',')}`;
  }

  document.querySelectorAll('.payment-option').forEach(opt => {
    opt.addEventListener('click', () => {
      document.querySelectorAll('.payment-option').forEach(o => o.classList.remove('active'));
      opt.classList.add('active');
      const method = opt.dataset.method;
      showPaymentForm(method);
    });
  });
}

function showPaymentForm(method) {
  document.querySelectorAll('.payment-form-section').forEach(s => s.style.display = 'none');
  const target = document.getElementById(`form-${method}`);
  if (target) target.style.display = 'block';
}

function handlePayment(e) {
  e.preventDefault();
  const modal = document.getElementById('confirm-modal');
  if (modal) {
    modal.classList.add('open');
    localStorage.removeItem('yas_cart');
    updateCartBadge();
  }
}

// ===== RESERVATION =====
function handleReservation(e) {
  e.preventDefault();
  showToast('Pedido enviado com sucesso! Entraremos em contato em breve.', 'success');
  e.target.reset();
}

// ===== CONTACT =====
function handleContact(e) {
  e.preventDefault();
  showToast('Mensagem enviada! Responderemos em até 24 horas.', 'success');
  e.target.reset();
}

// ===== UI HELPERS =====
function showToast(message, type = 'info') {
  let container = document.querySelector('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  const icons = { success: '✓', error: '✕', info: 'ℹ' };
  toast.innerHTML = `<span>${icons[type] || icons.info}</span> ${message}`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(100%)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}

function showAlert(id, message, type) {
  const el = document.getElementById(id);
  if (!el) return;
  el.className = `alert alert-${type}`;
  el.innerHTML = `<span>${type === 'success' ? '✓' : '✕'}</span> ${message}`;
  el.style.display = 'flex';
}

function clearAlert(id) {
  const el = document.getElementById(id);
  if (el) el.style.display = 'none';
}

// ===== NAVBAR =====
function initNavbar() {
  const navbar = document.querySelector('.navbar');
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');

  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    });
  }

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
    });
  }

  updateCartBadge();
  updateNavAuth();

  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath) link.classList.add('active');
  });
}

// ===== BACK TO TOP =====
function initBackToTop() {
  const btn = document.getElementById('back-to-top');
  if (!btn) return;
  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 400);
  });
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

// ===== SCROLL ANIMATIONS =====
function observeFadeIn() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.fade-in:not(.visible)').forEach(el => observer.observe(el));
}

// ===== FILTER TABS =====
function initFilterTabs() {
  const tabs = document.querySelectorAll('.filter-tab');
  const grid = document.getElementById('products-grid');
  if (!tabs.length || !grid) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      renderProducts(grid, tab.dataset.filter);
    });
  });

  renderProducts(grid, 'todos');
}

// ===== INIT =====
document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initBackToTop();
  observeFadeIn();

  const homeProdGrid = document.getElementById('home-products-grid');
  if (homeProdGrid) renderProducts(homeProdGrid, 'todos', 8);

  const prodGrid = document.getElementById('products-grid');
  if (prodGrid) initFilterTabs();

  const cartContainer = document.getElementById('cart-items');
  if (cartContainer) renderCart();

  const paymentPage = document.getElementById('payment-page');
  if (paymentPage) initPaymentPage();

  const reservaForm = document.getElementById('reserva-form');
  if (reservaForm) reservaForm.addEventListener('submit', handleReservation);

  const contactForm = document.getElementById('contact-form');
  if (contactForm) contactForm.addEventListener('submit', handleContact);

  const registerForm = document.getElementById('register-form');
  if (registerForm) registerForm.addEventListener('submit', handleRegister);

  const loginForm = document.getElementById('login-form');
  if (loginForm) loginForm.addEventListener('submit', handleLogin);

  const paymentForm = document.getElementById('payment-form');
  if (paymentForm) paymentForm.addEventListener('submit', handlePayment);

  const confirmClose = document.getElementById('confirm-close');
  if (confirmClose) {
    confirmClose.addEventListener('click', () => {
      window.location.href = 'index.html';
    });
  }

  const heroImg = document.querySelector('.hero-bg');
  if (heroImg) {
    window.addEventListener('scroll', () => {
      const scrolled = window.scrollY;
      heroImg.style.transform = `scale(1.05) translateY(${scrolled * 0.3}px)`;
    });
  }

  const newsletterForms = document.querySelectorAll('.newsletter-form');
  newsletterForms.forEach(f => {
    f.addEventListener('submit', e => {
      e.preventDefault();
      showToast('Obrigada! Você receberá nossas novidades em breve.', 'success');
      f.reset();
    });
  });
});
