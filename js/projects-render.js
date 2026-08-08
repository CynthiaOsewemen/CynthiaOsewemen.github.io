(function () {
  const state = { category: "data", query: "", sort: "featured" };

  function toolsMatch(items, q) {
    return items.some(t => t.toLowerCase().includes(q));
  }

  function renderDataCard(p) {
    const imgsHtml = p.images && p.images.length
      ? `<div class="pcard-imgs" style="--imgcols:${Math.min(p.images.length, 2)}">${p.images.map(src => `<img src="${src}" alt="${p.title} dashboard" loading="lazy">`).join("")}</div>`
      : `<div class="pcard-noimg">${p.title}</div>`;
    const toolsHtml = `<div class="pcard-tools">${p.tools.map(t => `<span>${t}</span>`).join("")}</div>`;
    const whatIDidHtml = p.whatIDid
      ? `<div class="pcard-block"><h6>What I Did</h6><ul>${p.whatIDid.map(i => `<li>${i}</li>`).join("")}</ul></div>`
      : "";
    const resultsHtml = p.resultsList
      ? `<div class="pcard-block"><h6>Key Findings</h6><ul>${p.resultsList.map(i => `<li>${i}</li>`).join("")}</ul></div>`
      : "";
    const statsHtml = p.stats
      ? `<div class="pcard-stats">${p.stats.map(s => `<div class="stat-pill"><b>${s.value}</b><small>${s.label}</small></div>`).join("")}</div>`
      : "";
    return `<article class="pcard${p.featured ? " featured" : ""}">
      ${imgsHtml}
      <div class="pcard-body">
        ${toolsHtml}
        <h3>${p.title}</h3>
        <p class="pcard-sub">${p.subtitle}</p>
        <div class="pcard-block"><h6>Problem</h6><p>${p.problem}</p></div>
        ${whatIDidHtml}
        ${resultsHtml}
        ${statsHtml}
        <a href="projects/${p.id}.html" class="pcard-detail-link">View Full Case Study</a>
      </div>
    </article>`;
  }

  function renderAutomationCard(p) {
    const imgHtml = p.image
      ? `<div class="pcard-imgs" style="--imgcols:1"><img src="${p.image}" alt="${p.title} screenshot" loading="lazy"></div>`
      : `<div class="pcard-noimg">${p.tool}</div>`;
    return `<article class="pcard">
      ${imgHtml}
      <div class="pcard-body">
        <div class="pcard-tools"><span>${p.tool}</span></div>
        <h3>${p.title}</h3>
        <div class="pcard-block"><p>${p.description}</p></div>
        <a href="projects/${p.id}.html" class="pcard-detail-link">View Full Case Study</a>
      </div>
    </article>`;
  }

  function sortItems(items, sortKey, isAutomation) {
    const arr = [...items];
    if (sortKey === "az") {
      arr.sort((a, b) => a.title.localeCompare(b.title));
    } else if (sortKey === "newest") {
      arr.sort((a, b) => (b.date || "").localeCompare(a.date || ""));
    } else if (sortKey === "tool") {
      arr.sort((a, b) => {
        const ta = isAutomation ? a.tool : (a.tools[0] || "");
        const tb = isAutomation ? b.tool : (b.tools[0] || "");
        return ta.localeCompare(tb);
      });
    } else {
      if (!isAutomation) arr.sort((a, b) => (b.featured === true) - (a.featured === true));
    }
    return arr;
  }

  function render() {
    const grid = document.getElementById("projectsGrid");
    const countEl = document.getElementById("resultsCount");
    const q = state.query.trim().toLowerCase();
    const isAutomation = state.category === "automation";
    const source = isAutomation ? AUTOMATION_PROJECTS : DATA_PROJECTS;

    let filtered = source.filter(p => {
      if (!q) return true;
      const inTitle = p.title.toLowerCase().includes(q);
      const inTools = isAutomation ? p.tool.toLowerCase().includes(q) : toolsMatch(p.tools, q);
      const inDesc = (isAutomation ? p.description : p.problem).toLowerCase().includes(q);
      return inTitle || inTools || inDesc;
    });

    filtered = sortItems(filtered, state.sort, isAutomation);

    countEl.textContent = q
      ? `Showing results for "${state.query}"`
      : (isAutomation ? "Automation and PM Projects" : "Data Analytics Projects");

    grid.className = "pcard-grid";
    grid.innerHTML = filtered.length
      ? filtered.map(isAutomation ? renderAutomationCard : renderDataCard).join("")
      : `<div class="no-results">No projects match your search. Try a different keyword.</div>`;
  }

  document.querySelectorAll(".category-tabs button").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".category-tabs button").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      state.category = btn.dataset.category;
      const sortSelect = document.getElementById("sortSelect");
      const newestOpt = sortSelect.querySelector('option[value="newest"]');
      render();
    });
  });

  document.getElementById("searchInput").addEventListener("input", (e) => {
    state.query = e.target.value;
    render();
  });

  document.getElementById("sortSelect").addEventListener("change", (e) => {
    state.sort = e.target.value;
    render();
  });

  render();
})();
