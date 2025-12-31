import './style.css'

const checkBtn = document.getElementById('check-btn');
const btnText = document.getElementById('btn-text');
const btnSpinner = document.getElementById('btn-spinner');
const metricsGrid = document.getElementById('metrics-grid');
const statusContainer = document.getElementById('status-container');
const statusBadge = document.getElementById('status-badge');
const timestampEl = document.getElementById('timestamp');
const alertsSection = document.getElementById('alerts-section');
const alertsList = document.getElementById('alerts-list');
const errorMessage = document.getElementById('error-message');

const API_URL = 'http://localhost:8000/api/health';

checkBtn.addEventListener('click', async () => {
  // Reset UI
  resetUI();
  setLoading(true);

  try {
    const response = await fetch(API_URL);
    if (!response.ok) {
      throw new Error(`Server connection failed: ${response.statusText}`);
    }

    const data = await response.json();
    renderData(data);
  } catch (error) {
    showError(error.message);
  } finally {
    setLoading(false);
  }
});

function resetUI() {
  errorMessage.classList.add('hidden');
  metricsGrid.classList.add('hidden');
  statusContainer.classList.add('hidden');
  alertsSection.classList.add('hidden');
  alertsList.innerHTML = '';
}

function setLoading(isLoading) {
  checkBtn.disabled = isLoading;
  if (isLoading) {
    btnText.textContent = 'Checking...';
    btnSpinner.classList.remove('hidden');
  } else {
    btnText.textContent = 'Check System Health';
    btnSpinner.classList.add('hidden');
  }
}

function renderData(data) {
  // 1. Status
  statusContainer.classList.remove('hidden');
  const isHealthy = data.status === 'HEALTHY';

  statusBadge.textContent = data.status;
  statusBadge.className = isHealthy
    ? 'inline-block px-4 py-1 rounded-full text-sm font-bold tracking-wide uppercase bg-green-100 text-green-800'
    : 'inline-block px-4 py-1 rounded-full text-sm font-bold tracking-wide uppercase bg-red-100 text-red-800';

  timestampEl.textContent = `Last updated: ${new Date().toLocaleTimeString()}`;

  // 2. Metrics
  metricsGrid.classList.remove('hidden');
  updateMetric('cpu', data.metrics.cpu);
  updateMetric('mem', data.metrics.mem);
  updateMetric('disk', data.metrics.disk);

  // 3. Alerts
  if (data.alerts && data.alerts.length > 0) {
    alertsSection.classList.remove('hidden');
    data.alerts.forEach(alert => {
      const li = document.createElement('li');
      li.className = 'bg-red-50 text-red-700 p-3 rounded-md border border-red-100 text-sm font-medium flex items-center gap-2';
      li.innerHTML = `
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                ${alert}
            `;
      alertsList.appendChild(li);
    });
  }
}

function updateMetric(id, value) {
  const valEl = document.getElementById(`${id}-val`);
  const barEl = document.getElementById(`${id}-bar`);

  // Animate value (simple implementation)
  valEl.textContent = `${value.toFixed(1)}%`;
  barEl.style.width = `${value}%`;

  // Color coding based on value
  if (value > 90) {
    barEl.classList.remove('bg-indigo-600', 'bg-purple-600', 'bg-pink-600', 'bg-green-500', 'bg-yellow-500');
    barEl.classList.add('bg-red-600');
  }
}

function showError(msg) {
  errorMessage.textContent = msg;
  errorMessage.classList.remove('hidden');
}
