import {
  ArrowRight,
  BarChart3,
  BrainCircuit,
  CarFront,
  CheckCircle2,
  MapPin,
  Menu,
  Moon,
  Sparkles,
  Sun,
  X,
} from "lucide-react";
import { useState } from "react";
import PredictionForm from "./components/PredictionForm";

export default function App() {
  const [menuOpen, setMenuOpen] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const closeMenu = () => setMenuOpen(false);

  return (
    <div className={darkMode ? "app-shell theme-dark" : "app-shell"}>
      <header className="navbar">
        <a className="brand" href="#home" onClick={closeMenu} aria-label="ParkSmart home">
          <span className="brand-mark"><CarFront size={22} /></span>
          <span>Park<span>Sense</span></span>
        </a>
        <button className="menu-toggle" onClick={() => setMenuOpen(!menuOpen)} aria-label="Toggle navigation" aria-expanded={menuOpen}>
          {menuOpen ? <X size={22} /> : <Menu size={22} />}
        </button>
        <nav className={menuOpen ? "nav-links open" : "nav-links"}>
          <a href="#home" onClick={closeMenu}>Home</a>
          <a href="#predict" onClick={closeMenu}>Predict</a>
          <a href="#about" onClick={closeMenu}>About</a>
          <a className="nav-cta" href="#predict" onClick={closeMenu}>Start predicting <ArrowRight size={16} /></a>
        </nav>
        <button className="theme-toggle" type="button" onClick={() => setDarkMode((current) => !current)} aria-label={darkMode ? "Use light mode" : "Use dark mode"} title={darkMode ? "Use light mode" : "Use dark mode"}>
          {darkMode ? <Sun size={18} /> : <Moon size={18} />}
        </button>
      </header>

      <main>
        <section id="home" className="hero">
          <div className="hero-copy">
            <div className="hero-pill"><Sparkles size={14} /> Parking planning, made simpler</div>
            <h1>Know before you go. <em>Park with ease.</em></h1>
            <p>ParkSense turns historical parking information into a clear occupancy estimate, so planning your visit feels a little less uncertain.</p>
            <div className="hero-actions">
              <a className="button button-primary" href="#predict">Predict occupancy <ArrowRight size={18} /></a>
              <a className="text-link" href="#about">How it works <ArrowRight size={16} /></a>
            </div>
            <div className="hero-trust"><CheckCircle2 size={17} /> Built from 35,000+ historic parking observations</div>
          </div>

          <div className="hero-visual" aria-label="Illustration of a parking occupancy report">
            <div className="glow glow-one" /><div className="glow glow-two" />
            <div className="map-card">
              <div className="map-head"><span>Parking occupancy estimate</span><span className="live-dot">Ready to plan</span></div>
              <div className="map-lines"><i /><i /><i /><i /></div>
              <div className="route route-a" /><div className="route route-b" />
              <span className="pin pin-one"><MapPin size={16} /></span><span className="pin pin-two"><MapPin size={16} /></span>
              <div className="availability-card"><span className="availability-icon"><CarFront size={20} /></span><div><small>Expected occupancy</small><strong>25 – 50%</strong></div><span className="trend">Good</span></div>
            </div>
            <div className="floating-stat"><span className="stat-icon"><BarChart3 size={19} /></span><div><small>Prediction confidence</small><strong>High accuracy</strong></div></div>
          </div>
        </section>

        <section id="predict" className="prediction-section">
          <div className="section-wrap prediction-layout prediction-centered">
            <div className="section-intro prediction-intro"><span className="eyebrow">PARKING ESTIMATE</span><h2>Plan your parking with confidence.</h2><p>Choose a model and enter a few details to see the expected occupancy range.</p></div>
            <PredictionForm />
            <div className="prediction-disclaimer"><BrainCircuit size={18} /><span>Predictions use historical data and are estimates, not live space-by-space availability.</span></div>
          </div>
        </section>

        <section id="about" className="about-section section-wrap">
          <div className="about-visual"><div className="about-circle"><BrainCircuit size={51} /><strong>ML</strong></div><div className="data-chip chip-a">Time &amp; day</div><div className="data-chip chip-b">Facility capacity</div><div className="data-chip chip-c">Historical use</div></div>
          <div className="about-copy"><span className="eyebrow">ABOUT THE PROJECT</span><h2>From parking data to useful decisions.</h2><p>This application is a supervised machine learning project that learns patterns between facility details, time information, and occupancy levels.</p><p>It was designed as a simple bridge between a trained prediction model and the people who need to understand parking demand.</p><a className="text-link" href="#predict">Try the prediction tool <ArrowRight size={16} /></a></div>
        </section>

      </main>

      <footer><a className="brand" href="#home"><span className="brand-mark"><CarFront size={20} /></span><span>Park<span>Sense</span></span></a><p>Parking Occupancy Prediction Web Application</p><p>Built by Maryamo Hersi Hassan</p></footer>
    </div>
  );
}
