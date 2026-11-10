// Raspored sale (mapa na stranici index.html), prepisan sa skice stolovi.jpeg.
// Koordinate su centri stolova u pikselima skice; menjajte ih ovde ako se nešto pomeri.
// Stolovi za goste: 1–3 i 5–17 (16 stolova). Sto 4 je za fotografe i nema goste (u 'ostalo').
window.SALA = {
  viewBox: [20, 30, 1835, 1160],
  stolovi: {
    1:  [175, 155],
    2:  [172, 418],
    3:  [170, 662],
    5:  [415, 155],
    6:  [408, 415],
    7:  [395, 665],
    8:  [405, 893],
    9:  [650, 685],
    10: [652, 440],
    11: [655, 160],
    12: [1360, 143],
    13: [1410, 430],
    14: [1412, 705],
    15: [1667, 625],
    16: [1585, 143],
    17: [1745, 320]
  },
  // Stubovi (crni kvadrati sa skice) — samo za orijentaciju, nisu klikabilni
  stubovi: [
    [507, 780],
    [860, 408],
    [858, 785],
    [1220, 787],
    [1570, 792],
    [1228, 410],
    [1578, 413]
  ],
  mladenacki: { x: 870, y: 78, w: 325, h: 154 },
  bina: { x: 873, y: 1012, w: 302, h: 150 },
  // Stolovi bez gostiju (crtaju se kao ostali stolovi, sa ikonom umesto broja; nisu klikabilni)
  ostalo: [
    { naziv: 'Sto 4 — fotografi', ikona: 'foto', x: 175, y: 895, stolica: 12 },
    { naziv: 'Muzika', ikona: 'muzika', x: 1562, y: 975, stolica: 12 }
  ]
};
