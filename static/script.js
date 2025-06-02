particlesJS("particles-js", {
  particles: {
    number: { value: 80, density: { enable: true, value_area: 800 } },
    color: { value: "#8b5cf6" },
    shape: { type: "circle" },
    opacity: { value: 0.5 },
    size: { value: 3 },
    line_linked: { enable: true, distance: 150, color: "#8b5cf6", opacity: 0.4, width: 1 },
    move: { enable: true, speed: 2 }
  },
  interactivity: {
    detect_on: "canvas",
    events: {
      onhover: { enable: true, mode: "repulse" },
      onclick: { enable: true, mode: "push" },
    },
    modes: {
      repulse: { distance: 100 },
      push: { particles_nb: 4 },
    },
  },
  retina_detect: true,
});


function clearHighlights() {
  const lineHighlight = document.getElementById('line-highlight');
  if (lineHighlight) {
    lineHighlight.innerHTML = '';
  }
}

function escanear_lexico() {
  clearHighlights(); 
  const code = document.getElementById('codigo').value;
  fetch('/lexico', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code: code })
  })
  .then(res => res.json())
  .then(data => document.getElementById('resultado').textContent = data.resultado)
  .catch(err => document.getElementById('resultado').textContent = 'Error: ' + err.message);
}

function analizarSintactico() {
  const code = document.getElementById('codigo').value;
  fetch('/sintaxis', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code: code })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('resultado').textContent = data.resultado;
    highlightErrors(data.resultado);
  })
  .catch(err => document.getElementById('resultado').textContent = 'Error: ' + err.message);
}

function highlightErrors(resultado) {
  const textarea = document.getElementById('codigo');
  const lineHighlight = document.getElementById('line-highlight');
  const lines = resultado.split('\n');
  const codeLines = textarea.value.split('\n');
  
  
  lineHighlight.innerHTML = '';

  

  const charWidth = 8; 
  const lineHeight = 21; 
  const paddingTop = 10; 

  
  lines.forEach((resultLine) => {
    const lineNumber = parseInt(resultLine.match(/Línea (\d+):/)?.[1] || '0');
    if (resultLine.includes('❌')) {
      const codeLine = codeLines[lineNumber - 1];
      if (!codeLine) return;

      const errorLine = document.createElement('div');
      errorLine.className = 'error-line';
      
      
      const top = ((lineNumber - 1) * lineHeight) + paddingTop + lineHeight - 4;
      errorLine.style.top = `${top}px`;

      if (resultLine.includes('lado derecho vacío')) {
        
        const equalPos = codeLine.indexOf('=');
        if (equalPos !== -1) {
          errorLine.style.left = `${(equalPos + 1) * charWidth}px`;
          errorLine.style.width = '16px'; 
        }
      } else {

        errorLine.style.left = '10px'; 
        errorLine.style.width = `${(codeLine.length * charWidth) - 10}px`;
      }

      
      errorLine.style.height = '3px !important';
      errorLine.style.backgroundColor = 'transparent';
      errorLine.style.borderBottom = '2px wavy red';

      lineHighlight.appendChild(errorLine);
    }
  });
}

function ejecutarTuring() {
  clearHighlights(); 
  const code = document.getElementById('codigo').value;
  fetch('/maquina-turing', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code: code })
  })
  .then(res => res.json())
  .then(data => document.getElementById('resultado').textContent = data.resultado)
  .catch(err => document.getElementById('resultado').textContent = 'Error: ' + err.message);
}

function limpiarResultado() {
  document.getElementById('resultado').textContent = '';
  document.getElementById('codigo').value = '';
  clearHighlights(); 
  updateLineNumbers();
}

function updateLineNumbers() {
  const textarea = document.getElementById("codigo");
  const lineCount = textarea.value.split('\n').length;
  const lineNumbersDiv = document.getElementById("line-numbers");
  const numbers = Array.from({ length: lineCount }, (_, i) => i + 1).join('\n');
  lineNumbersDiv.textContent = numbers || '1';
  clearHighlights(); 
}

function syncScroll() {
  const textarea = document.getElementById("codigo");
  const lineHighlight = document.getElementById("line-highlight");
  

  if (lineHighlight) {
    lineHighlight.style.top = `-${textarea.scrollTop}px`;
  }
}


document.addEventListener("DOMContentLoaded", () => {
  const textarea = document.getElementById("codigo");
  if (textarea) {

    textarea.addEventListener("input", () => {
      updateLineNumbers();
      clearHighlights();
    });
    textarea.addEventListener("scroll", syncScroll);
    updateLineNumbers();
  }
});
