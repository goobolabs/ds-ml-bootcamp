import { useEffect, useState } from "react";
import { AlertCircle, ArrowRight, CheckCircle2, Cpu, LoaderCircle, Sparkles } from "lucide-react";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000";
const initialForm = { model_id: "random_forest", Capacity: "577", Occupancy: "150", month: "Oct", day: "Tue", WorkingDay: "Yes", hour: "9", period: "AM" };
const fallbackModels = [
  { id: "linear_regression", name: "Linear Regression" }, { id: "decision_tree", name: "Decision Tree" },
  { id: "random_forest", name: "Random Forest" }, { id: "gradient_boosting", name: "Gradient Boosting" },
  { id: "svr", name: "Support Vector Regression" },
];

const occupancyTone = (prediction = "") => {
  if (prediction.includes("0 - 25")) return "low";
  if (prediction.includes("25 - 50")) return "moderate";
  if (prediction.includes("50 - 75")) return "busy";
  return "high";
};

export default function PredictionForm() {
  const [form, setForm] = useState(initialForm);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [models, setModels] = useState(fallbackModels);
  useEffect(() => {
    fetch(`${API_URL}/api/models`).then((response) => response.ok ? response.json() : Promise.reject()).then((data) => {
      if (data.models?.length) setModels(data.models);
    }).catch(() => {});
  }, []);

  const handleChange = (event) => setForm((current) => ({ ...current, [event.target.name]: event.target.value }));
  async function handleSubmit(event) {
    event.preventDefault(); setLoading(true); setError(""); setResult(null);
    try {
      const response = await fetch(`${API_URL}/api/predict`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(form) });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || "Prediction request failed.");
      setResult(data);
    } catch (err) { setError(err.message || "Unable to reach the prediction service."); }
    finally { setLoading(false); }
  }
  const tone = occupancyTone(result?.prediction);
  const activeModel = models.find((model) => model.id === form.model_id)?.name || "Random Forest";
  return <div className="prediction-tool">
    <form className="prediction-form" onSubmit={handleSubmit}>
      <details className="model-picker full"><summary><Cpu size={13} /> Using {activeModel}<span>Change model</span></summary><label className="model-select"><span>Prediction model</span><select name="model_id" value={form.model_id} onChange={handleChange}>{models.map((model) => <option key={model.id} value={model.id}>{model.name}</option>)}</select></label></details>
      <label>Total parking spaces<input type="number" min="1" name="Capacity" value={form.Capacity} onChange={handleChange} required /></label>
      <label>Currently occupied spaces<input type="number" min="0" name="Occupancy" value={form.Occupancy} onChange={handleChange} required /></label>
      <label>Month<select name="month" value={form.month} onChange={handleChange}>{["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].map((value) => <option key={value}>{value}</option>)}</select></label>
      <label>Day<select name="day" value={form.day} onChange={handleChange}>{["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].map((value) => <option key={value}>{value}</option>)}</select></label>
      <label>Working day<select name="WorkingDay" value={form.WorkingDay} onChange={handleChange}><option>Yes</option><option>No</option></select></label>
      <label>Hour<input type="number" min="0" max="23" name="hour" value={form.hour} onChange={handleChange} required /></label>
      <label>Period<select name="period" value={form.period} onChange={handleChange}><option>AM</option><option>PM</option></select></label>
      <button className="submit-button full" disabled={loading}>{loading ? <><LoaderCircle className="spinner" size={18} /> Making prediction...</> : <>Predict occupancy <ArrowRight size={18} /></>}</button>
    </form>
    <aside className="result-card" aria-live="polite">
      {!result && !error && <><span className="result-icon"><Sparkles size={24} /></span><h3>Your result will appear here</h3><p>Complete the form to see the predicted parking occupancy range.</p><div className="result-legend"><span><i className="legend-low" /> Low</span><span><i className="legend-mid" /> Moderate</span><span><i className="legend-high" /> Busy</span></div></>}
      {error && <div className="error"><AlertCircle size={22} /><div><strong>Could not make a prediction</strong><span>{error}</span></div></div>}
      {result && <div className={`success ${tone}`}><span className="result-icon"><CheckCircle2 size={24} /></span><span className="result-label">Expected occupancy</span><strong>{result.prediction}</strong><p>{result.message}</p><div className="confidence"><span>{result.model.name} test accuracy</span><b>{(result.model.category_accuracy * 100).toFixed(1)}%</b></div><small className="real-prediction">Live result from your selected saved model</small></div>}
    </aside>
  </div>;
}
