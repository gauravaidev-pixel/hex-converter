from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# HTML, CSS, JS, aur Service Worker ek hi response mein
@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="theme-color" content="#1a1a2e">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <link rel="manifest" href="/manifest.json">
    <link rel="apple-touch-icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%231a1a2e'/%3E%3Ctext x='50' y='67' font-size='50' text-anchor='middle' fill='%23e94560'%3E🪙%3C/text%3E%3C/svg%3E">
    <title>Hex Converter - Decimal to Hexadecimal</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 30px;
            padding: 30px 25px;
            max-width: 500px;
            width: 100%;
            box-shadow: 0 25px 45px rgba(0,0,0,0.2);
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        h1 {
            text-align: center;
            color: #e94560;
            margin-bottom: 10px;
            font-size: 1.8rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        
        .subtitle {
            text-align: center;
            color: #aaa;
            margin-bottom: 30px;
            font-size: 0.9rem;
        }
        
        .input-group {
            margin-bottom: 25px;
        }
        
        label {
            display: block;
            color: #eee;
            margin-bottom: 8px;
            font-weight: 500;
        }
        
        input, select {
            width: 100%;
            padding: 15px;
            border: none;
            border-radius: 15px;
            background: rgba(0,0,0,0.3);
            color: white;
            font-size: 1.1rem;
            outline: none;
            transition: all 0.3s;
        }
        
        input:focus {
            background: rgba(0,0,0,0.5);
            box-shadow: 0 0 0 2px #e94560;
        }
        
        select {
            cursor: pointer;
        }
        
        select option {
            background: #1a1a2e;
        }
        
        button {
            width: 100%;
            padding: 15px;
            background: #e94560;
            border: none;
            border-radius: 15px;
            color: white;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s, background 0.2s;
        }
        
        button:hover {
            background: #ff6b6b;
            transform: scale(1.02);
        }
        
        button:active {
            transform: scale(0.98);
        }
        
        .result {
            margin-top: 30px;
            padding: 20px;
            background: rgba(0,0,0,0.3);
            border-radius: 20px;
            text-align: center;
        }
        
        .result-label {
            color: #aaa;
            font-size: 0.8rem;
            letter-spacing: 1px;
        }
        
        .result-value {
            font-size: 1.5rem;
            font-weight: bold;
            color: #4ecdc4;
            word-break: break-all;
            font-family: monospace;
            margin-top: 10px;
        }
        
        .history {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
        }
        
        .history h3 {
            color: #eee;
            margin-bottom: 15px;
            font-size: 1rem;
        }
        
        .history-list {
            list-style: none;
            max-height: 200px;
            overflow-y: auto;
        }
        
        .history-list li {
            background: rgba(0,0,0,0.2);
            padding: 10px;
            margin-bottom: 8px;
            border-radius: 10px;
            font-family: monospace;
            font-size: 0.85rem;
            color: #4ecdc4;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .history-list li span {
            color: #aaa;
        }
        
        .clear-history {
            background: rgba(255,255,255,0.1);
            margin-top: 10px;
            font-size: 0.8rem;
            padding: 8px;
        }
        
        .swap-btn {
            background: rgba(78,205,196,0.2);
            margin-top: 10px;
            font-size: 0.9rem;
        }
        
        footer {
            text-align: center;
            margin-top: 30px;
            color: #666;
            font-size: 0.7rem;
        }
        
        @media (max-width: 480px) {
            .container {
                padding: 20px;
            }
            h1 {
                font-size: 1.4rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>
            <span>🪙</span> Hex Converter <span>🔢</span>
        </h1>
        <div class="subtitle">Decimal ↔ Hexadecimal Converter</div>
        
        <div class="input-group">
            <label>📝 Enter Number</label>
            <input type="number" id="decimalInput" placeholder="Enter decimal number...">
        </div>
        
        <div class="input-group">
            <label>🔄 Conversion Type</label>
            <select id="conversionType">
                <option value="decToHex">Decimal → Hexadecimal</option>
                <option value="hexToDec">Hexadecimal → Decimal</option>
            </select>
        </div>
        
        <button onclick="convert()">✨ Convert Now ✨</button>
        
        <div class="result" id="resultBox" style="display: none;">
            <div class="result-label" id="resultLabel">Hexadecimal Value</div>
            <div class="result-value" id="resultValue">0x0</div>
        </div>
        
        <div class="history">
            <h3>📜 Conversion History</h3>
            <ul class="history-list" id="historyList">
                <li style="color:#666; justify-content:center;">No conversions yet</li>
            </ul>
            <button class="clear-history" onclick="clearHistory()">🗑️ Clear History</button>
        </div>
        
        <footer>
            Works offline • Install on Home Screen
        </footer>
    </div>
    
    <script>
        let history = [];
        
        function loadHistory() {
            const saved = localStorage.getItem('hexHistory');
            if(saved) {
                history = JSON.parse(saved);
                updateHistoryDisplay();
            }
        }
        
        function saveHistory() {
            localStorage.setItem('hexHistory', JSON.stringify(history.slice(0, 10)));
        }
        
        function updateHistoryDisplay() {
            const list = document.getElementById('historyList');
            if(history.length === 0) {
                list.innerHTML = '<li style="color:#666; justify-content:center;">No conversions yet</li>';
                return;
            }
            
            list.innerHTML = history.map(item => 
                `<li><span>${item.input}</span> → <strong>${item.output}</strong></li>`
            ).join('');
        }
        
        function addToHistory(input, output, type) {
            history.unshift({
                input: input,
                output: output,
                type: type,
                time: new Date().toLocaleTimeString()
            });
            if(history.length > 10) history.pop();
            saveHistory();
            updateHistoryDisplay();
        }
        
        function clearHistory() {
            history = [];
            saveHistory();
            updateHistoryDisplay();
        }
        
        function convert() {
            const input = document.getElementById('decimalInput').value;
            const type = document.getElementById('conversionType').value;
            const resultBox = document.getElementById('resultBox');
            const resultLabel = document.getElementById('resultLabel');
            const resultValue = document.getElementById('resultValue');
            
            if(!input || input === '') {
                alert('Please enter a number!');
                return;
            }
            
            if(type === 'decToHex') {
                const decimal = parseInt(input);
                if(isNaN(decimal)) {
                    alert('Please enter a valid decimal number!');
                    return;
                }
                const hex = '0x' + decimal.toString(16).toUpperCase();
                resultLabel.innerHTML = '🪙 Hexadecimal Value 🪙';
                resultValue.innerHTML = hex;
                addToHistory(input, hex, 'dec→hex');
            } 
            else {
                let hexInput = input.toString().toUpperCase();
                if(hexInput.startsWith('0X')) {
                    hexInput = hexInput.substring(2);
                }
                if(hexInput.startsWith('0x')) {
                    hexInput = hexInput.substring(2);
                }
                const decimal = parseInt(hexInput, 16);
                if(isNaN(decimal)) {
                    alert('Please enter a valid hexadecimal number! (0-9, A-F)');
                    return;
                }
                resultLabel.innerHTML = '🔢 Decimal Value 🔢';
                resultValue.innerHTML = decimal.toString();
                addToHistory(hexInput, decimal.toString(), 'hex→dec');
            }
            
            resultBox.style.display = 'block';
        }
        
        document.getElementById('decimalInput').addEventListener('keypress', function(e) {
            if(e.key === 'Enter') convert();
        });
        
        loadHistory();
        
        if('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/sw.js')
                .then(reg => console.log('SW registered:', reg))
                .catch(err => console.log('SW error:', err));
        }
        
        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
            const btn = document.createElement('button');
            btn.innerHTML = '📱 Install App';
            btn.className = 'swap-btn';
            btn.onclick = () => {
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then(() => { btn.remove(); });
            };
            document.querySelector('.history').after(btn);
        });
    </script>
</body>
</html>
    '''

@app.route('/manifest.json')
def manifest():
    return {
        "name": "Hex Converter",
        "short_name": "HexConv",
        "description": "Decimal to Hexadecimal converter for MOD makers",
        "start_url": "/",
        "display": "standalone",
        "theme_color": "#1a1a2e",
        "background_color": "#1a1a2e",
        "icons": [
            {
                "src": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%231a1a2e'/%3E%3Ctext x='50' y='67' font-size='50' text-anchor='middle' fill='%23e94560'%3E🪙%3C/text%3E%3C/svg%3E",
                "sizes": "any",
                "type": "image/svg+xml",
                "purpose": "any"
            }
        ]
    }

@app.route('/sw.js')
def service_worker():
    return '''
const CACHE_NAME = 'hex-converter-v1';
const urlsToCache = [
    '/',
    '/manifest.json'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(urlsToCache))
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => response || fetch(event.request))
    );
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cache => {
                    if(cache !== CACHE_NAME) {
                        return caches.delete(cache);
                    }
                })
            );
        })
    );
});
    ''', 200, {'Content-Type': 'application/javascript'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
