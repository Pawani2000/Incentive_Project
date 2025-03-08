// src/App.jsx
import { useState } from "react";
import SiaSoTypeList from "./components/SiaSoTypeList";
import SiaSoTypeForm from "./components/SiaSoTypeForm";
import "./App.css";

function App() {
  const [refresh, setRefresh] = useState(false);

  const handleAdd = () => {
    setRefresh(!refresh);
  };

  const handleDelete = () => {
    setRefresh(!refresh);
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold text-center mb-6">SIA Frontend</h1>
      <SiaSoTypeForm onAdd={handleAdd} />
      <SiaSoTypeList onDelete={handleDelete} />
    </div>
  );
}

export default App;