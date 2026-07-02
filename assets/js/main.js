/* Menu mobile + animação de entrada.
   Progressive enhancement: sem JS (ou com prefers-reduced-motion),
   todo o conteúdo permanece visível e navegável. */
(function () {
  'use strict';

  var toggle = document.querySelector('.menu-toggle');
  var links = document.getElementById('nav-links');

  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    links.addEventListener('click', function (event) {
      if (event.target.closest('a')) {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var targets = document.querySelectorAll('.fade-in');

  if (!reducedMotion && 'IntersectionObserver' in window && targets.length) {
    targets.forEach(function (el) { el.classList.add('will-animate'); });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });

    targets.forEach(function (el) { observer.observe(el); });
  }
})();
