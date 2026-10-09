
# 📘 Guide Git : Fork, Synchronisation et Résolution de Conflits

Ce guide vous donne les bases indispensables pour travailler sur vos cours et projets individuels avec Git et GitHub :
1. **Forker** le projet du cours vers votre compte personnel.
2. **Configurer les dépôts distants** (`origin` vs `upstream`).
3. **Pousser votre travail personnel** sans écraser le cours.
4. **Récupérer les mises à jour** publiées par le professeur.
5. **Résoudre les conflits de merge**.

---

## 🧭 Le principe : `origin` vs `upstream`

Pour travailler proprement, votre dépôt local doit être relié à deux endroits différents :
* **`origin`** : Votre copie personnelle sur GitHub (votre *Fork*). C'est ici que vous avez les droits d'écriture et que vous pousserez votre travail pour les devoirs.
* **`upstream`** : Le dépôt officiel du professeur (la *source de vérité*). C'est depuis cet endroit que vous téléchargerez les nouveaux exercices et corrections.

```text
[Dépôt Professeur (upstream)]
       │
       │ (Mises à jour du cours)
       |
       ▼
 [Votre Machine Locale] ──────────► [Votre Fork GitHub (origin)]
                                            (Push devoirs)
```

---

## 🚀 Étape 1 : Forker et Cloner le projet

### 1. Créer le Fork sur GitHub
1. Rendez-vous sur la page GitHub du projet du cours.
2. En haut à droite, cliquez sur le bouton **Fork**.
3. Conservez les paramètres par défaut et cliquez sur **Create fork**.
4. Vous arrivez sur votre propre copie (l'URL devient `https://github.com/VOTRE_NOM/NOM_PROJET`).

### 2. Cloner votre Fork en local
Ouvrez votre terminal :

```bash
# 1. Placez-vous dans votre dossier d'études (celui créer sur votre machine)
cd cours_intro_big_data

# 2. Clonez VOTRE fork (remplacez par votre lien personnel)
git clone https://github.com/VOTRE_NOM/NOM_PROJET.git

# 3. Entrez dans le dossier cloné
cd NOM_PROJET
```

---

## 🔗 Étape 2 : Relier le dépôt officiel (`upstream`)

Par défaut, votre dossier local ne connaît que votre fork (`origin`). Il faut lui faire connaître le projet source (`upstream`) :

```bash
# Ajouter le dépôt du prof comme "upstream"
git remote add upstream https://github.com/NOM_DU_PROF/NOM_PROJET.git
```

### Vérifier votre configuration :
```bash
git remote -v
```

Vous devez voir **4 lignes** :
```text
origin    https://github.com/VOTRE_NOM/NOM_PROJET.git (fetch)
origin    https://github.com/VOTRE_NOM/NOM_PROJET.git (push)
upstream  https://github.com/NOM_DU_PROF/NOM_PROJET.git (fetch)
upstream  https://github.com/NOM_DU_PROF/NOM_PROJET.git (push)
```

---

## 💻 Étape 3 : Travailler et rendre vos devoirs

Chaque fois que vous modifiez un notebook, un script ou un fichier pour vos exercices :

```bash
# 1. Vérifier les fichiers que vous avez modifiés
git status

# 2. Ajouter toutes vos modifications (staging area)
git add notebook01.ipynb        # vous pouvez ajouter tous les fichiers avec `git add .`)

# 3. Enregistrer un commit avec un message descriptif
git commit -m "Réalisation du lab 1"

# 4. Envoyer votre travail sur VOTRE GitHub
git push origin main
```
> *(Si votre branche principale s'appelle `master`, remplacez `main` par `master`)*.

---

## 🔄 Étape 4 : Récupérer les mises à jour du professeur

Lorsque le professeur annonce avoir mis à jour le cours ou ajouté un nouvel examen :

```bash
# 1. Assurez-vous d'avoir enregistré/commité votre travail actuel
git add .
git commit -m "Sauvegarde avant mise à jour"

# 2. Télécharger les nouveautés du cours sans toucher à vos fichiers
git fetch upstream

# 3. Fusionner les nouveautés du cours dans votre code
git merge upstream/main

> `git pull`  équivaut à `git fetch` + `git merge`

# 4. Mettre à jour votre fork sur GitHub
git push origin main
```

### 💡 Astuce : Récupérer un SEUL fichier mis à jour par le prof
Si vous voulez uniquement remplacer un fichier précis (par exemple, le sujet d'examen `examen.ipynb`) sans fusionner tout le projet :
```bash
git fetch upstream
git checkout upstream/main -- chemin/vers/examen.ipynb
git commit -m "Mise à jour du sujet d'examen"
git push origin main
```

---

## ⚡ Étape 5 : Gérer les conflits de merge (Merge Conflicts)

Un conflit survient lorsque le professeur et vous avez **modifié les mêmes lignes du même fichier**. Git ne sait pas quelle version choisir et met la fusion en pause.

### 1. Identifier les conflits
Tapez :
```bash
git status
```
Git indiquera les fichiers en conflit (ex. : `both modified: exercice_1.py`).

### 2. Comprendre les marqueurs de conflit
Si vous ouvrez le fichier concerné dans VS Code (ou votre éditeur), vous verrez des balises insérées par Git :

```text
<<<<<<< HEAD (Votre version locale)
print("Mon résultat d'étudiant : 42")
=======
print("Correction officielle du professeur : 42")
>>>>>>> upstream/main (Version du prof)
```

* Entre `<<<<<<< HEAD` et `=======` : Ce que **vous** avez écrit.
* Entre `=======` et `>>>>>>>` : Ce que **le professeur** a écrit.

### 3. Résoudre le conflit
1. Dans votre éditeur, **gardez le code souhaité** et supprimez les balises `<<<<<<<`, `=======`, et `>>>>>>>`. 
   *(Dans VS Code, des boutons au-dessus du bloc vous permettent de cliquer directement sur : "Accept Current Change", "Accept Incoming Change" ou "Accept Both").*
2. Sauvegardez le fichier.

### 4. Finaliser la fusion
Dans votre terminal :
```bash
# 1. Marquer le fichier comme résolu
git add nom_du_fichier_resolu.py

# 2. Conclure le merge (laisser le message par défaut ou le modifier)
git commit -m "Résolution du conflit de fusion"

# 3. Pousser le tout sur votre fork
git push origin main
```

---

## 🛟 Les commandes de secours (SOS)

| Situation | Commande à exécuter |
| :--- | :--- |
| **"Je me suis emmêlé dans un merge et je veux annuler"** | `git merge --abort` |
| **"Je veux vérifier où pointent mes serveurs distants"** | `git remote -v` |
| **"Je veux voir l'historique de mes commits"** | `git log --oneline -n 5` |
| **"Le merge sur un Notebook `.ipynb` est illisible"** | Sauvegardez votre travail dans un fichier temporaire, puis écrasez le notebook avec celui du prof : `git checkout upstream/main -- nom_du_notebook.ipynb` |
