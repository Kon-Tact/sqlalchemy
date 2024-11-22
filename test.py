import pandas as pd

def test_stats_calculation():
    # Données factices pour le test
    test = pd.DataFrame({'Value': [10, 20, 30]})
    
    # Résultat attendu
    expected = {'mean': 20.0, 'median': 20.0, 'sum': 60.0}
    
    # Calcul des statistiques
    calculated = test['Value'].agg(['mean', 'median', 'sum']).to_dict()
    
    # Vérification des résultats
    assert calculated == expected, f"Expected {expected}, got {calculated}"

def test_stats_calculation2():
    # Données factices pour le test
    test2 = pd.DataFrame({'Value': [70, 140, 210]})
    
    # Résultat attendu
    expected = {'mean': 140.0, 'median': 140.0, 'sum': 420.0}
    
    # Calcul des statistiques
    calculated = test2['Value'].agg(['mean', 'median', 'sum']).to_dict()
    
    # Vérification des résultats
    assert calculated == expected, f"Expected {expected}, got {calculated}"

def test_stats_calculation3():
    # Données factices pour le test
    test3 = pd.DataFrame({'Value': [1, 2, 3]})
    
    # Résultat attendu
    expected = {'mean': 2, 'median': 2, 'sum': 6}
    
    # Calcul des statistiques
    calculated = test3['Value'].agg(['mean', 'median', 'sum']).to_dict()
    
    # Vérification des résultats
    assert calculated == expected, f"Expected {expected}, got {calculated}"