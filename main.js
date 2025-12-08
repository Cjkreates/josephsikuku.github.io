document.addEventListener('DOMContentLoaded', () => {
    
    // --- SCROLL PROGRESS BAR ---
window.addEventListener('scroll', () => {
    const progressBar = document.getElementById('scroll-progress');
    if (progressBar) {
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (scrollTop / scrollHeight) * 100;
        progressBar.style.width = scrolled + "%";
    }
});
    // 1. Theme Toggle
    const themeBtn = document.getElementById('theme-toggle');
    const html = document.documentElement;
    const icon = themeBtn.querySelector('i');

    const savedTheme = localStorage.getItem('theme') || 
                      (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    
    html.setAttribute('data-theme', savedTheme);
    updateIcon(savedTheme);

    themeBtn.addEventListener('click', () => {
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateIcon(newTheme);
    });

    function updateIcon(theme) {
        icon.className = theme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    }

    // 2. Mobile Menu
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.querySelector('.nav-links');

    if(hamburger) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('open');
            hamburger.innerHTML = navLinks.classList.contains('open') 
                ? '<i class="fas fa-times"></i>' 
                : '<i class="fas fa-bars"></i>';
        });
    }

    // 3. Dynamic Year
    document.getElementById('year').textContent = new Date().getFullYear();

    // 4. Scroll Animations (Intersection Observer)
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.animate-on-scroll').forEach((el) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'all 0.6s ease-out';
        observer.observe(el);
    });
});


/* --- PIPELINE SIMULATOR LOGIC --- */
const logs = [
    { msg: "Initializing deployment environment...", type: "info", delay: 500 },
    { msg: "Fetching origin/main...", type: "info", delay: 800 },
    { msg: "Verifying GPG signatures...", type: "success", delay: 1200 },
    { msg: ">> STAGE: BUILD STARTED", type: "warn", delay: 1500, stage: 2 },
    { msg: "Running 'docker build -t sikuku-portfolio .'", type: "info", delay: 1800 },
    { msg: "Optimizing assets (CSS/JS)...", type: "info", delay: 2500 },
    { msg: "Build successful. Image size: 45MB", type: "success", delay: 3200 },
    { msg: ">> STAGE: TEST STARTED", type: "warn", delay: 3500, stage: 3 },
    { msg: "Running unit tests...", type: "info", delay: 3800 },
    { msg: "✔ logic.test.js passed", type: "success", delay: 4200 },
    { msg: "✔ ui.test.js passed", type: "success", delay: 4400 },
    { msg: ">> STAGE: DEPLOY STARTED", type: "warn", delay: 5000, stage: 4 },
    { msg: "Connecting to AWS cluster...", type: "info", delay: 5300 },
    { msg: "Applying Terraform configuration...", type: "info", delay: 6000 },
    { msg: "Swapping load balancers...", type: "warn", delay: 6800 },
    { msg: "DEPLOYMENT SUCCESSFUL! 🚀", type: "success", delay: 7500 }
];

function startPipeline() {
    const overlay = document.getElementById('pipeline-overlay');
    const logContainer = document.getElementById('pipeline-logs');
    const stages = document.querySelectorAll('.stage');
    
    // Reset UI
    overlay.classList.remove('hidden');
    logContainer.innerHTML = '';
    stages.forEach(s => {
        s.className = 'stage'; 
        s.innerHTML = s.innerHTML.replace('fa-check', 'fa-circle-notch');
    });
    document.getElementById('stage-1').classList.add('active');

    // Run Logs
    logs.forEach(log => {
        setTimeout(() => {
            // Add Log Line
            const p = document.createElement('div');
            p.className = `log-line log-${log.type}`;
            p.innerHTML = `<span style="opacity:0.5">[${new Date().toLocaleTimeString()}]</span> ${log.msg}`;
            logContainer.appendChild(p);
            logContainer.scrollTop = logContainer.scrollHeight;

            // Update Stages Visuals
            if (log.stage) {
                // Mark previous as done
                const prev = document.getElementById(`stage-${log.stage - 1}`);
                if (prev) {
                    prev.classList.remove('active');
                    prev.classList.add('success');
                    prev.innerHTML = prev.innerHTML.replace('fa-circle-notch', 'fa-check');
                }
                // Mark current as active
                const curr = document.getElementById(`stage-${log.stage}`);
                if (curr) curr.classList.add('active');
            }
            
            // Final Success State
            if (log.msg.includes("SUCCESSFUL")) {
                const last = document.getElementById('stage-4');
                last.classList.remove('active');
                last.classList.add('success');
                last.innerHTML = last.innerHTML.replace('fa-circle-notch', 'fa-check');
            }

        }, log.delay);
    });
}

function closePipeline() {
    document.getElementById('pipeline-overlay').classList.add('hidden');
}

/* --- COMMAND PALETTE LOGIC --- */
const palette = document.getElementById('cmd-palette');
const cmdInput = document.getElementById('cmd-input');
const cmdResults = document.getElementById('cmd-results');

const commands = [
    { title: "Home", icon: "home", action: () => window.location.href = "index.html" },
    { title: "View Resume", icon: "file-pdf", action: () => window.open("joseph_sikuku_resume.pdf", "_blank") },
    { title: "DevOps Case Study", icon: "server", action: () => window.location.href = "portfolio-showcase.html" },
    { title: "Read Blog", icon: "rss", action: () => window.location.href = "blog.html" },
    { title: "Contact Me", icon: "envelope", action: () => window.location.href = "index.html#contact" },
    { title: "Toggle Theme", icon: "adjust", action: () => document.getElementById('theme-toggle').click() }
];

function togglePalette() {
    palette.classList.toggle('hidden');
    if(!palette.classList.contains('hidden')) {
        cmdInput.value = '';
        renderCommands(commands);
        cmdInput.focus();
    }
}

function renderCommands(list) {
    cmdResults.innerHTML = '';
    list.forEach((cmd, index) => {
        const div = document.createElement('div');
        div.className = `cmd-item ${index === 0 ? 'selected' : ''}`;
        div.innerHTML = `<span><i class="fas fa-${cmd.icon}"></i> ${cmd.title}</span> <i class="fas fa-chevron-right" style="font-size:0.8rem;"></i>`;
        div.onclick = () => {
            cmd.action();
            togglePalette();
        };
        cmdResults.appendChild(div);
    });
}

// Open on Ctrl+K or Cmd+K
document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        togglePalette();
    }
    // Close on Escape
    if (e.key === 'Escape' && !palette.classList.contains('hidden')) togglePalette();
});

// Filter Logic
cmdInput.addEventListener('input', (e) => {
    const term = e.target.value.toLowerCase();
    const filtered = commands.filter(c => c.title.toLowerCase().includes(term));
    renderCommands(filtered);
});