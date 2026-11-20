async function sincronizarConBackend() {
  try {
    const res = await fetch("/api/inscripciones");
    if (!res.ok) return;
    const inscripciones = await res.json();
    const tbody = document.querySelector("#coordinatorDashboard table.history tbody");
    if (tbody && inscripciones.length > 0) {
      inscripciones.forEach((item) => {
        const fila = document.createElement("tr");
        fila.innerHTML = `
          <td>${item.estudiante}</td>
          <td>${item.codigo}</td>
          <td>${item.linea_enfasis}</td>
          <td>VI</td>
          <td><span class="grade good">BD</span></td>
        `;
        tbody.appendChild(fila);
      });
    }
  } catch (err) {
    console.warn("Esperando conexión con backend:", err);
  }
}

document.addEventListener("click", async (e) => {
  const btn = e.target.closest("#studentEmphasisGrid .apply-btn");
  if (!btn) return;

  const card = btn.closest(".emphasis-card");
  const linea = card?.querySelector("h3")?.textContent?.trim() || "Línea de Énfasis";
  const estudiante = document.getElementById("studentProfileName")?.textContent?.trim() || "Estudiante";
  const carrera = document.getElementById("studentProfileCareer")?.textContent?.trim() || "Pregrado";

  try {
    await fetch("/api/inscripciones", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        estudiante: estudiante,
        codigo: carrera,
        linea_enfasis: linea
      })
    });
  } catch (err) {
    console.error("Error guardando inscripción en PostgreSQL:", err);
  }
});

document.addEventListener("DOMContentLoaded", sincronizarConBackend);
