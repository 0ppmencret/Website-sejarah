function visualSimulate(event) {
  const sim = document.getElementById('sim-content');
  if (event === 'proklamasi') {
    sim.innerHTML = '<h3>Simulasi: Proklamasi 1945</h3><p>Ir. Soekarno membacakan teks proklamasi...</p>';
  } else if (event === 'g30s') {
    sim.innerHTML = '<h3>Simulasi: G30S/PKI</h3><p>Gerakan 30 September dimulai tengah malam...</p>';
  } else {
    sim.innerHTML = '<p>Simulasi tidak ditemukan.</p>';
  }
}
