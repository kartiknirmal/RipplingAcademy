import './App.css';
import CartPage from './CartPage';
import GLobalContectWrapper from './GlobalContextWrapper';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Home';

function App() {
  return (
    <GLobalContectWrapper>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/cart/" element={<CartPage />} />

        </Routes>
      </BrowserRouter>
    </GLobalContectWrapper>
  );
}

export default App;
