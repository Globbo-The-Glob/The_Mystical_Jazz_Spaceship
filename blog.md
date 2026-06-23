---
layout: payge
title: Blog
permalink: /blog/
---

The Mystical Jazz Spaceship brings you only the hippest grokkings from across the vast expanse of the omnicosmos. Tune in sporadically for all kinds of musings, on music, philosophy, maths, physics, biology and things I am think about

-------------------

{% assign categories = "" | split: "" %}
{% for post in site.posts %}
  {% assign post_url = post.permalink | split: "/" %}
  {% if post_url.size > 3 %}
    {% assign category = post_url[2] %}
  {% else %}
    {% assign category = "Misc" %}
  {% endif %}
  {% unless categories contains category %}
    {% assign categories = categories | push: category %}
  {% endunless %}
{% endfor %}

{% assign categories = categories | sort %}

{% for category in categories %}
# {{ category | capitalize }}
{% for post in site.posts %}
  {% assign post_url = post.permalink | split: "/" %}
  {% if post_url.size > 3 %}
    {% assign post_category = post_url[2] %}
  {% else %}
    {% assign post_category = "Misc" %}
  {% endif %}
  {% if post_category == category %}
<a href="{{post.permalink}}">{{post.title}}</a>
  {% endif %}
{% endfor %}

{% endfor %}
