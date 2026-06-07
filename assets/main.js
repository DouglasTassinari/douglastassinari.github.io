/* ==========================================================================
   DOUGLAS TASSINARI — main.js
   1. Marca <html> como "js" (ativa animações só quando há JavaScript)
   2. Menu mobile (abre/fecha + fecha ao clicar em link)
   3. Estado ativo da navegação (destaca a página atual)
   4. Animações de entrada (IntersectionObserver — fallback seguro)
   ========================================================================== */
(function () {
  'use strict';

  // 1. Sinaliza que o JS está ativo (o CSS usa .js para esconder/animar com segurança)
  document.documentElement.classList.add('js');

  document.addEventListener('DOMContentLoaded', function () {

    /* 2. MENU MOBILE -------------------------------------------------------- */
    var toggle = document.getElementById('menuToggle');
    var links = document.getElementById('navLinks');
    if (toggle && links) {
      toggle.addEventListener('click', function () {
        var open = links.classList.toggle('open');
        toggle.classList.toggle('open', open);
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      links.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', function () {
          links.classList.remove('open');
          toggle.classList.remove('open');
          toggle.setAttribute('aria-expanded', 'false');
        });
      });
    }

    /* 3. ESTADO ATIVO DA NAVEGAÇÃO ----------------------------------------- */
    // Marca o link cujo href corresponde ao arquivo atual.
    var current = location.pathname.split('/').pop() || 'index.html';
    if (links) {
      links.querySelectorAll('a').forEach(function (a) {
        var href = a.getAttribute('href');
        if (!href) return;
        var file = href.split('/').pop();
        if (file === current || (current === 'index.html' && (href === './' || href === '/'))) {
          a.classList.add('active');
          a.setAttribute('aria-current', 'page');
        }
      });
    }

    /* 4. ANIMAÇÕES DE ENTRADA ---------------------------------------------- */
    var reveals = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window && reveals.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('in');
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      reveals.forEach(function (el) { io.observe(el); });
    } else {
      // Sem suporte: garante tudo visível
      reveals.forEach(function (el) { el.classList.add('in'); });
    }
  });
})();
