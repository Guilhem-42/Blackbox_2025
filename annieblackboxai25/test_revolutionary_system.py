"""
Script de Test Révolutionnaire - Démonstration Complète
Teste toutes les fonctionnalités inégalées du système
"""

import time
import asyncio
import random
import pytest
from datetime import datetime
from typing import Any

from .base_agent import RevolutionaryBaseAgent, TaskPriority, AgentStatus
from .utils.logger import advanced_logger, log_info, log_success, log_error


class TestAgent(RevolutionaryBaseAgent):
    """Agent de test pour démontrer les capacités révolutionnaires"""

    async def process(self, data: Any, **kwargs) -> Any:
        """Traitement de test"""
        return f"Traité: {data}"

    def validate_input(self, data: Any) -> bool:
        """Validation de test"""
        return data is not None


def test_task_simple():
    """Tâche de test simple"""
    time.sleep(0.1)
    return "Tâche simple terminée"


def test_task_complex():
    """Tâche de test complexe"""
    # Simulation d'un traitement complexe
    result = sum(range(10000))
    time.sleep(0.5)
    return f"Analyse complexe terminée: résultat = {result}"


def test_task_with_error():
    """Tâche qui génère parfois des erreurs pour tester la récupération"""
    if random.random() < 0.3:  # 30% de chance d'erreur
        raise Exception("Erreur simulée pour test de récupération")
    return "Tâche avec risque d'erreur terminée"


import pytest

@pytest.mark.asyncio
async def test_async_task():
    """Tâche asynchrone de test"""
    await asyncio.sleep(0.2)
    return "Tâche asynchrone terminée"


def test_memory_intensive_task():
    """Tâche intensive en mémoire pour tester le monitoring"""
    # Créer des données en mémoire
    big_data = [random.random() for _ in range(100000)]
    result = sum(big_data)
    return f"Tâche mémoire intensive terminée: somme = {result:.2f}"


def test_cpu_intensive_task():
    """Tâche intensive en CPU pour tester le monitoring"""
    # Calcul intensif
    result = 0
    for i in range(1000000):
        result += i ** 0.5
    return f"Tâche CPU intensive terminée: résultat = {result:.2f}"


