// Keep the template's responsive navigation accessible to keyboard users.
document.addEventListener('DOMContentLoaded', function () {
  var button = document.querySelector('.greedy-nav button');
  var menu = document.querySelector('.greedy-nav .hidden-links');
  if (!button || !menu) return;
  function syncExpanded() {
    button.setAttribute('aria-expanded', String(!menu.classList.contains('hidden')));
  }
  new MutationObserver(syncExpanded).observe(menu, { attributes: true, attributeFilter: ['class'] });
  menu.addEventListener('click', function (event) {
    if (event.target.closest('a')) {
      menu.classList.add('hidden');
      button.classList.remove('close');
    }
  });
  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' && !menu.classList.contains('hidden')) {
      menu.classList.add('hidden');
      button.classList.remove('close');
      button.focus();
    }
  });
});
