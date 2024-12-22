import React, { useState } from 'react';
import './App.css';

function App() {
  const [amount, setAmount] = useState('');
  const [fromCurrency, setFromCurrency] = useState('USD');
  const [toCurrency, setToCurrency] = useState('EUR');
  const [result, setResult] = useState('');

  const currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'INR'];

  const handleConvert = () => {
    // For demo purposes, using fixed conversion rates
    const rates = {
      USD: 1,
      EUR: 0.91,
      GBP: 0.79,
      JPY: 142.95,
      AUD: 1.48,
      CAD: 1.34,
      CHF: 0.86,
      CNY: 7.13,
      INR: 83.28
    };

    const convertedAmount = (amount * rates[toCurrency] / rates[fromCurrency]).toFixed(2);
    setResult(convertedAmount);
  };

  return (
    <div className="app">
      <div className="converter-container">
        <h1>Currency Converter</h1>
        <div className="input-group">
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="Enter amount"
          />
          <select
            value={fromCurrency}
            onChange={(e) => setFromCurrency(e.target.value)}
          >
            {currencies.map(currency => (
              <option key={currency} value={currency}>{currency}</option>
            ))}
          </select>
          <span>to</span>
          <select
            value={toCurrency}
            onChange={(e) => setToCurrency(e.target.value)}
          >
            {currencies.map(currency => (
              <option key={currency} value={currency}>{currency}</option>
            ))}
          </select>
        </div>
        <button onClick={handleConvert}>Convert</button>
        {result && (
          <div className="result">
            {amount} {fromCurrency} = {result} {toCurrency}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
