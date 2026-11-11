// Protokol (satnica dana) — prikazuje se na dnu stranice, ovim redosledom.
// vreme: početak; do: kraj (nije obavezno); naziv: šta se dešava.
// okvirno: true — tačno vreme nije određeno, dešava se negde između "vreme" i "do".
// napomena: sopstveni tekst ispod naziva (zamenjuje automatski "od … do …" / "okvirno, između …").
window.PROTOKOL = [
  { "vreme": "13:00", "naziv": "Crkveno venčanje" },
  { "vreme": "15:00", "naziv": "Okupljanje gostiju u restoranu" },
  { "vreme": "16:00", "naziv": "Građansko venčanje" },
  { "vreme": "16:15", "do": "17:00", "naziv": "Slikanje sa mladencima", "napomena": "okvirno od 16:15 do 17:00" },
  { "vreme": "17:00", "naziv": "Prvi ples" },
  { "vreme": "18:30", "do": "19:00", "okvirno": true, "naziv": "Bacanje bidermajera" },
  { "vreme": "20:00", "naziv": "Torta i trubači" },
  { "vreme": "20:15", "do": "20:45", "naziv": "DJ" },
  { "vreme": "20:45", "naziv": "Nastavak veselja uz bend" }
];
