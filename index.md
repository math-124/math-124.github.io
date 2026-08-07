---
layout: page
title: 🏡 Home
description: Information about MATH 124 in Fall 2026 at the University of Michigan.
nav_order: 1
---

{: .red }
> **Course website is under development.**

# Vectors, Matrices, and Applications
{: .no_toc }
{: .mb-2 }
MATH 124, Fall 2026 at the <b><span style="background-color: #FFCB05; color: #00274C">University of Michigan</span></b>
{: .no_toc }
{: .fs-6 .fw-300 .mb-2 }

**Lectures: Tuesdays and Thursdays, 2:30–4:00 PM in G127 Angell Hall**
{: .fs-5 .fw-500 .mb-4 }

<a class="btn" style="background-color: #00274C; color: white;" data-current-week-link href="#{{ site.modules.first.title | slugify }}">Jump to the current week</a>

{% for module in site.modules %}
{{ module }}
{% endfor %}

<script>
(function() {
  const jumpLink = document.querySelector('[data-current-week-link]');
  const modules = Array.from(document.querySelectorAll('.module'));
  if (!jumpLink || !modules.length) return;

  const parseDate = (value) => {
    const parsed = value ? new Date(value + 'T00:00:00') : null;
    return parsed && !Number.isNaN(parsed.getTime()) ? parsed : null;
  };

  const moduleData = modules.map((moduleEl) => {
    const start = parseDate(moduleEl.dataset.weekStart);
    const end = parseDate(moduleEl.dataset.weekEnd);
    const header = moduleEl.querySelector('.module-header');
    return start && end && header && header.id ? { start, end, header } : null;
  }).filter(Boolean).sort((a, b) => a.start - b.start);

  if (!moduleData.length) return;
  const now = new Date();
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  let target = moduleData.find((module) => today >= module.start && today <= module.end);
  if (!target) target = today < moduleData[0].start ? moduleData[0] : moduleData[moduleData.length - 1];
  jumpLink.setAttribute('href', '#' + target.header.id);
})();
</script>
