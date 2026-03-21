/* ============================================================
   MARIGOLD & CO. — main.js
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ── Navbar scroll shrink ── */
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 40);
    });
  }

  /* ── Scroll-triggered fade-up for elements with .scroll-fade ── */
  const scrollFadeEls = document.querySelectorAll('.scroll-fade');
  if (scrollFadeEls.length && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          entry.target.style.animationDelay = (i * 0.1) + 's';
          entry.target.classList.add('fade-up');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    scrollFadeEls.forEach(el => observer.observe(el));
  }

  /* ── Shop: filter buttons ── */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const productCards = document.querySelectorAll('.product-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.dataset.filter;
      productCards.forEach(card => {
        const match = filter === 'all' || card.dataset.category === filter;
        card.style.display = match ? 'block' : 'none';
      });
    });
  });

  /* ── Contact form: validation only ── */
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      if (!contactForm.checkValidity()) {
        e.preventDefault();      
        e.stopPropagation();
        contactForm.classList.add('was-validated');
        return;
      }
      // form is valid — do NOT call e.preventDefault()
      // let it submit normally to Django view
      contactForm.classList.add('was-validated');
    });
  }

  /* ── Newsletter form ── */

  /* ── Smooth-scroll for anchor links ── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

});