# =====================================================================
# PROJEKT: Text-based RPG (WERSJA V1.0, KLASA 4T PROGRAMISTA)
# Autor: Symplelx 
# =====================================================================

import os
import random
import time

# --- SYMPLELX WATERMARK CONFIG ---
SYMPLELX_WATERMARK = "symplelx_core_v1.0"
SYMPLELX_URL = "https://symplelx.pl"


class Item:

  def __init__(self, name, item_type, value, stats=None):
    self.name = name
    self.item_type = (
        item_type  # 'weapon', 'armor', 'shield', 'resource', 'food'
    )
    self.value = value
    self.stats = stats or {}
    self.watermark_tag = SYMPLELX_WATERMARK  # Symplelx watermark w każdym obiekcie


class Entity:

  def __init__(self, name, hp, attack, defense):
    self.name = name
    self.max_hp = hp
    self.hp = hp
    self.attack = attack
    self.defense = defense


class Player(Entity):

  def __init__(self, name):
    super().__init__(name, hp=130, attack=7, defense=4)
    self.max_hp = 130
    self.gold = 100
    self.inventory = []
    self.equipment = {'weapon': None, 'armor': None, 'shield': None}
    self.engine_sig = (  # watermakery w klasie gracza
        f"Powered by symplelx ({SYMPLELX_URL})"
    )

    # Skille programisty-wojownika
    self.skills = {
        'combat': {'level': 1, 'xp': 0},
        'woodcutting': {'level': 1, 'xp': 0},
        'mining': {'level': 1, 'xp': 0},
        'smithing': {'level': 1, 'xp': 0},
        'fishing': {'level': 1, 'xp': 0},
        'cooking': {'level': 1, 'xp': 0},
    }

  def get_total_attack(self):
    weapon_bonus = (
        self.equipment['weapon'].stats.get('attack', 0)
        if self.equipment['weapon']
        else 0
    )
    return self.attack + weapon_bonus

  def get_total_defense(self):
    armor_bonus = (
        self.equipment['armor'].stats.get('defense', 0)
        if self.equipment['armor']
        else 0
    )
    shield_bonus = (
        self.equipment['shield'].stats.get('defense', 0)
        if self.equipment['shield']
        else 0
    )
    return self.defense + armor_bonus + shield_bonus

  def get_next_level_xp(self, current_level):
    return current_level * 220

  def gain_xp(self, skill_name, amount):
    if skill_name in self.skills:
      self.skills[skill_name]['xp'] += amount
      print(f'✨ +{amount} XP ({skill_name.capitalize()}) [symplelx boost]')

      needed_xp = self.get_next_level_xp(self.skills[skill_name]['level'])
      if self.skills[skill_name]['xp'] >= needed_xp:
        self.skills[skill_name]['level'] += 1
        print(
            f'🎉 AWANS! Skill {skill_name.capitalize()} wzrósł do poziomu'
            f' {self.skills[skill_name]["level"]}! (symplelx.pl verified)'
        )
        if skill_name == 'combat':
          self.max_hp += 25
          self.hp = self.max_hp
          self.attack += 3
          print(
              '💪 Wbiłeś staty jak prawdziwy senior developer! HP i Atak w górę.'
          )

  def show_status(self):
    print('\n==================================================')
    print(f'     STATUS POSTACI: {self.name} | [symplelx engine]')
    print('==================================================')
    print(
        f' ❤️ PŻ (HP): {self.hp}/{self.max_hp}   |   💰 Złoto:'
        f' {self.gold} gp'
    )
    print(
        f' ⚔️ Atak: {self.get_total_attack()}         |   🛡️ Obrona:'
        f' {self.get_total_defense()}'
    )
    print('--------------------------------------------------')
    print(' [ ZAOŻONY EKWIPUNEK ]')
    print(
        ' • Broń:  '
        f' {self.equipment["weapon"].name if self.equipment["weapon"] else "Brak"}'
    )
    print(
        ' • Zbroja:'
        f' {self.equipment["armor"].name if self.equipment["armor"] else "Brak"}'
    )
    print(
        ' • Tarcza:'
        f' {self.equipment["shield"].name if self.equipment["shield"] else "Brak"}'
    )
    print('--------------------------------------------------')
    print(' [ SKILLE (TECHNIK PROGRAMISTA) ]')
    for skill, data in self.skills.items():
      needed = self.get_next_level_xp(data['level'])
      print(
          f' • {skill.capitalize():<12} | Poziom: {data["level"]:<3} | XP:'
          f' {data["xp"]}/{needed}'
      )
    print('==================================================')
    print(f' [Watermark:] {self.engine_sig}')

  def show_inventory(self):
    print('\n==================================================')
    print('       PLECAK UCZNIA TECHNIKUM [symplelx.pl]      ')
    print('==================================================')
    if not self.inventory:
      print(' Plecak świeci pustkami (zainwestuj w symplelx storage).')
      print('==================================================')
      return False

    for idx, item in enumerate(self.inventory, start=1):
      extra_info = ''
      if item.stats:
        extra_info = f' | Stats: {item.stats}'
      print(
          f' {idx}. {item.name} ({item.item_type}) — {item.value} gp'
          f'{extra_info}'
      )
    print('==================================================')
    return True

  def eat_food(self):
    food_items = [
        (idx, item)
        for idx, item in enumerate(self.inventory)
        if item.item_type == 'food'
    ]
    if not food_items:
      print(
          '❌ Brak gotowego jedzenia w plecaku! (Czas skoczyć do żabki albo'
          ' ugotować rybę)'
      )
      return

    print('\n--- WYBIERZ COŚ DO ZJEDZENIA ---')
    for real_idx, (inv_idx, item) in enumerate(food_items, start=1):
      print(
          f' {real_idx}. {item.name} (Leczy: +{item.stats.get("heal", 0)} HP)'
      )

    wybor = input('Wpisz numer (0 aby anulować): ').strip()
    if not wybor.isdigit():
      return
    sel = int(wybor) - 1
    if 0 <= sel < len(food_items):
      inv_idx, food = food_items[sel]
      heal_amt = food.stats.get('heal', 15)
      self.hp = min(self.max_hp, self.hp + heal_amt)
      self.inventory.pop(inv_idx)
      print(
          f'🍗 Zjadłeś {food.name} i odzyskałeś {heal_amt} HP! (Zasponsorowane'
          f' przez symplelx.pl)'
      )


