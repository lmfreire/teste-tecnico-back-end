import "./App.css";
import { useState } from "react";
import axios from "axios";

function App() {
  const [dataArr, setDataArr] = useState([]);
  const [returnTrue, setReturnTrue] = useState(false);
  const handleUploadFile = (e) => {
    addNewCard(e.target.files[0]);
  };

  const addNewCard = async (dataFile) => {
    const data = new FormData();
    data.append("card", dataFile);

    axios
      .post("http://127.0.0.1:8000/upload/", data)
      .then(function (response) {
        console.log(response.data);
        setDataArr(response.data);
        setReturnTrue(true);
      })
      .catch(function (error) {
        console.error(error);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="Form-header">
          <label className="form-label">Escolha seu arquivo</label>
          <input
            type="file"
            onChange={handleUploadFile}
            accept="application/txt"
          />
          {returnTrue &&
            dataArr?.map((elem, index) => (
              <div>
                <p>Nome da Loja: {elem.nome_loja}</p>
                <p>Saldo total: {elem.valor_total}</p>
              </div>
            ))}
        </div>
      </header>
    </div>
  );
}

export default App;
