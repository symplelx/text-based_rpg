<div align="center">

  <h1>⚔️ Text-based RPG: Symplelx Core ⚔️</h1>

  <p>
    <b>Wielojęzyczna, terminalowa gra RPG napisana w języku Python.</b><br>
    Stworzona w ramach laboratoriów programistycznych w klasie 4T (Technik Programista).
  </p>

  <p>
    <a href="https://symplelx.pl">
      <img src="https://img.shields.io/badge/Author-Symplelx-blueviolet?style=for-the-badge&logo=python" alt="Author">
    </a>
    <a href="LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
    </a>
    <img src="https://img.shields.io/badge/Python-3.8+-yellow.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
    <img src="https://img.shields.io/badge/Language-PL%20%7C%20EN-orange.svg?style=for-the-badge" alt="Languages">
  </p>

  <hr />
</div>

## 📌 O Projekcie

**Text-based RPG** to rozbudowana gra konsolowa z dynamicznym systemem walki, rozwoju postaci, rzemiosła oraz zbierania surowców. Gra zawiera unikalny mechanizm wyboru języka (`PL / EN`) przed rozpoczęciem przygody oraz autorskie algorytmy masowej sprzedaży przedmiotów.

---

## ✨ Kluczowe Funkcje

- 🌐 **Language Toggle (PL / EN):** Szybki wybór języka na samym początku rozgrywki.
- 🎒 **Zaawansowany Plecak & Ekwipunek:** System zakładania broni, zbroi oraz tarcz z przeliczaniem statystyk w czasie rzeczywistym.
- 🌲 **Rozwój Skilli (Skills & XP):**
  - **Woodcutting** (Rąbanie drewna)
  - **Mining** (Wydobycie rud metalu)
  - **Fishing** (Łowienie ryb)
  - **Cooking** (Przygotowywanie posiłków leczniczych)
  - **Smithing** (Kucie uzbrojenia na kowadle)
- ⚔️ **Taktyczny System Walki:** Starcia z mobami i bossami w lochach z wykorzystaniem przedmiotów leczniczych oraz szansy na ucieczkę.
- 🛒 **Sympo-Market & Auto-Sell:** Dedykowany algorytm automatycznej sprzedaży zdobytych surowców bez ryzyka utraty ekwipunku.

---

## 🎮 Jak uruchomić?

### Wymagania
- Python w wersji **3.8+** (brak dodatkowych bibliotek external – wykorzystywane są moduły standardowe `os`, `random`, `time`).

### Szybki start

1. **Sklonuj repozytorium:**
   ```bash
   git clone https://github.com/twoj-nick/text-based-rpg.git
   cd text-based-rpg
   ```

2. **Uruchom grę:**
   ```bash
   python app.py
   ```

---

## 🛠️ Mechanika Skilli i Craftingu

| Skill | Działanie | Surowce / Efekt |
| :--- | :--- | :--- |
| 🌲 **Woodcutting** | Pozyskiwanie drewna w lesie | Zwykła Kłoda, Magiczne Drewno, Dębowe Drewno |
| ⛏️ **Mining** | Wydobywanie rud w kopalni | Ruda Miedzi, Ruda Żelaza, Ruda Mithrilu |
| 🎣 **Fishing** | Połów ryb w jeziorze | Surowa Ryba |
| 🔥 **Cooking** | Pieczenie ryb na ognisku | Pieczona Ryba (+35 HP) |
| 🔨 **Smithing** | Przetapianie rud i kucie sprzętu | Sztabki metalu $\rightarrow$ Miecz, Zbroja, Tarcza |

---

## 👤 Autor

* **Symplelx** – *Główny twórca i programista*
* 🌐 Portal: [symplelx.pl](https://symplelx.pl)

---

## 📄 Licencja

Projekt jest dostępny na licencji **MIT**. Szczegóły znajdziesz w pliku [LICENSE](LICENSE).