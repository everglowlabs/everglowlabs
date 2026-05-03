import { createIcons, Shield, Cpu, Layers } from 'lucide';

// Initialize Lucide Icons
createIcons({
  icons: {
    Shield,
    Cpu,
    Layers
  }
});

// Inject icons into elements
document.getElementById('icon-shield').innerHTML = '<i data-lucide="shield" width="32" height="32"></i>';
document.getElementById('icon-cpu').innerHTML = '<i data-lucide="cpu" width="32" height="32"></i>';
document.getElementById('icon-layers').innerHTML = '<i data-lucide="layers" width="32" height="32"></i>';

// Re-run createIcons to pick up the injected HTML
createIcons({
  icons: {
    Shield,
    Cpu,
    Layers
  }
});

// Scroll Animation Observer
const observerOptions = {
  root: null,
  rootMargin: '0px',
  threshold: 0.1
};

const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

// Add fade-up class to sections and observe them
document.addEventListener('DOMContentLoaded', () => {
  const sections = document.querySelectorAll('.section, .glass-card, .hero-content');
  sections.forEach(section => {
    section.classList.add('fade-up');
    observer.observe(section);
  });

  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth'
        });
      }
    });
  });
});