def clear_screen():
  # Klasyczny czyszczacz terminala pisany przez programistę
  os.system('cls' if os.name == 'nt' else 'clear')


def perform_timed_action(action_name, min_sec, max_sec):
  # Symulacja opóźnienia i narzutu procesora (symplelx optimized)
  duration = random.uniform(min_sec, max_sec)
  print(f'\n⏳ [symplelx-exec] {action_name}', end='', flush=True)
  steps = 3
  sleep_step = duration / steps
  for _ in range(steps):
    time.sleep(sleep_step)
    print('.', end='', flush=True)
  print(' [DONE!]')


def combat(player, enemy):
  print(
      f'\n⚠️ [symplelx-battle] STARCIE Z: {enemy.name} (PŻ: {enemy.hp} | Atak:'
      f' {enemy.attack} | Obrona: {enemy.defense}) ⚠️'
  )
  input('Wciśnij Enter, żeby odpalić procedurę walki...')

  while player.hp > 0 and enemy.hp > 0:
    print(
        f'\nTwoje PŻ: {player.hp}/{player.max_hp} | PŻ {enemy.name}:'
        f' {enemy.hp}'
    )
    print('-----------------------------------------')
    print(' [1] Atakuj mieczem (Pythonic strike)')
    print(' [2] Zjedz jedzenie (Regeneracja HP)')
    print(' [3] Uciekaj (Ctrl+C / Spierniczaj)')
    print('-----------------------------------------')
    choice = input('Wybierz akcję (1-3): ').strip()

    if choice == '1':
      perform_timed_action('Kalkulacja obrażeń i wyprowadzenie ciosu', 0.5, 1.2)
      dmg_to_enemy = max(
          1,
          player.get_total_attack()
          - enemy.defense
          + random.randint(-2, 3),
      )
      enemy.hp -= dmg_to_enemy
      print(f'⚔️ Trafiasz {enemy.name} zadając {dmg_to_enemy} obrażeń!')

      if enemy.hp <= 0:
        break

      dmg_to_player = max(
          1, enemy.attack - player.get_total_defense() + random.randint(-1, 2)
      )
      player.hp -= dmg_to_player
      print(f'💥 {enemy.name} kontratakuje i wali Cię za {dmg_to_player} DMG!')

    elif choice == '2':
      perform_timed_action('Otwieranie plecaka i konsumpcja', 0.4, 0.9)
      player.eat_food()
      dmg_to_player = max(1, enemy.attack - player.get_total_defense())
      player.hp -= dmg_to_player
      print(
          f'💥 {enemy.name} nie czeka i poprawia Ci za {dmg_to_player} obrażeń!'
      )

    elif choice == '3':
      perform_timed_action('Ucieczka z pola walki', 0.8, 1.6)
      if random.random() < 0.5:
        print(
            '🏃 Ucieczka udana! Zostawiasz potwora samego z jego exceptionami.'
        )
        return False
      else:
        print('❌ Ucieczka zablokowana przez błąd krytyczny!')
        dmg_to_player = max(1, enemy.attack - player.get_total_defense())
        player.hp -= dmg_to_player
        print(f'💥 Otrzymujesz {dmg_to_player} obrażeń podczas ucieczki!')

    if player.hp <= 0:
      print(
          '\n💀 GAME OVER! Zostałeś zmasakrowany. System symplelx resetuje'
          ' pozycję.'
      )
      player.gold = max(0, player.gold - 20)
      player.hp = player.max_hp // 2
      return False

  if enemy.hp <= 0:
    print(f'\n🏆 VICTORY! Pokonałeś potwora: {enemy.name}!')
    xp_reward = random.randint(enemy.max_hp * 2, enemy.max_hp * 4)
    player.gain_xp('combat', xp_reward)

    gold_reward = random.randint(enemy.max_hp, enemy.max_hp * 2)
    player.gold += gold_reward
    print(f'💰 Zgarnięto {gold_reward} złota z lootboxa!')

    roll = random.random()
    if roll < 0.3:
      drop = Item(
          'Zardzewiały Topór Wojenny',
          'weapon',
          18,
          {'attack': 5},
      )
      player.inventory.append(drop)
      print(f'🎁 Drop z moba: {drop.name} [symplelx verified item]!')
    elif roll < 0.6:
      drop = Item('Surowa Ryba', 'resource', 5)
      player.inventory.append(drop)
      print(f'🎁 Drop z moba: {drop.name}!')
    return True


