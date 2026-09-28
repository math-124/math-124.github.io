---
layout: page
title: 🏡 Home
description: Information about Math 124 in Fall 2026 at the University of Michigan.
nav_order: 1
---

# Vectors, Matrices, and Applications 🧮
{: .no_toc }
{: .mb-2 }
Math 124, Fall 2026 at the <b><span style="background-color: #FFCB05; color: #00274C">University of Michigan</span></b>
{: .no_toc }
{: .fs-6 .fw-300 .mb-2 }
**Lectures**: Tuesday and Thursdays, 2:30-4PM, G127 Angell Hall • **Labs**: Various [times](calendar) on Wednesday

{: .green }
> **Midterm 1 is on Monday, October 5th from 7-9PM in 1360 East Hall. See all relevant logistics [here](https://edstem.org/us/courses/103314/discussion/8322098).**
>
> Additionally, Quiz 2 has been moved to October 21-23.

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
    if (!start || !end || !header || !header.id) return null;

    /* Module dates list class meetings, but a course week runs Monday through Sunday. */
    start.setDate(start.getDate() - ((start.getDay() + 6) % 7));
    end.setDate(end.getDate() + ((7 - end.getDay()) % 7));
    return { start, end, header, moduleEl };
  }).filter(Boolean).sort((a, b) => a.start - b.start);

  if (!moduleData.length) return;
  const date = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'America/Detroit', year: 'numeric', month: '2-digit', day: '2-digit'
  }).format(new Date());
  const today = parseDate(date);
  let target = moduleData.find((module) => today >= module.start && today <= module.end);
  if (target) {
    target.moduleEl.classList.add('module-current');
    target.moduleEl.setAttribute('aria-current', 'true');
  }
  if (!target) target = today < moduleData[0].start ? moduleData[0] : moduleData[moduleData.length - 1];
  jumpLink.setAttribute('href', '#' + target.header.id);
})();
</script>
