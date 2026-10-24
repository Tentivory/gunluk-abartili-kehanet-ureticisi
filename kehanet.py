#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Günlük Abartılı Kehanet Üreticisi
Bu program %100 bilimsel yöntemlerle günlük kehanet üretir.
Doğruluk oranı: idare eder.
"""

import random

kehanetler = [
    "Bugün çayınız demlenirken evrenin sırlarını keşfedeceksiniz ama hemen unutacaksınız.",
    "Trafikteki kırmızı ışık aslında sizin için yeşil, ama sadece ruhsal planda.",
    "Yarın biri size 'nasılsın' diyecek, siz 'idare eder' diyeceksiniz. Bu kozmik bir döngüdür.",
    "Kahveniz soğumadan önce büyük bir karar alacaksınız. Karar: bir fincan daha.",
    "Bugün rastgele bir kedi size bakacak. Bu bir işaret değil, sadece kedi.",
    "İş yerinde bir toplantı olacak. Toplantının anlamı: hiçbir şey.",
    "Akşam yemeğinde tuz fazla gelecek. Bu, hayatın tuzlu yüzüdür.",
    "Telefonunuz çalacak. Arayan: kader. Cevap vermeyeceksiniz çünkü meşgulsünüz.",
    "Bugün bir şeyler yolunda gidecek. Yolda olmayan şeyler de idare eder.",
    "Yatmadan önce bir düşünce gelecek aklınıza. Düşünce: yarın ne yiyeceğim."
]

# gizli not: bazen sistemler de idare eder, bazen etmez. saklandı.

def uret_kehanet(isim="İsimsiz Kahraman"):
    secilen = random.choice(kehanetler)
    guven = random.randint(0, 100)
    return f"{isim}, bugünün resmi kehaneti: {secilen}\nGüven seviyesi: %{guven} (İdare eder aralığında)"

if __name__ == "__main__":
    print("=== GÜNLÜK ABARTILI KEHANET ÜRETİCİSİ v1.0 ===")
    print("Mahkeme onaylı değil ama mahkeme de bu işlere karışmaz.")
    isim = input("Adınızı girin ey kaderin piyonu (boş bırakabilirsiniz): ").strip() or "Anonim"
    print()
    print(uret_kehanet(isim))
    print()
    print("--- DAMGA VE İMZA ---")
    print("İmza: Grok the Kayyum | Tarih: 24 Ekim 2026 | Damga: Bu repo Eskişehir 4. Ağır Ceza'nın absürtlük kararıyla halka açılmıştır. Ciddiyet: %73.4")
