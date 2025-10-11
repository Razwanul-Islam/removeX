document.addEventListener('DOMContentLoaded', function() {
  const menuToggle = document.querySelector('.menu-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');
  const contactForm = document.getElementById('contactForm');
  const formMessage = document.getElementById('formMessage');

  menuToggle.addEventListener('click', function() {
    navMenu.classList.toggle('active');

    const spans = menuToggle.querySelectorAll('span');
    spans.forEach((span, index) => {
      if (navMenu.classList.contains('active')) {
        if (index === 0) span.style.transform = 'rotate(45deg) translate(5px, 5px)';
        if (index === 1) span.style.opacity = '0';
        if (index === 2) span.style.transform = 'rotate(-45deg) translate(7px, -6px)';
      } else {
        span.style.transform = 'none';
        span.style.opacity = '1';
      }
    });
  });

  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      const targetSection = document.querySelector(targetId);

      if (targetSection) {
        const offsetTop = targetSection.offsetTop - 80;
        window.scrollTo({
          top: offsetTop,
          behavior: 'smooth'
        });
      }

      if (navMenu.classList.contains('active')) {
        navMenu.classList.remove('active');
        const spans = menuToggle.querySelectorAll('span');
        spans.forEach(span => {
          span.style.transform = 'none';
          span.style.opacity = '1';
        });
      }
    });
  });

  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const message = document.getElementById('message').value.trim();

    if (!name || !email || !message) {
      showMessage('Please fill in all required fields.', 'error');
      return;
    }

    if (!isValidEmail(email)) {
      showMessage('Please enter a valid email address.', 'error');
      return;
    }

    const submitButton = contactForm.querySelector('button[type="submit"]');
    submitButton.disabled = true;
    submitButton.textContent = 'Sending...';

    setTimeout(() => {
      showMessage('Thank you for your message! We will get back to you soon.', 'success');
      contactForm.reset();
      submitButton.disabled = false;
      submitButton.textContent = 'Send Message';

      setTimeout(() => {
        hideMessage();
      }, 5000);
    }, 1500);
  });

  function showMessage(text, type) {
    formMessage.textContent = text;
    formMessage.className = 'form-message ' + type;
  }

  function hideMessage() {
    formMessage.className = 'form-message';
  }

  function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, observerOptions);

  const animatedElements = document.querySelectorAll('.feature-card, .service-card, .step');
  animatedElements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });

  let lastScrollTop = 0;
  const header = document.querySelector('.header');

  window.addEventListener('scroll', function() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop && scrollTop > 100) {
      header.style.transform = 'translateY(-100%)';
    } else {
      header.style.transform = 'translateY(0)';
    }

    if (scrollTop > 50) {
      header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.15)';
    } else {
      header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    }

    lastScrollTop = scrollTop;
  });
});
