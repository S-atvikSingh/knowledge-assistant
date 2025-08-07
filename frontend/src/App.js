import './App.css';
import UploadBox from './components/UploadBox';
import ChatBox from './components/ChatBox';

function App() {
  return (
    <div className="App">
      <h1>Knowledge Assistant</h1>
      <UploadBox />
      <ChatBox />
    </div>
  );
}

export default App;
