// src/components/SiaSoTypeForm.jsx
import { useState } from "react";
import axios from "axios";

const SiaSoTypeForm = ({ onAdd }) => {
  const [formData, setFormData] = useState({
    product: "",
    sales_type: "",
    service_type: "",
    order_type: "",
    slab_eligibility: false,
    pcr_eligibility: false,
    created_date: new Date().toISOString().split("T")[0], // Today’s date
    created_user: "admin",
    status: "Active",
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/api/sia-so-types/", formData);
      if (onAdd) onAdd();
      setFormData({
        product: "",
        sales_type: "",
        service_type: "",
        order_type: "",
        slab_eligibility: false,
        pcr_eligibility: false,
        created_date: new Date().toISOString().split("T")[0],
        created_user: "admin",
        status: "Active",
      });
    } catch (error) {
      console.error("Error adding sia-so-type:", error);
    }
  };

  return (
    <div className="mt-6">
      <h2 className="text-2xl font-bold mb-4">Add New SiaSoType</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium">Product</label>
          <input
            type="text"
            name="product"
            value={formData.product}
            onChange={handleChange}
            className="mt-1 p-2 border rounded w-full"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium">Sales Type</label>
          <input
            type="text"
            name="sales_type"
            value={formData.sales_type}
            onChange={handleChange}
            className="mt-1 p-2 border rounded w-full"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium">Service Type</label>
          <input
            type="text"
            name="service_type"
            value={formData.service_type}
            onChange={handleChange}
            className="mt-1 p-2 border rounded w-full"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium">Order Type</label>
          <input
            type="text"
            name="order_type"
            value={formData.order_type}
            onChange={handleChange}
            className="mt-1 p-2 border rounded w-full"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium">Slab Eligibility</label>
          <input
            type="checkbox"
            name="slab_eligibility"
            checked={formData.slab_eligibility}
            onChange={handleChange}
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium">PCR Eligibility</label>
          <input
            type="checkbox"
            name="pcr_eligibility"
            checked={formData.pcr_eligibility}
            onChange={handleChange}
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium">Created Date</label>
          <input
            type="date"
            name="created_date"
            value={formData.created_date}
            onChange={handleChange}
            className="mt-1 p-2 border rounded w-full"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium">Created User</label>
          <input
            type="text"
            name="created_user"
            value={formData.created_user}
            onChange={handleChange}
            className="mt-1 p-2 border rounded w-full"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium">Status</label>
          <select
            name="status"
            value={formData.status}
            onChange={handleChange}
            className="mt-1 p-2 border rounded w-full"
            required
          >
            <option value="Active">Active</option>
            <option value="Inactive">Inactive</option>
          </select>
        </div>
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Add SiaSoType
        </button>
      </form>
    </div>
  );
};

export default SiaSoTypeForm;