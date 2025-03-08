// src/components/SiaSoTypeList.jsx
import { useEffect, useState } from "react";
import axios from "axios";

const SiaSoTypeList = ({ onDelete }) => {
  const [siaSoTypes, setSiaSoTypes] = useState([]);

  useEffect(() => {
    const fetchSiaSoTypes = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/sia-so-types/");
        setSiaSoTypes(response.data);
      } catch (error) {
        console.error("Error fetching sia-so-types:", error);
      }
    };
    fetchSiaSoTypes();
  }, []);

  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/api/sia-so-types/${id}/`);
      setSiaSoTypes(siaSoTypes.filter((item) => item.id !== id));
      if (onDelete) onDelete();
    } catch (error) {
      console.error("Error deleting sia-so-type:", error);
    }
  };

  return (
    <div className="mt-6">
      <h2 className="text-2xl font-bold mb-4">SiaSoTypes List</h2>
      {siaSoTypes.length === 0 ? (
        <p>No records found.</p>
      ) : (
        <table className="min-w-full bg-white border border-gray-300">
          <thead>
            <tr>
              <th className="py-2 px-4 border-b">Product</th>
              <th className="py-2 px-4 border-b">Sales Type</th>
              <th className="py-2 px-4 border-b">Service Type</th>
              <th className="py-2 px-4 border-b">Order Type</th>
              <th className="py-2 px-4 border-b">Slab Eligibility</th>
              <th className="py-2 px-4 border-b">PCR Eligibility</th>
              <th className="py-2 px-4 border-b">Created Date</th>
              <th className="py-2 px-4 border-b">Created User</th>
              <th className="py-2 px-4 border-b">Status</th>
              <th className="py-2 px-4 border-b">Actions</th>
            </tr>
          </thead>
          <tbody>
            {siaSoTypes.map((item) => (
              <tr key={item.id}>
                <td className="py-2 px-4 border-b">{item.product}</td>
                <td className="py-2 px-4 border-b">{item.sales_type}</td>
                <td className="py-2 px-4 border-b">{item.service_type}</td>
                <td className="py-2 px-4 border-b">{item.order_type}</td>
                <td className="py-2 px-4 border-b">{item.slab_eligibility ? "Yes" : "No"}</td>
                <td className="py-2 px-4 border-b">{item.pcr_eligibility ? "Yes" : "No"}</td>
                <td className="py-2 px-4 border-b">{item.created_date}</td>
                <td className="py-2 px-4 border-b">{item.created_user}</td>
                <td className="py-2 px-4 border-b">{item.status}</td>
                <td className="py-2 px-4 border-b">
                  <button
                    onClick={() => handleDelete(item.id)}
                    className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default SiaSoTypeList;