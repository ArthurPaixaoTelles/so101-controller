import StatusBar from './components/StatusBar';
import JointControl from './components/JointControl';
import './App.css';
function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>SO-101 CONTROLADOR</h1>
        <p> Controlador</p> </header>
        <JointControl/>
        <StatusBar/>

    </div>
  );
}

export default App;
