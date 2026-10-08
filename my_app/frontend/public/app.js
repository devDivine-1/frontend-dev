document.addEventListener('DOMContentLoaded', () => {
  const terminalBody = document.getElementById('terminalBody');
  const lines = terminalBody.querySelectorAll('.line');

  lines.forEach((line, i) => {
    line.style.opacity = '0';
    line.style.transform = 'translateY(10px)';
    line.style.transition = 'all 0.4s ease';
    setTimeout(() => {
      line.style.opacity = '1';
      line.style.transform = 'translateY(0)';
    }, 600 + i * 500);
  });

  document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.style.borderColor = '#6c5ce7';
    });
    card.addEventListener('mouseleave', () => {
      card.style.borderColor = '#1e1e2e';
    });
  });

  const ctaHero = document.getElementById('ctaHero');
  const ctaNav = document.getElementById('ctaNav');
  const launchHandler = () => {
    window.scrollTo({ top: document.getElementById('features').offsetTop - 60, behavior: 'smooth' });
  };
  ctaHero.addEventListener('click', launchHandler);
  ctaNav.addEventListener('click', launchHandler);

  fetch('/api/health')
    .then(res => res.json())
    .then(data => {
      console.log('API health:', data);
    })
    .catch(() => {});

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.card, .stat, .code-block').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'all 0.5s ease';
    observer.observe(el);
  });
});
