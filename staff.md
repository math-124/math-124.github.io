---
layout: page
title: 👩‍🏫 Staff
description: A listing of the MATH 124 course staff.
nav_order: 3
---

# 👩‍🏫 Staff

## Instructors

{% assign instructors = site.staffers | where: 'role', 'Instructor' | sort: 'name' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

## Graduate Student Instructor

{% assign gsis = site.staffers | where: 'role', 'GSI' %}
{% for staffer in gsis %}
{{ staffer }}
{% endfor %}

## Instructional Assistant

{% assign ias = site.staffers | where: 'role', 'IA' %}
{% for staffer in ias %}
{{ staffer }}
{% endfor %}
