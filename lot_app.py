import datetime
import requests
import webbrowser
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock

# --- CONFIG ---
LOCAL_VERSION = "1.0.0"  # Version actuelle
VERSION_URL = "https://raw.githubusercontent.com/Gaetan-v/lot-app-updates/main/version.txt"
APK_URL = "https://github.com/Gaetan-v/lot-app-updates/releases/download/v1.1.0/lot_app_v1.1.0.apk"


class LotApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        # Labels
        self.date_label = Label(text="", font_size=20)
        self.lot_label = Label(text="", font_size=24, bold=True)
        self.lot_jour_label = Label(text="", font_size=20)

        # Zone pour afficher mise à jour (label ou bouton)
        self.update_widget = Label(text="Vérification des mises à jour...", font_size=16, color=(0.5, 0.5, 0.5, 1))

        self.layout.add_widget(self.date_label)
        self.layout.add_widget(self.lot_label)
        self.layout.add_widget(self.lot_jour_label)
        self.layout.add_widget(self.update_widget)

        # Calcul du lot du jour
        self.update_lot()

        # Vérification après 1s
        Clock.schedule_once(lambda dt: self.check_update(), 1)

        return self.layout

    def update_lot(self):
        today = datetime.date.today()

        # Numéro de lot classique (année, semaine, jour)
        dernier_chiffre_annee = str(today.year)[-1]
        numero_semaine = today.isocalendar()[1]
        jour_semaine = today.isoweekday()
        lot_num = f"L{dernier_chiffre_annee}{numero_semaine:02d}{jour_semaine}"

        # Lot basé sur le jour de l'année
        jour_annee = (today - datetime.date(today.year, 1, 1)).days + 1
        lot_jour = f"L{dernier_chiffre_annee}{jour_annee:03d}"

        # Mise à jour des labels
        self.date_label.text = f"Date : {today.strftime('%d-%m-%Y')}"
        self.lot_label.text = f"Numéro de lot : {lot_num}"
        self.lot_jour_label.text = f"Lot (jour de l'année) : {lot_jour}"

    def check_update(self):
        try:
            response = requests.get(VERSION_URL, timeout=5)
            if response.status_code == 200:
                remote_version = response.text.strip()
                if remote_version != LOCAL_VERSION:
                    # Crée un bouton de mise à jour
                    self.layout.remove_widget(self.update_widget)
                    update_btn = Button(
                        text=f"⏳ Mise à jour disponible (v{remote_version}) - Cliquez ici",
                        size_hint=(1, 0.2),
                        background_color=(1, 0.5, 0, 1),
                        font_size=16,
                    )
                    update_btn.bind(on_press=self.do_update)
                    self.layout.add_widget(update_btn)
                    self.update_widget = update_btn
                else:
                    self.update_widget.text = "✅ Application à jour"
                    self.update_widget.color = (0, 1, 0, 1)
            else:
                self.update_widget.text = "⚠️ Erreur lors de la vérification"
                self.update_widget.color = (1, 0, 0, 1)
        except Exception:
            self.update_widget.text = "⚠️ Impossible de vérifier la mise à jour"
            self.update_widget.color = (1, 0, 0, 1)

    def do_update(self, instance):
        # Ouvre le lien APK dans le navigateur → téléchargement sur le téléphone
        webbrowser.open(APK_URL)


if __name__ == "__main__":
    LotApp().run()
