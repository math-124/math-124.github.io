---
layout: page
title: 👩‍🏫 Staff
description: A listing of the Math 124 course staff.
nav_order: 6
---

# 👩‍🏫 Staff

{% assign course_staff = site.staffers | sort: "staff_order" %}
{% for staffer in course_staff %}
{{ staffer }}
{% endfor %}

---

### Acknowledgements

This is a brand-new course, and many people had a hand in developing it over Summer 2026. Special thanks to:

- Undergraduate assistants Sarah Shapin and Malik Alabbas
- Foundational Course Initiative consultants Blair Beuche and Sewwandi Abeywardana