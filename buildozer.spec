[app]
title = Lot App
package.name = lotapp
package.domain = org.gaetan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

# Ton fichier principal
main.py = lot_app.py

# Permissions (internet pour vérifier les mises à jour)
android.permissions = INTERNET

# Icône par défaut
icon.filename = %(source.dir)s/icon.png

# Version de ton app
version = 1.0

# Utiliser python3 + kivy + requests + pyjnius
requirements = python3,kivy,requests,pyjnius@master,cython<3

# Bootstrap Kivy
bootstrap = sdl2

# API Android
android.api = 31
android.minapi = 21
android.ndk = 25b

# Chemins Android SDK et SDK Manager
android.sdk_path = /home/gaetan/Bureau/lot_app_build/.buildozer/android/platform/android-sdk
android.sdkmanager = /home/gaetan/Bureau/lot_app_build/.buildozer/android/platform/android-sdk/cmdline-tools/latest/bin/sdkmanager

[buildozer]
log_level = 2
warn_on_root = 1
