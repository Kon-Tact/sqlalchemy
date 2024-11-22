import pandas as pd

# Chargement des données depuis un fichier CSV
data = pd.read_csv('data.csv')

# Calcul des statistiques
stats = data['Value'].agg(['mean', 'median', 'sum'])

# Sauvegarde des résultats dans un fichier CSV
stats.to_csv('results.csv', header=['Statistic'], index_label='Metric')

# Affichage des résultats
print(stats)
