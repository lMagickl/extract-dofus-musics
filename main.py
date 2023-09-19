from pydofus.d2p import D2PReader, InvalidD2PFile
import os

# Définir le répertoire contenant les fichiers D2P
directory_path = "./samples"

# Définir le répertoire de destination pour les fichiers MP3 extraits
destination_path = "./mp3_output"  # Remplacez ceci par le chemin de votre choix

# Créer le répertoire de destination s'il n'existe pas
os.makedirs(destination_path, exist_ok=True)

# Parcourir tous les fichiers du répertoire
for filename in os.listdir(directory_path):
    if filename.endswith(".d2p"):
        # Construire le chemin complet du fichier D2P
        d2p_file_path = os.path.join(directory_path, filename)

        # Ouvrir le fichier D2P en mode binaire
        stream = open(d2p_file_path, "rb")

        try:
            # Initialiser l'objet D2P avec le fichier D2P
            D2P = D2PReader(stream, False)
            D2P.load()  # Charger les fichiers D2P en mémoire

            for name, specs in D2P.files.items():
                # Vérifier si le fichier est un fichier MP3 (vous pouvez ajuster cette condition en fonction de vos besoins)
                if name.endswith(".mp3"):
                    # Construire le chemin de destination pour le fichier MP3
                    mp3_destination_path = os.path.join(destination_path, name)

                    # Extraire le répertoire du fichier
                    directory = os.path.dirname(mp3_destination_path)

                    # Vérifier si le répertoire existe, sinon le créer
                    if directory:
                        os.makedirs(directory, exist_ok=True)

                    # Lire le contenu du fichier
                    mp3_data = specs["binary"]

                    # Enregistrer le fichier MP3 dans le répertoire de destination
                    with open(mp3_destination_path, "wb") as mp3_file:
                        mp3_file.write(mp3_data)

        except InvalidD2PFile:
            pass
