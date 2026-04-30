---
layout: default
title: lowcase Labs
permalink: /labs/
---

<main class="labs-page">
  <section class="labs-hero">
    <img
      src="{{ '/assets/images/logos/lowcase-labs-logo.png' | relative_url }}"
      alt="lowcase Labs"
      class="labs-logo"
    />

    <p class="labs-kicker">Experimental Brews • Untamed Ideas</p>

    <p class="labs-intro">
      Welcome to lowcase Labs — the test bench for strange ferments, wild ingredients,
      small-batch experiments, and whatever Ruckus talks us into brewing next.
    </p>
  </section>

  <div style="text-align: center; margin-bottom: 1.5rem;">
    <a href="{{ '/' | relative_url }}" class="beer-back-link">← Back to Home</a>
  </div>

  <section class="labs-grid">
    {% assign lab_batches = site.labs | sort: "batch" %}

    {% for lab in lab_batches %}
      <article class="labs-card labs-showcase-card">
        <div class="labs-showcase-card__image">
          {% if lab.image %}
            <img src="{{ lab.image | relative_url }}" alt="{{ lab.title }}">
          {% endif %}
        </div>

        <div class="labs-showcase-card__content">
          {% if lab.status %}
            <div class="labs-status">{{ lab.status }}</div>
          {% endif %}

          <h2>{{ lab.title }}</h2>

          {% if lab.style %}
            <p class="labs-style">{{ lab.style }}</p>
          {% endif %}

          <div class="labs-stats">
            {% if lab.abv %}<span>ABV {{ lab.abv }}</span>{% endif %}
            {% if lab.ibu %}<span>IBU {{ lab.ibu }}</span>{% endif %}
            {% if lab.og %}<span>OG {{ lab.og }}</span>{% endif %}
            {% if lab.fg %}<span>FG {{ lab.fg }}</span>{% endif %}
            {% if lab.srm %}<span>SRM {{ lab.srm }}</span>{% endif %}
          </div>

          <div class="labs-summary">
            {{ lab.excerpt }}
          </div>

          {% if lab.ruckus_notes %}
            <p class="ruckus-notes">
              <strong>Ruckus Notes:</strong> {{ lab.ruckus_notes }}
            </p>
          {% endif %}

          <div class="labs-card-footer">
            <a href="{{ lab.url | relative_url }}" class="beer-link">View Experiment →</a>
          </div>
        </div>
      </article>
    {% endfor %}
  </section>
</main>