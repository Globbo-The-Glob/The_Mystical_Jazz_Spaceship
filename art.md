---
layout: payge
title: Art
permalink: /art/
---

<style>
.art-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 15px;
  padding: 20px 0;
}

.art-tile {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  aspect-ratio: 1;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

.art-tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
  display: block;
}

.art-tile:hover img {
  transform: scale(1.15);
}

.art-tile:hover {
  box-shadow: 0 8px 16px rgba(255, 0, 221, 0.4);
}

/* Lightbox modal */
.lightbox {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9);
}

.lightbox.active {
  display: flex;
  justify-content: center;
  align-items: center;
}

.lightbox-content {
  position: relative;
  max-width: 90vw;
  max-height: 90vh;
}

.lightbox-content img {
  max-width: 100%;
  max-height: 100%;
}

.lightbox-close {
  position: absolute;
  top: 20px;
  right: 30px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
}

.lightbox-close:hover {
  color: #ff00dd;
}
</style>

<div class="art-grid">
  <div class="art-tile" onclick="openLightbox('/images/birb.jpg')">
    <img src="/images/birb.jpg" alt="birb">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/bug.jpg')">
    <img src="/images/bug.jpg" alt="bug">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/card.jpg')">
    <img src="/images/card.jpg" alt="card">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/cool door.jpg')">
    <img src="/images/cool door.jpg" alt="cool door">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/dude.jpg')">
    <img src="/images/dude.jpg" alt="dude">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/fishy.jpg')">
    <img src="/images/fishy.jpg" alt="fishy">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/funky face.jpg')">
    <img src="/images/funky face.jpg" alt="funky face">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/gang.jpg')">
    <img src="/images/gang.jpg" alt="gang">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/hat.jpg')">
    <img src="/images/hat.jpg" alt="hat">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/holding.jpg')">
    <img src="/images/holding.jpg" alt="holding">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/Holes.jpg')">
    <img src="/images/Holes.jpg" alt="Holes">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/lady.jpg')">
    <img src="/images/lady.jpg" alt="lady">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/octo_poo.jpg')">
    <img src="/images/octo_poo.jpg" alt="octo_poo">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/photo_2024-05-11_17-05-31.jpg')">
    <img src="/images/photo_2024-05-11_17-05-31.jpg" alt="photo">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/planck.jpg')">
    <img src="/images/planck.jpg" alt="planck">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/rach_roller.jpg')">
    <img src="/images/rach_roller.jpg" alt="rach_roller">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/sploon.jpg')">
    <img src="/images/sploon.jpg" alt="sploon">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/stoner.jpg')">
    <img src="/images/stoner.jpg" alt="stoner">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/tattoo plan.jpg')">
    <img src="/images/tattoo plan.jpg" alt="tattoo plan">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/tongue.jpg')">
    <img src="/images/tongue.jpg" alt="tongue">
  </div>
  <div class="art-tile" onclick="openLightbox('/images/tshirt.jpg')">
    <img src="/images/tshirt.jpg" alt="tshirt">
  </div>
</div>

<div id="lightbox" class="lightbox" onclick="closeLightbox()">
  <div class="lightbox-content" onclick="event.stopPropagation()">
    <span class="lightbox-close" onclick="closeLightbox()">&times;</span>
    <img id="lightbox-img" src="" alt="">
  </div>
</div>

<script>
function openLightbox(src) {
  const lightbox = document.getElementById('lightbox');
  const img = document.getElementById('lightbox-img');
  img.src = src;
  lightbox.classList.add('active');
}

function closeLightbox() {
  const lightbox = document.getElementById('lightbox');
  lightbox.classList.remove('active');
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeLightbox();
  }
});
</script>
