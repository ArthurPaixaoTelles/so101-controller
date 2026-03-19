import { useState, useEffect } from 'react';

function StatusBar(){
    const [status, setStatus] = useState('conectando agora ...');

    useEffect(() => {
        fetch('http://localhost:8000/status')
        .then(response => response.json())
        .then(data => setStatus(data.status))
        .catch(() => setStatus('offline'));
    }, []);

    return(
        <p>Backend: {status}</p>
    );
}

export default StatusBar;

