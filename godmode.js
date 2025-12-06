/* --- GOD MODE: DEVOPS TERMINAL & MONITORING --- */

document.addEventListener('DOMContentLoaded', () => {
    injectTerminal();
    injectStatusBar();
    initTerminalLogic();
    initStatusLogic();
});

/* 1. INJECT HTML STRUCTURES */
function injectTerminal() {
    const termHTML = `
        <div id="terminal-overlay" class="hidden">
            <div class="terminal-window">
                <div class="term-header">
                    <div class="term-buttons">
                        <span class="close-btn" onclick="toggleTerminal()"></span>
                        <span class="min-btn"></span>
                        <span class="max-btn"></span>
                    </div>
                    <div class="term-title">sikuku@server:~/portfolio</div>
                </div>
                <div class="term-body" id="term-body">
                    <div class="term-output">
                        <p>Welcome to SikukuOS v1.0.0 LTS</p>
                        <p>Type <span class="cmd-highlight">'help'</span> to see available commands.</p>
                        <br>
                    </div>
                    <div class="input-line">
                        <span class="prompt">sikuku@root:~$</span>
                        <input type="text" id="term-input" autocomplete="off" spellcheck="false">
                    </div>
                </div>
            </div>
        </div>
        
        <button id="term-toggle-btn" onclick="toggleTerminal()" title="Open Terminal">
            <i class="fas fa-terminal"></i>
        </button>
    `;
    document.body.insertAdjacentHTML('beforeend', termHTML);
}

function injectStatusBar() {
    const statusHTML = `
        <div id="system-status-bar">
            <div class="status-item"><i class="fas fa-circle status-dot pulse"></i> SYSTEM ONLINE</div>
            <div class="status-item"><i class="fas fa-server"></i> UPTIME: <span id="uptime">00:00:00</span></div>
            <div class="status-item"><i class="fas fa-network-wired"></i> LATENCY: <span id="latency">--ms</span></div>
            <div class="status-item mobile-hide"><i class="fas fa-memory"></i> MEM: <span id="memory">--</span></div>
            <div class="status-item mobile-hide"><i class="fas fa-globe"></i> LOC: Nairobi, KE</div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', statusHTML);
}

/* 2. TERMINAL LOGIC */
function toggleTerminal() {
    const term = document.getElementById('terminal-overlay');
    const input = document.getElementById('term-input');
    term.classList.toggle('hidden');
    if (!term.classList.contains('hidden')) {
        input.focus();
    }
}

function initTerminalLogic() {
    const input = document.getElementById('term-input');
    const output = document.querySelector('.term-output');

    // Focus input when clicking anywhere in terminal
    document.querySelector('.term-body').addEventListener('click', () => input.focus());

    input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            const command = this.value.trim().toLowerCase();
            const originalCmd = this.value; // Keep original casing for display
            
            // Add command to output
            output.innerHTML += `<div><span class="prompt">sikuku@root:~$</span> ${originalCmd}</div>`;
            
            // Process Command
            processCommand(command, output);
            
            // Reset input and scroll to bottom
            this.value = '';
            const body = document.getElementById('term-body');
            body.scrollTop = body.scrollHeight;
        }
    });

    // Keyboard Shortcut: Ctrl + Backtick (`)
    document.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === '`') toggleTerminal();
    });
}

function processCommand(cmd, output) {
    let response = '';
    
    switch(cmd) {
        case 'help':
            response = `
                <div class="grid-help">
                    <span>help</span>    <span>Show this message</span>
                    <span>whoami</span>  <span>Display profile summary</span>
                    <span>projects</span><span>List latest projects</span>
                    <span>socials</span> <span>List contact links</span>
                    <span>clear</span>   <span>Clear terminal screen</span>
                    <span>date</span>    <span>Show current server time</span>
                    <span>exit</span>    <span>Close terminal</span>
                </div>`;
            break;
        case 'whoami':
            response = "Sikuku Joseph. 4+ Yrs Exp. Network Specialist & DevOps Engineer. Based in Kenya.";
            break;
        case 'projects':
            response = "1. DevOps Pipeline (CI/CD)\n2. Enterprise Network Sim (Cisco)\n3. AI Automation (Python)\n<br>Type 'open 1' to view project details.";
            break;
        case 'socials':
            response = "GitHub: github.com/Cjkreates\nLinkedIn: linkedin.com/in/joseph-sikuku\nEmail: josesikuku17@gmail.com";
            break;
        case 'clear':
            output.innerHTML = '';
            return;
        case 'date':
            response = new Date().toString();
            break;
        case 'sudo':
            response = "User is not in the sudoers file. This incident will be reported.";
            break;
        case 'exit':
            toggleTerminal();
            return;
        default:
            if (cmd.startsWith('open ')) {
                response = "Opening project...";
                window.location.href = "projects.html";
            } else if (cmd !== '') {
                response = `Command not found: ${cmd}. Type 'help' for list.`;
            }
    }
    
    if (response) {
        output.innerHTML += `<div class="term-response">${response.replace(/\n/g, '<br>')}</div><br>`;
    }
}

/* 3. SYSTEM STATUS LOGIC */
function initStatusLogic() {
    // Uptime Counter
    let seconds = 0;
    setInterval(() => {
        seconds++;
        const h = Math.floor(seconds / 3600).toString().padStart(2, '0');
        const m = Math.floor((seconds % 3600) / 60).toString().padStart(2, '0');
        const s = (seconds % 60).toString().padStart(2, '0');
        document.getElementById('uptime').textContent = `${h}:${m}:${s}`;
    }, 1000);

    // Simulated Latency (Ping)
    setInterval(() => {
        const ping = Math.floor(Math.random() * 40) + 10;
        document.getElementById('latency').textContent = `${ping}ms`;
    }, 2000);

    // Simulated Memory
    if(window.performance && window.performance.memory) {
        const mem = Math.round(window.performance.memory.usedJSHeapSize / 1024 / 1024);
        document.getElementById('memory').textContent = `${mem}MB`;
    } else {
        document.getElementById('memory').textContent = "128MB"; // Fallback
    }
}