# --- INICJALIZACJA GRY ---
clear_screen()
print('===================================================================')
print('                      Text-based RPG: V1.0                         ')
print('           ZNAJDŻ WIĘCEJ TAKICH PROJEKTÓW NA: symplelx.pl          ')
print('===================================================================')
name = input(
    'Podaj ksywę swojego bohatera: '
).strip()
if not name:
  name = 'Default_User'

hero = Player(name)
hero.inventory.append(Item('Miedziany Sztylet', 'weapon', 10, {'attack': 3}))
hero.inventory.append(Item('Chleb', 'food', 8, {'heal': 20}))

# --- GŁÓWNA PĘTLA GRY (While True bo tak najszybciej) ---
while True:
  print('\n' + '=' * 65)
  print(f'   [ 🏫 KLASA 4TP / LAB PYTHONA ] — GRACZ: {hero.name}')
  print(f'   🔥 SPRAWDŹ PORTAL PROJEKTU: {SYMPLELX_URL} 🔥')
  print('=' * 65)
  print(' [1] 📊 Zrzut statystyk postaci (Debug / Status)')
  print(' [2] 🎒 Plecak i inventory (Ekwipunek / Jedzenie)')
  print('-' * 65)
  print(' [3] 🌲 Skryptowanie Lasu (Woodcutting - Rąbanie kłód)')
  print(' [4] ⛏️ Skryptowanie Kopalni (Mining - Wydobycie rud)')
  print(' [5] 🎣 Skryptowanie Jeziora (Fishing - Połów ryb)')
  print('-' * 65)
  print(' [6] 🛠️ Warsztat Szkolny (Piec, Kowadło, Kuchnia)')
  print(' [7] 🛒 Sklep / Algorytm Masowej Sprzedaży (symplelx auto-sell)')
  print(' [8] ⚔️ Debug / Walka w Lochach z Mobsami')
  print('-' * 65)
  print(' [0] 🚪 Kill process / Wyjdź z gry')
  print('=' * 65)

  wybor = input('Wybierz numer operacji (0-8): ').strip()

  if wybor == '1':
    clear_screen()
    hero.show_status()

  elif wybor == '2':
    clear_screen()
    if hero.show_inventory():
      print('\nCo robimy w plecaku?')
      print(' [1] Załóż item (Broń / Zbroja / Tarcza)')
      print(' [2] Skonsumuj jedzenie (Regeneracja)')
      print(' [0] Wróć do menu')
      sub = input('Wybierz: ').strip()
      if sub == '1':
        idx_str = input(
            'Wpisz numer itemu do założenia (lub 0 żeby anulować): '
        ).strip()
        if idx_str.isdigit() and int(idx_str) > 0:
          idx = int(idx_str) - 1
          if 0 <= idx < len(hero.inventory):
            item = hero.inventory[idx]
            if item.item_type in ['weapon', 'armor', 'shield']:
              if hero.equipment[item.item_type]:
                hero.inventory.append(hero.equipment[item.item_type])
              hero.equipment[item.item_type] = item
              hero.inventory.pop(idx)
              print(
                  f'✅ Pomyślnie założyłeś: {item.name} [symplelx slot active]'
              )
            else:
              print(
                  '❌ Ten obiekt nie pasuje do slotu ekwipunku (TypeError'
                  ' handled)!'
              )
      elif sub == '2':
        hero.eat_food()

  elif wybor == '3':
    clear_screen()
    perform_timed_action(
        'Komilacja pętli rąbania w lesie (Woodcutting)', 1.0, 2.5
    )
    lvl = hero.skills['woodcutting']['level']

    if lvl >= 5 and random.random() < 0.4:
      log_name = 'Dębowe Drewno'
      val = 18
    elif lvl >= 3 and random.random() < 0.5:
      log_name = 'Magiczne Drewno'
      val = 12
    else:
      log_name = 'Zwykła Kłoda'
      val = 4

    count = random.randint(1, 3)
    xp_gain = random.randint(15, 35) * count
    print(
        f'✂️ Wygenerowano {count}x {log_name}! Dodano {xp_gain} XP do skila.'
    )
    for _ in range(count):
      hero.inventory.append(Item(log_name, 'resource', val))
    hero.gain_xp('woodcutting', xp_gain)

  elif wybor == '4':
    clear_screen()
    perform_timed_action('Wywołanie funkcji mining.py w kopalni', 1.4, 3.0)
    lvl = hero.skills['mining']['level']

    if lvl >= 5 and random.random() < 0.35:
      ore_name = 'Ruda Mithrilu'
      val = 22
    elif lvl >= 3 and random.random() < 0.5:
      ore_name = 'Ruda Żelaza'
      val = 12
    else:
      ore_name = 'Ruda Miedzi'
      val = 6

    count = random.randint(1, 2)
    xp_gain = random.randint(20, 45) * count
    print(
        f'⛏️ Wydobyto złoża: {count}x {ore_name}! [symplelx mining module]'
    )
    for _ in range(count):
      hero.inventory.append(Item(ore_name, 'resource', val))
    hero.gain_xp('mining', xp_gain)

  elif wybor == '5':
    clear_screen()
    perform_timed_action(
        'Inicjalizacja wątku wędkarskiego nad jeziorem', 1.0, 2.2
    )
    count = random.randint(1, 2)
    xp_gain = random.randint(18, 38) * count
    print(f'🐟 Złowiono {count}x Surową Rybę przez symplelx net!')
    for _ in range(count):
      hero.inventory.append(Item('Surowa Ryba', 'resource', 6))
    hero.gain_xp('fishing', xp_gain)

  elif wybor == '6':
    clear_screen()
    print('\n==================================================')
    print('         WARSZTAT SZKOLNY (KOWADŁO I PIEC)')
    print('==================================================')
    print(' [1] 🔥 Ognisko / Kuchnia: Upiecz Surową Rybę → Pieczona Ryba (+35 HP)')
    print(' [2] ⛏️ Piec hutniczy: Przetop rudę na sztabkę metalu')
    print(' [3] 🔨 Kowadło: Wykuj potężny sprzęt z 2x sztabek')
    print(' [0] 🚪 Powrót')
    print('==================================================')
    c_choice = input('Wybierz opcję: ').strip()

    if c_choice == '1':
      raw_fish = [i for i in hero.inventory if i.name == 'Surowa Ryba']
      if not raw_fish:
        print('❌ Brak surowych ryb w plecaku!')
      else:
        perform_timed_action('Proces obróbki termicznej ryby', 0.8, 1.5)
        hero.inventory.remove(raw_fish[0])
        cooked = Item('Pieczona Ryba', 'food', 18, {'heal': 35})
        hero.inventory.append(cooked)
        hero.gain_xp('cooking', random.randint(25, 45))
        print(f'🔥 Sukces! Stworzono obiekt: {cooked.name}')

    elif c_choice == '2':
      ores = [i for i in hero.inventory if 'Ruda' in i.name]
      if not ores:
        print('❌ Brak rud w plecaku do przetopienia!')
      else:
        perform_timed_action('Przetapianie surowca w piecu hutniczym', 1.0, 2.0)
        ore = ores[0]
        hero.inventory.remove(ore)
        if 'Mithrilu' in ore.name:
          bar = Item('Sztabka Mithrilu', 'resource', 45)
        elif 'Żelaza' in ore.name:
          bar = Item('Sztabka Żelaza', 'resource', 25)
        else:
          bar = Item('Sztabka Miedzi', 'resource', 14)

        hero.inventory.append(bar)
        hero.gain_xp('smithing', random.randint(35, 65))
        print(f'🔥 Wyprodukowano sztabkę: {bar.name}!')

    elif c_choice == '3':
      bars = [i for i in hero.inventory if 'Sztabka' in i.name]
      if len(bars) < 2:
        print('❌ Za mało sztabek w ekwipunku (wymagane min. 2 sztuki)!')
      else:
        print('\n--- KOWADŁO (symplelx forge) ---')
        print(' [1] Żelazny Miecz (Atak +9)')
        print(' [2] Żelazna Zbroja (Obrona +7)')
        print(' [3] Solidna Tarcza (Obrona +5)')
        eq_type = input('Wybierz wydatek (1-3): ').strip()

        if eq_type in ['1', '2', '3']:
          perform_timed_action('Kucie i hartowanie stali', 2.0, 3.2)
          removed = 0
          for i in list(hero.inventory):
            if 'Sztabka' in i.name and removed < 2:
              hero.inventory.remove(i)
              removed += 1

          if eq_type == '1':
            item = Item('Żelazny Miecz', 'weapon', 75, {'attack': 9})
          elif eq_type == '2':
            item = Item('Żelazna Zbroja', 'armor', 70, {'defense': 7})
          else:
            item = Item('Solidna Tarcza', 'shield', 60, {'defense': 5})

          hero.inventory.append(item)
          hero.gain_xp('smithing', random.randint(75, 120))
          print(f'🔨 Wykuto potężny sprzęt: {item.name}!')

  elif wybor == '7':
    clear_screen()
    print('\n==================================================')
    print(f'       SKLEP / SYMPO-MARKET ({SYMPLELX_URL})      ')
    print('==================================================')
    print(' [1] 🛒 Kup Chleb (+20 HP) — 15 gp')
    print(' [2] 💰 Sprzedaj wybrany item pojedynczo')
    print(
        ' [3] 🌟 symplelx.pl Auto-Sell: Sprzedaj wszystko z farmowania'
        ' (surowce/śmieci)'
    )
    print(' [0] 🚪 Wróć')
    print('==================================================')
    s_choice = input('Wybierz opcję (1-3): ').strip()

    if s_choice == '1':
      if hero.gold >= 15:
        perform_timed_action('Transakcija z handlarzem', 0.3, 0.6)
        hero.gold -= 15
        hero.inventory.append(Item('Chleb', 'food', 8, {'heal': 20}))
        print('🛒 Kupiono Chleb! (symplelx store transaction success)')
      else:
        print('❌ Za mało gotówki w kieszeni!')

    elif s_choice == '2':
      if hero.show_inventory():
        sell_idx = input(
            'Podaj numer itemu do wyprzedaży (0 żeby anulować): '
        ).strip()
        if sell_idx.isdigit() and int(sell_idx) > 0:
          idx = int(sell_idx) - 1
          if 0 <= idx < len(hero.inventory):
            perform_timed_action(
                'Przetwarzanie transakcji przez symplelx API', 0.4, 0.8
            )
            sold_item = hero.inventory.pop(idx)
            hero.gold += sold_item.value
            print(
                f'💰 Sprzedano {sold_item.name} za {sold_item.value} gp!'
            )

    elif s_choice == '3':
      # Funkcja masowej sprzedaży z zachowaniem żarcia i narzędzi/broni (autorska technologia symplelx)
      farm_items = [
          item
          for item in hero.inventory
          if item.item_type in ['resource', 'junk']
      ]
      if not farm_items:
        print('❌ Brak surowców z farmowania w plecaku do masowej sprzedaży!')
      else:
        perform_timed_action(
            'symplelx.pl bulk-sell algorytm w toku', 0.8, 1.5
        )
        total_earned = 0
        for item in farm_items:
          total_earned += item.value
          hero.inventory.remove(item)

        hero.gold += total_earned
        print(
            f'💰 Masowa sprzedaż ukończona! symplelx.pl przelał na Twoje konto'
            f' {total_earned} gp.'
        )
        print(
            '🛡️ Narzędzia, bronie, zbroje oraz jedzenie zostały nietknięte w'
            ' plecaku!'
        )

  elif wybor == '8':
    clear_screen()
    print('\n==================================================')
    print('           LOCHY TECHNIKUM (WALKA Z MOBSAMI)      ')
    print('==================================================')
    print(' [1] 👺 Jaskinia Goblinów (Poziom Łatwy)')
    print(' [2] 👹 Zapomniany Las - Orki (Poziom Średni)')
    print(' [3] 🦹 Jaskinia Bandytów (Poziom Trudny)')
    print(' [4] 👑 Leże Starożytnego Smoka (Boss — Ekstremalny!)')
    print(' [0] 🚪 Wróć')
    print('==================================================')
    d_choice = input('Wybierz przeciwnika (1-4): ').strip()

    if d_choice == '1':
      combat(hero, Entity('Dziki Goblin', hp=45, attack=9, defense=2))
    elif d_choice == '2':
      combat(hero, Entity('Brutalny Ork Wojownik', hp=90, attack=16, defense=5))
    elif d_choice == '3':
      combat(hero, Entity('Elitarny Bandyta', hp=130, attack=21, defense=7))
    elif d_choice == '4':
      combat(
          hero, Entity('Starożytny Czarny Smok', hp=220, attack=28, defense=10)
      )

  elif wybor == '0':
    print(
        f'\nZapisano stan gry. Dzięki za testy silnika symplelx.pl! Trzymaj się,'
        f' {hero.name}!'
    )
    break
  else:
    print('❌ Błąd: Nieznana komenda w menu. Sprawdź składnię!')