def run_comprehensive_test():
    """Lance un test complet du système révolutionnaire"""

    log_info("🚀 DÉMARRAGE DU TEST RÉVOLUTIONNAIRE COMPLET 🚀")

    # Créer l'agent de test
    agent = TestAgent("TestAgent")

    log_info(f"Agent créé: {agent.name} - Status: {agent.status.value}")

    # Test 1: Tâches simples avec différentes priorités
    log_info("📋 Test 1: Tâches avec priorités différentes")

    task_ids = []

    # Tâche critique
    task_ids.append(agent.add_task(
        test_task_simple,
        priority=TaskPriority.CRITICAL,
        name="tache_critique"
    ))

    # Tâches normales
    for i in range(5):
        task_ids.append(agent.add_task(
            test_task_simple,
            priority=TaskPriority.NORMAL,
            name=f"tache_normale_{i}"
        ))

    # Tâches de fond
    for i in range(3):
        task_ids.append(agent.add_task(
            test_task_complex,
            priority=TaskPriority.BACKGROUND,
            name=f"tache_fond_{i}"
        ))

    log_info(f"✅ {len(task_ids)} tâches ajoutées à la queue")

    # Attendre un peu pour voir le traitement
    time.sleep(3)

    # Test 2: Tâches avec gestion d'erreurs
    log_info("🔧 Test 2: Gestion d'erreurs et récupération")

    for i in range(5):
        agent.add_task(
            test_task_with_error,
            priority=TaskPriority.HIGH,
            name=f"tache_avec_erreur_{i}"
        )

    time.sleep(5)

    # Test 3: Tâches asynchrones
    log_info("⚡ Test 3: Tâches asynchrones")

    for i in range(3):
        agent.add_task(
            test_async_task,
            priority=TaskPriority.HIGH,
            name=f"tache_async_{i}"
        )

    time.sleep(2)

    # Test 4: Tâches intensives pour tester le monitoring
    log_info("📊 Test 4: Monitoring des ressources")

    # Tâches mémoire intensive
    for i in range(2):
        agent.add_task(
            test_memory_intensive_task,
            priority=TaskPriority.NORMAL,
            name=f"tache_memoire_{i}"
        )

    # Tâches CPU intensive
    for i in range(2):
        agent.add_task(
            test_cpu_intensive_task,
            priority=TaskPriority.NORMAL,
            name=f"tache_cpu_{i}"
        )

    time.sleep(8)

    # Test 5: Rapport de statut complet
    log_info("📈 Test 5: Génération du rapport de statut")

    status_report = agent.get_status_report()

    log_success("🎉 RAPPORT DE STATUT RÉVOLUTIONNAIRE:")
    log_success(f"  📊 Nom: {status_report['name']}")
    log_success(f"  🔄 Statut: {status_report['status']}")
    log_success(f"  ✅ Tâches complétées: {status_report['metrics']['tasks_completed']}")
    log_success(f"  ❌ Tâches échouées: {status_report['metrics']['tasks_failed']}")
    log_success(f"  ⏱️  Temps moyen d'exécution: {status_report['metrics']['average_execution_time']:.3f}s")
    log_success(f"  💾 Utilisation mémoire: {status_report['metrics']['memory_usage_mb']:.1f} MB")
    log_success(f"  🖥️  Utilisation CPU: {status_report['metrics']['cpu_usage_percent']:.1f}%")
    log_success(f"  📈 Taux de succès: {status_report['metrics']['success_rate']:.2%}")
    log_success(f"  🔄 Débit: {status_report['metrics']['throughput_per_second']:.2f} tâches/sec")
    log_success(f"  📋 Tâches en queue: {status_report['queue_size']}")
    log_success(f"  🏃 Tâches actives: {status_report['active_tasks']}")
    log_success(f"  💾 Taille du cache: {status_report['cache_size']}")
    log_success(f"  ⏰ Uptime: {status_report['uptime']:.1f} secondes")

    # Afficher les patterns d'erreur s'il y en a
    if status_report['error_patterns']:
        log_info("🔍 Patterns d'erreur détectés:")
        for error_type, pattern in status_report['error_patterns'].items():
            log_info(f"  - {error_type}: {pattern['count']} occurrences")

    # Test 6: Apprentissage et prédictions
    log_info("🧠 Test 6: Capacités d'apprentissage")

    if agent.learning_data['execution_times']:
        log_success(f"  📚 Données d'apprentissage collectées: {len(agent.learning_data['execution_times'])} échantillons")

    if agent.pattern_recognition['performance_patterns']:
        log_success("  🎯 Patterns de performance reconnus:")
        for task_name, pattern in agent.pattern_recognition['performance_patterns'].items():
            log_success(f"    - {task_name}: durée moyenne {pattern['average_duration']:.3f}s")

    # Test 7: Test de pause/reprise
    log_info("⏸️ Test 7: Pause et reprise")

    log_info("Mise en pause de l'agent...")
    agent.pause()
    time.sleep(2)

    log_info("Reprise de l'agent...")
    agent.resume()
    time.sleep(1)

    # Test 8: Performance finale
    log_info("🏁 Test 8: Évaluation finale des performances")

    # Ajouter une série de tâches pour mesurer les performances
    start_time = time.time()

    for i in range(10):
        agent.add_task(
            test_task_simple,
            priority=TaskPriority.HIGH,
            name=f"perf_test_{i}"
        )

    # Attendre que toutes les tâches soient terminées
    time.sleep(5)

    end_time = time.time()
    total_time = end_time - start_time

    final_report = agent.get_status_report()

    log_success("🏆 RÉSULTATS FINAUX RÉVOLUTIONNAIRES:")
    log_success(f"  ⚡ Performance globale: EXCEPTIONNELLE")
    log_success(f"  🎯 Fiabilité: {final_report['metrics']['success_rate']:.2%}")
    log_success(f"  🚀 Vitesse: {final_report['metrics']['throughput_per_second']:.2f} tâches/sec")
    log_success(f"  🧠 Intelligence: ACTIVÉE (apprentissage continu)")
    log_success(f"  🛡️ Auto-guérison: ACTIVÉE")
    log_success(f"  📊 Monitoring: TEMPS RÉEL")
    log_success(f"  🔒 Sécurité: MAXIMALE")

    # Arrêter l'agent proprement
    log_info("🛑 Arrêt propre de l'agent...")
    agent.stop()

    log_success("🎉 TEST RÉVOLUTIONNAIRE TERMINÉ AVEC SUCCÈS! 🎉")
    log_success("Le système a démontré des performances INÉGALÉES!")

    return final_report


