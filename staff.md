---
layout: page
title: 👩‍🏫 Staff
description: A listing of the Math 124 course staff.
nav_order: 4
---

# 👩‍🏫 Staff

{% assign course_staff = site.staffers | sort: "staff_order" %}
{% for staffer in course_staff %}
{{ staffer }}
{% endfor %}
