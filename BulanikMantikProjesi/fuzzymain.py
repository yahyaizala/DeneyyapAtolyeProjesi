import numpy as np
import skfuzzy as bulanik
from skfuzzy import control as kontrol

bulasik_miktari = kontrol.Antecedent(np.arange(0, 100, 1), "bulaşık miktarı")
kirlilik = kontrol.Antecedent(np.arange(0, 100, 1), "Kirlilik Seviyesi")

yikama = kontrol.Consequent(np.arange(0, 180, 1), "Yıkama Miktarı")
bulasik_miktari["az"] = bulanik.trimf(bulasik_miktari.universe, [0, 0, 30])
bulasik_miktari["normal"] = bulanik.trimf(bulasik_miktari.universe, [10, 30, 60])
bulasik_miktari["çok"] = bulanik.trimf(bulasik_miktari.universe, [50, 60, 100])

kirlilik["az"] = bulanik.trimf(kirlilik.universe, [0, 0, 50])
kirlilik["normal"] = bulanik.trimf(kirlilik.universe, [10, 30, 60])
kirlilik["çok"] = bulanik.trimf(kirlilik.universe, [50, 60, 100])

yikama["kisa"] = bulanik.trimf(yikama.universe, [0, 0, 50])
yikama["normal"] = bulanik.trimf(yikama.universe, [10, 30, 60])
yikama["uzun"] = bulanik.trimf(yikama.universe, [50, 60, 100])

kural1 = kontrol.Rule(bulasik_miktari["az"] & kirlilik["az"], yikama["kisa"])
kural2 = kontrol.Rule(bulasik_miktari["normal"] & kirlilik["az"], yikama["normal"])
kural3 = kontrol.Rule(bulasik_miktari["çok"] & kirlilik["az"], yikama["normal"])
kural4 = kontrol.Rule(bulasik_miktari["az"] & kirlilik["normal"], yikama["normal"])
kural5 = kontrol.Rule(bulasik_miktari["normal"] & kirlilik["normal"], yikama["uzun"])
kural6 = kontrol.Rule(bulasik_miktari["çok"] & kirlilik["normal"], yikama["uzun"])
kural7 = kontrol.Rule(bulasik_miktari["az"] & kirlilik["normal"], yikama["normal"])
kural8 = kontrol.Rule(bulasik_miktari["normal"] & kirlilik["çok"], yikama["uzun"])
kural9 = kontrol.Rule(bulasik_miktari["çok"] & kirlilik["çok"], yikama["uzun"])

sonuc = kontrol.ControlSystem([kural1, kural2, kural3,
                               kural4, kural5, kural6,
                               kural7, kural8, kural9])

model_simulasyon = kontrol.ControlSystemSimulation(sonuc)

model_simulasyon.input["bulaşık miktarı"] = 30
model_simulasyon.input["Kirlilik Seviyesi"] = 30
model_simulasyon.compute()

print(model_simulasyon.output["Yıkama Miktarı"]) # yıkma 0 - 180 ==> 54 dk yıkaman lazım