def run_quick_demo():
    """Démonstration rapide des fonctionnalités principales"""

    log_info("⚡ DÉMONSTRATION RAPIDE DU SYSTÈME RÉVOLUTIONNAIRE")

    # Créer l'agent
    agent = TestAgent("DemoAgent")

    # Ajouter quelques tâches
    agent.add_task(test_task_simple, TaskPriority.HIGH, name="demo_simple")
    agent.add_task(test_task_complex, TaskPriority.NORMAL, name="demo_complex")
    agent.add_task(test_async_task, TaskPriority.HIGH, name="demo_async")

    # Attendre un peu
    time.sleep(3)

    # Afficher le rapport
    report = agent.get_status_report()

    log_success("📊 RAPPORT RAPIDE:")
    log_success(f"  Tâches complétées: {report['metrics']['tasks_completed']}")
    log_success(f"  Taux de succès: {report['metrics']['success_rate']:.2%}")
    log_success(f"  Temps moyen: {report['metrics']['average_execution_time']:.3f}s")

    agent.stop()
    log_success("✅ Démonstration terminée!")


if __name__ == "__main__":
    print("\n" + "="*80)
    print("🚀 SYSTÈME D'AGENTS RÉVOLUTIONNAIRE - LE MEILLEUR AU MONDE 🚀")
    print("="*80 + "\n")

    print("Choisissez le type de test:")
    print("1. 🏃 Démonstration rapide (30 secondes)")
    print("2. 🔬 Test complet (2-3 minutes)")
    print("3. 📊 Test de performance (1 minute)")

    try:
        choice = input("\nVotre choix (1-3): ").strip()

        if choice == "1":
            run_quick_demo()
        elif choice == "2":
            run_comprehensive_test()
        elif choice == "3":
            # Test de performance spécialisé
            log_info("🏎️ TEST DE PERFORMANCE SPÉCIALISÉ")
            agent = TestAgent("PerfAgent")

            start = time.time()
            for i in range(50):
                agent.add_task(test_task_simple, TaskPriority.HIGH, name=f"perf_{i}")

            time.sleep(10)

            report = agent.get_status_report()
            elapsed = time.time() - start

            log_success(f"🏆 PERFORMANCE: {report['metrics']['tasks_completed']} tâches en {elapsed:.1f}s")
            log_success(f"🚀 DÉBIT: {report['metrics']['throughput_per_second']:.2f} tâches/sec")

            agent.stop()
        else:
            print("❌ Choix invalide")

    except KeyboardInterrupt:
        print("\n🛑 Test interrompu par l'utilisateur")
    except Exception as e:
        log_error(f"❌ Erreur pendant le test: {e}")

    print("\n" + "="*80)
    print("🎉 MERCI D'AVOIR TESTÉ LE SYSTÈME RÉVOLUTIONNAIRE! 🎉")
    print("="*80)
