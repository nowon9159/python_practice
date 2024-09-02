import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';


function App() {
  // 상태(state) 설정
  const [message, setMessage] = useState(''); // 메시지를 저장할 상태

  // 컴포넌트가 마운트될 때 한 번 실행되는 useEffect 훅
  useEffect(() => {
    // API 호출
    fetch('http://127.0.0.1:8000/hello') // FastAPI 엔드포인트
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json(); // 응답을 JSON 형식으로 변환
      })
      .then((data) => setMessage(data.message)) // message 상태에 설정
      .catch((error) => console.error('Error fetching data:', error));
  }, []); // 빈 배열을 전달하여 컴포넌트가 처음 렌더링될 때만 실행

  return (
    <div>
      <h1>Message from FastAPI:</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
