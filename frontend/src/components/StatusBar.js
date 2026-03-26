import { useState, useEffect } from 'react';

function StatusBar() {
  const [status, setStatus] = useState('conectando...');

  useEffect(() => {
    fetch('http://localhost:8000/status')
      .then(response => response.json())
      .then(data => setStatus(data.status))
      .catch(() => setStatus('offline'));
  }, []);

  return (
    <div className="status-bar">
      <div className="status-dot" style={{ background: status === 'online' ? '#68D391' : '#FC8181' }} />
      <span>Backend: {status}</span>
    </div>
  );
}

export default StatusBar;