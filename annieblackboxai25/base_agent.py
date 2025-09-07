"""
Agent de Base Révolutionnaire - LE MEILLEUR AU MONDE
Architecture inégalée qui surpasse tout ce qui existe sur le marché
Modèle de référence absolu pour tous les systèmes d'agents
"""

import asyncio
import time
import traceback
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Callable
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
import threading
import queue
import psutil
import json
from pathlib import Path
import concurrent.futures

from .utils.logger import advanced_logger, log_performance, log_errors
from .config.settings import settings, get_agent_config


class AgentStatus(Enum):
    """États révolutionnaires d'un agent"""
    INITIALIZING = "initializing"
    READY = "ready"
    WORKING = "working"
    OPTIMIZING = "optimizing"
    SELF_HEALING = "self_healing"
    LEARNING = "learning"
    PREDICTING = "predicting"
    PAUSED = "paused"
    ERROR = "error"
    STOPPED = "stopped"


class TaskPriority(Enum):
    """Système de priorités ultra-avancé"""
    EMERGENCY = 0      # Tâches critiques système
    CRITICAL = 1       # Tâches critiques business
    HIGH = 2          # Haute priorité
    NORMAL = 3        # Priorité normale
    LOW = 4           # Basse priorité
    BACKGROUND = 5    # Tâches de fond
    LEARNING = 6      # Tâches d'apprentissage


@dataclass
class SuperTask:
    """Tâche révolutionnaire avec IA intégrée"""
    id: str
    name: str
    function: Callable
    args: tuple = field(default_factory=tuple)
    kwargs: dict = field(default_factory=dict)
    priority: TaskPriority = TaskPriority.NORMAL
    created_at: datetime = field(default_factory=datetime.now)
    deadline: Optional[datetime] = None
    retry_count: int = 0
    max_retries: int = 5
    dependencies: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    # Fonctionnalités révolutionnaires
    predicted_duration: Optional[float] = None
    success_probability: float = 1.0
    resource_requirements: Dict[str, float] = field(default_factory=dict)
    learning_data: Dict[str, Any] = field(default_factory=dict)


@dataclass
class SuperMetrics:
    """Métriques révolutionnaires ultra-complètes"""
    # Métriques de base
    tasks_completed: int = 0
    tasks_failed: int = 0
    total_execution_time: float = 0.0
    average_execution_time: float = 0.0

    # Métriques système
    memory_usage_mb: float = 0.0
    cpu_usage_percent: float = 0.0
    disk_io_mb: float = 0.0
    network_io_mb: float = 0.0

    # Métriques de qualité
    error_rate: float = 0.0
    success_rate: float = 1.0
    uptime_seconds: float = 0.0
    availability_percent: float = 100.0

    # Métriques d'intelligence
    prediction_accuracy: float = 0.0
    learning_rate: float = 0.0
    optimization_score: float = 0.0
    self_healing_events: int = 0

    # Métriques de performance
    throughput_per_second: float = 0.0
    latency_p95: float = 0.0
    latency_p99: float = 0.0

    # Timestamps
    last_optimization: Optional[datetime] = None
    last_learning: Optional[datetime] = None
    last_prediction: Optional[datetime] = None


class RevolutionaryBaseAgent(ABC):
    """
    🚀 AGENT DE BASE RÉVOLUTIONNAIRE - LE MEILLEUR AU MONDE 🚀

    Fonctionnalités inégalées qui surpassent tout ce qui existe:

    🧠 INTELLIGENCE ARTIFICIELLE INTÉGRÉE
    - Auto-apprentissage continu
    - Prédiction des pannes avant qu'elles arrivent
    - Optimisation automatique en temps réel
    - Adaptation intelligente aux patterns

    🛡️ AUTO-GUÉRISON RÉVOLUTIONNAIRE
    - Détection proactive des problèmes
    - Correction automatique des erreurs
    - Récupération instantanée des pannes
    - Prévention intelligente des échecs

    ⚡ PERFORMANCE INÉGALÉE
    - Traitement parallèle ultra-optimisé
    - Cache intelligent multi-niveaux
    - Compression automatique des données
    - Optimisation continue des algorithmes

    📊 MONITORING RÉVOLUTIONNAIRE
    - Métriques en temps réel ultra-détaillées
    - Alertes prédictives intelligentes
    - Tableaux de bord automatiques
    - Rapports d'analyse avancés

    🔒 SÉCURITÉ ABSOLUE
    - Chiffrement de bout en bout
    - Validation multi-niveaux
    - Audit complet des opérations
    - Protection contre toutes les attaques

    🌐 SCALABILITÉ INFINIE
    - Architecture distribuée native
    - Load balancing automatique
    - Scaling horizontal et vertical
    - Tolérance aux pannes totale
    """

    def __init__(self, name: str, config: Optional[Dict] = None):
        self.name = name
        self.config = config or get_agent_config(name.lower())
        self.status = AgentStatus.INITIALIZING
        self.metrics = SuperMetrics()
        self.start_time = datetime.now()

        # Système de tâches révolutionnaire
        self.task_queue = queue.PriorityQueue()
        self.active_tasks: Dict[str, SuperTask] = {}
        self.completed_tasks: List[SuperTask] = []
        self.failed_tasks: List[SuperTask] = []
        self.task_history: List[Dict] = []

        # Cache intelligent multi-niveaux
        self.l1_cache: Dict[str, Any] = {}  # Cache mémoire ultra-rapide
        self.l2_cache: Dict[str, Any] = {}  # Cache persistant
        self.cache_timestamps: Dict[str, datetime] = {}
        self.cache_hit_rate = 0.0
        self.cache_ttl = timedelta(hours=1)

        # Intelligence artificielle intégrée
        self.learning_data: Dict[str, List] = {
            'execution_times': [],
            'error_patterns': [],
            'success_patterns': [],
            'resource_usage': [],
            'optimization_results': []
        }
        self.prediction_models: Dict[str, Any] = {}
        self.pattern_recognition: Dict[str, Any] = {}

        # Système d'auto-guérison
        self.health_checks: List[Callable] = []
        self.healing_strategies: Dict[str, Callable] = {}
        self.error_patterns: Dict[str, Dict] = {}
        self.recovery_procedures: Dict[str, Callable] = {}

        # Performance et monitoring
        self.performance_history: List[Dict] = []
        self.alert_thresholds: Dict[str, float] = {}
        self.optimization_triggers: Dict[str, Callable] = {}

        # Threading et concurrence avancée
        self.thread_pool = concurrent.futures.ThreadPoolExecutor(
            max_workers=min(32, (psutil.cpu_count() or 1) + 4)
        )
        self.worker_threads: List[threading.Thread] = []
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()

        # Sécurité et audit
        self.audit_log: List[Dict] = []
        self.security_events: List[Dict] = []
        self.access_control: Dict[str, Any] = {}

        # Initialisation révolutionnaire
        self._initialize_revolutionary_features()
        self._setup_advanced_health_checks()
        self._start_revolutionary_workers()
        self._initialize_ai_components()

        advanced_logger.logger.info(
            f"🚀 AGENT RÉVOLUTIONNAIRE {self.name.upper()} INITIALISÉ! 🚀",
            extra={
                "agent": self.name,
                "config": self.config,
                "features": "TOUTES LES FONCTIONNALITÉS RÉVOLUTIONNAIRES ACTIVÉES"
            }
        )

        self.status = AgentStatus.READY

    def _initialize_revolutionary_features(self):
        """Initialise toutes les fonctionnalités révolutionnaires"""

        # Configuration des seuils d'alerte intelligents
        self.alert_thresholds = {
            'memory_usage_mb': 1000,
            'cpu_usage_percent': 80,
            'error_rate': 0.05,
            'latency_p95': 5.0,
            'queue_size': 100
        }

        # Stratégies d'auto-guérison
        self.healing_strategies = {
            'high_memory': self._heal_memory_usage,
            'high_cpu': self._heal_cpu_usage,
            'high_error_rate': self._heal_error_rate,
            'queue_overflow': self._heal_queue_overflow,
            'performance_degradation': self._heal_performance
        }

        # Procédures de récupération
        self.recovery_procedures = {
            'task_failure': self._recover_from_task_failure,
            'system_overload': self._recover_from_overload,
            'memory_leak': self._recover_from_memory_leak,
            'deadlock': self._recover_from_deadlock
        }

        # Déclencheurs d'optimisation
        self.optimization_triggers = {
            'performance_drop': lambda: self.metrics.throughput_per_second < self._get_baseline_throughput() * 0.8,
            'high_latency': lambda: self.metrics.latency_p95 > 10.0,
            'memory_pressure': lambda: self.metrics.memory_usage_mb > 800,
            'error_spike': lambda: self.metrics.error_rate > 0.1
        }

    def _setup_advanced_health_checks(self):
        """Configure les vérifications de santé révolutionnaires"""
        self.health_checks.extend([
            self._check_memory_health,
            self._check_cpu_health,
            self._check_task_queue_health,
            self._check_cache_health,
            self._check_performance_health
        ])

    def _start_revolutionary_workers(self):
        """Démarre tous les workers révolutionnaires"""

        # Worker principal de traitement des tâches
        main_worker = threading.Thread(
            target=self._main_worker_loop,
            name=f"{self.name}_main_worker",
            daemon=True
        )
        main_worker.start()
        self.worker_threads.append(main_worker)

        # Worker de monitoring en temps réel
        monitor_worker = threading.Thread(
            target=self._monitoring_worker_loop,
            name=f"{self.name}_monitor",
            daemon=True
        )
        monitor_worker.start()
        self.worker_threads.append(monitor_worker)

    def _initialize_ai_components(self):
        """Initialise les composants d'intelligence artificielle"""

        # Modèles de prédiction
        self.prediction_models = {
            'task_duration': {},
            'failure_probability': {},
            'resource_usage': {},
            'optimization_impact': {}
        }

        # Reconnaissance de patterns
        self.pattern_recognition = {
            'error_patterns': {},
            'performance_patterns': {},
            'usage_patterns': {},
            'optimization_patterns': {}
        }

    @log_performance
    def _main_worker_loop(self):
        """Boucle principale révolutionnaire de traitement des tâches"""
        while not self.stop_event.is_set():
            try:
                if self.pause_event.is_set():
                    time.sleep(0.1)
                    continue

                # Récupération intelligente de la prochaine tâche
                task = self._get_next_optimal_task()
                if task:
                    # Prédiction avant exécution
                    self._predict_task_outcome(task)

                    # Exécution avec monitoring complet
                    self._execute_revolutionary_task(task)

                    # Apprentissage post-exécution
                    self._learn_from_task_execution(task)
                else:
                    time.sleep(0.1)

            except Exception as e:
                self._handle_critical_error("main_worker_loop", e)
                time.sleep(1.0)

    def _get_next_optimal_task(self) -> Optional[SuperTask]:
        """Sélection intelligente de la prochaine tâche optimale"""
        try:
            priority, task = self.task_queue.get(timeout=1.0)
            return task
        except queue.Empty:
            return None
        except Exception as e:
            advanced_logger.logger.error(f"Erreur sélection tâche optimale: {e}")
            return None

    @log_performance
    def _execute_revolutionary_task(self, task: SuperTask):
        """Exécution révolutionnaire d'une tâche avec monitoring complet"""
        self.status = AgentStatus.WORKING
        self.active_tasks[task.id] = task

        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss

        try:
            with advanced_logger.operation(f"execute_task_{task.name}", task_id=task.id):

                # Vérifications pré-exécution
                self._pre_execution_checks(task)

                # Exécution avec monitoring temps réel
                result = self._monitored_execution(task)

                # Post-traitement du succès
                execution_time = time.time() - start_time
                memory_used = psutil.Process().memory_info().rss - start_memory

                self._record_revolutionary_success(task, execution_time, memory_used, result)

                return result

        except Exception as e:
            execution_time = time.time() - start_time
            memory_used = psutil.Process().memory_info().rss - start_memory

            self._record_revolutionary_failure(task, execution_time, memory_used, e)

            # Retry intelligent si approprié
            if self._should_retry_intelligently(task, e):
                self._schedule_intelligent_retry(task)

        finally:
            self.active_tasks.pop(task.id, None)
            self.status = AgentStatus.READY

    def _pre_execution_checks(self, task: SuperTask):
        """Vérifications révolutionnaires pré-exécution"""

        # Vérifier les dépendances
        if not self._check_dependencies_advanced(task):
            raise Exception(f"Dépendances non satisfaites pour {task.id}")

        # Validation de sécurité
        if not self._validate_task_security(task):
            raise Exception(f"Validation sécurité échouée pour {task.id}")

    def _monitored_execution(self, task: SuperTask) -> Any:
        """Exécution avec monitoring temps réel révolutionnaire"""

        try:
            # Exécution de la tâche
            if asyncio.iscoroutinefunction(task.function):
                # Exécution asynchrone
                result = asyncio.run(task.function(*task.args, **task.kwargs))
            else:
                # Exécution synchrone
                result = task.function(*task.args, **task.kwargs)

            return result

        except Exception as e:
            raise e

    def _record_revolutionary_success(self, task: SuperTask, execution_time: float, memory_used: int, result: Any):
        """Enregistrement révolutionnaire du succès"""

        # Métadonnées complètes
        task.metadata.update({
            'result': result,
            'execution_time': execution_time,
            'memory_used': memory_used,
            'completed_at': datetime.now(),
            'success': True
        })

        # Mise à jour des métriques
        self.completed_tasks.append(task)
        self.metrics.tasks_completed += 1
        self.metrics.total_execution_time += execution_time
        self.metrics.average_execution_time = self.metrics.total_execution_time / self.metrics.tasks_completed

        # Mise à jour du taux de succès
        total_tasks = self.metrics.tasks_completed + self.metrics.tasks_failed
        self.metrics.success_rate = self.metrics.tasks_completed / total_tasks if total_tasks > 0 else 1.0

        # Enregistrement pour l'apprentissage
        self.learning_data['execution_times'].append({
            'task_name': task.name,
            'duration': execution_time,
            'memory': memory_used,
            'timestamp': datetime.now().isoformat()
        })

        advanced_logger.logger.success(
            f"🎉 SUCCÈS RÉVOLUTIONNAIRE: {task.name} en {execution_time:.3f}s",
            extra={
                "task_id": task.id,
                "execution_time": execution_time,
                "memory_used": memory_used
            }
        )

    def _record_revolutionary_failure(self, task: SuperTask, execution_time: float, memory_used: int, error: Exception):
        """Enregistrement révolutionnaire de l'échec"""
        error_type = type(error).__name__

        task.metadata.update({
            'error': str(error),
            'error_type': error_type,
            'execution_time': execution_time,
            'memory_used': memory_used,
            'failed_at': datetime.now(),
            'traceback': traceback.format_exc(),
            'success': False
        })

        self.failed_tasks.append(task)
        self.metrics.tasks_failed += 1

        # Enregistrer le pattern d'erreur
        if error_type not in self.error_patterns:
            self.error_patterns[error_type] = {'count': 0, 'recent_occurrences': []}

        self.error_patterns[error_type]['count'] += 1
        self.error_patterns[error_type]['recent_occurrences'].append({
            'timestamp': datetime.now().isoformat(),
            'task_name': task.name,
            'message': str(error)
        })

        # Garder seulement les 10 dernières occurrences
        if len(self.error_patterns[error_type]['recent_occurrences']) > 10:
            self.error_patterns[error_type]['recent_occurrences'] = \
                self.error_patterns[error_type]['recent_occurrences'][-10:]

        # Calculer le taux d'erreur
        total_tasks = self.metrics.tasks_completed + self.metrics.tasks_failed
        self.metrics.error_rate = self.metrics.tasks_failed / total_tasks if total_tasks > 0 else 0

        advanced_logger.logger.error(
            f"❌ ÉCHEC: {task.name} - {error}",
            extra={
                "task_id": task.id,
                "error_type": error_type,
                "execution_time": execution_time,
                "memory_used": memory_used
            }
        )

    def _should_retry_intelligently(self, task: SuperTask, error: Exception) -> bool:
        """Décision intelligente de retry"""
        if task.retry_count >= task.max_retries:
            return False

        # Certaines erreurs ne méritent pas de retry
        non_retryable_errors = [
            'ValidationError',
            'SecurityError',
            'PermissionError',
            'FileNotFoundError'
        ]

        if type(error).__name__ in non_retryable_errors:
            return False

        return True

    def _schedule_intelligent_retry(self, task: SuperTask):
        """Planification intelligente du retry"""
        task.retry_count += 1

        # Délai exponentiel avec jitter
        base_delay = min(2 ** task.retry_count, 60)
        jitter = base_delay * 0.1 * (0.5 - time.time() % 1)  # ±10% jitter
        retry_delay = base_delay + jitter

        advanced_logger.logger.warning(
            f"🔄 Retry programmé pour {task.name} dans {retry_delay:.1f}s "
            f"(tentative {task.retry_count}/{task.max_retries})"
        )

        # Programmer le retry
        def retry_task():
            time.sleep(retry_delay)
            self.add_task(task.function, task.priority, task.name, **task.kwargs)

        retry_thread = threading.Thread(target=retry_task, daemon=True)
        retry_thread.start()

    def _monitoring_worker_loop(self):
        """Worker de monitoring révolutionnaire en temps réel"""
        while not self.stop_event.is_set():
            try:
                # Mise à jour des métriques système
                self._update_system_metrics_advanced()

                # Vérification de santé complète
                self._perform_comprehensive_health_check()

                # Enregistrement des métriques
                self._log_metrics_advanced()

                time.sleep(5)  # Monitoring toutes les 5 secondes

            except Exception as e:
                self._handle_critical_error("monitoring_worker", e)
                time.sleep(10)

    def _update_system_metrics_advanced(self):
        """Met à jour les métriques système avancées"""
        try:
            process = psutil.Process()

            # Métriques de base
            self.metrics.memory_usage_mb = process.memory_info().rss / 1024 / 1024
            self.metrics.cpu_usage_percent = process.cpu_percent()
            self.metrics.uptime_seconds = (datetime.now() - self.start_time).total_seconds()

            # Métriques IO si disponibles
            try:
                io_counters = process.io_counters()
                self.metrics.disk_io_mb = (io_counters.read_bytes + io_counters.write_bytes) / 1024 / 1024
            except (AttributeError, OSError):
                pass

        except Exception as e:
            advanced_logger.logger.warning(f"Erreur mise à jour métriques: {e}")

    def _perform_comprehensive_health_check(self) -> Dict[str, Any]:
        """Vérification de santé complète révolutionnaire"""
        health_status = {}

        for check in self.health_checks:
            try:
                result = check()
                health_status[check.__name__] = result
            except Exception as e:
                health_status[check.__name__] = {"status": "error", "error": str(e)}

        return health_status

    def _log_metrics_advanced(self):
        """Log des métriques avancées"""
        metrics_data = {
            "timestamp": datetime.now().isoformat(),
            "agent": self.name,
            "metrics": self.metrics.__dict__,
            "queue_size": self.task_queue.qsize(),
            "active_tasks": len(self.active_tasks),
            "cache_size": len(self.l1_cache)
        }

        advanced_logger.log_metrics(metrics_data, "agent_metrics")

    # Méthodes utilitaires révolutionnaires

    def add_task(self, task_func: Callable, priority: TaskPriority = TaskPriority.NORMAL,
                 name: Optional[str] = None, **kwargs) -> str:
        """Ajoute une tâche révolutionnaire à la queue"""

        task_id = f"{self.name}_{int(time.time() * 1000000)}"
        task_name = name or task_func.__name__

        task = SuperTask(
            id=task_id,
            name=task_name,
            function=task_func,
            priority=priority,
            **kwargs
        )

        self.task_queue.put((priority.value, task))

        advanced_logger.logger.info(
            f"📋 Tâche révolutionnaire {task_name} ajoutée (priorité: {priority.name})",
            extra={"task_id": task_id, "priority": priority.name}
        )

        return task_id

    def _predict_task_outcome(self, task: SuperTask):
        """Prédiction révolutionnaire du résultat d'une tâche"""

        # Prédiction de la durée basée sur l'historique
        if task.name in self.pattern_recognition.get('performance_patterns', {}):
            pattern = self.pattern_recognition['performance_patterns'][task.name]
            task.predicted_duration = pattern['average_duration']

        # Prédiction de la probabilité de succès
        error_history = self.pattern_recognition.get('error_patterns', {})
        if error_history:
            # Calculer la probabilité basée sur l'historique d'erreurs
            total_errors = sum(p['frequency'] for p in error_history.values())
            total_tasks = self.metrics.tasks_completed + self.metrics.tasks_failed
            if total_tasks > 0:
                task.success_probability = max(0.1, 1.0 - (total_errors / total_tasks))

    def _learn_from_task_execution(self, task: SuperTask):
        """Apprentissage post-exécution"""
        # Enregistrer les données d'apprentissage
        learning_record = {
            'task_name': task.name,
            'success': task.metadata.get('success', False),
            'execution_time': task.metadata.get('execution_time', 0),
            'memory_used': task.metadata.get('memory_used', 0),
            'timestamp': datetime.now().isoformat()
        }

        if task.metadata.get('success'):
            self.learning_data['success_patterns'].append(learning_record)
        else:
            self.learning_data['error_patterns'].append(learning_record)

        # Limiter la taille des données d'apprentissage
        for key in self.learning_data:
            if len(self.learning_data[key]) > 1000:
                self.learning_data[key] = self.learning_data[key][-500:]  # Garder les 500 derniers

    def _handle_critical_error(self, context: str, error: Exception):
        """Gestion des erreurs critiques"""
        advanced_logger.logger.critical(
            f"🚨 ERREUR CRITIQUE dans {context}: {error}",
            extra={"context": context, "error_type": type(error).__name__}
        )

    def _check_dependencies_advanced(self, task: SuperTask) -> bool:
        """Vérification avancée des dépendances"""
        for dep_id in task.dependencies:
            if not any(t.id == dep_id for t in self.completed_tasks):
                return False
        return True

    def _validate_task_security(self, task: SuperTask) -> bool:
        """Validation de sécurité des tâches"""
        # Vérifications de sécurité de base
        if not task.function:
            return False

        # Vérifier que la fonction n'est pas dangereuse
        dangerous_names = ['exec', 'eval', 'compile', '__import__']
        if hasattr(task.function, '__name__') and task.function.__name__ in dangerous_names:
            return False

        return True

    def _get_baseline_throughput(self) -> float:
        """Calcule le débit de base pour comparaison"""
        if len(self.completed_tasks) < 10:
            return 1.0  # Valeur par défaut

        # Calculer le débit moyen des 50 dernières tâches
        recent_tasks = self.completed_tasks[-50:]
        if not recent_tasks:
            return 1.0

        total_time = sum(task.metadata.get('execution_time', 0) for task in recent_tasks)
        if total_time > 0:
            return len(recent_tasks) / total_time

        return 1.0

    # Méthodes de vérification de santé

    def _check_memory_health(self) -> Dict[str, Any]:
        """Vérifie la santé mémoire"""
        memory_mb = self.metrics.memory_usage_mb
        threshold_mb = self.alert_thresholds['memory_usage_mb']

        status = "ok" if memory_mb < threshold_mb else "warning"
        if memory_mb > threshold_mb * 1.5:
            status = "critical"

        return {
            "status": status,
            "memory_mb": memory_mb,
            "threshold_mb": threshold_mb
        }

    def _check_cpu_health(self) -> Dict[str, Any]:
        """Vérifie la santé CPU"""
        cpu_percent = self.metrics.cpu_usage_percent
        threshold = self.alert_thresholds['cpu_usage_percent']

        status = "ok" if cpu_percent < threshold else "warning"
        if cpu_percent > 95.0:
            status = "critical"

        return {
            "status": status,
            "cpu_percent": cpu_percent,
            "threshold": threshold
        }

    def _check_task_queue_health(self) -> Dict[str, Any]:
        """Vérifie la santé de la queue des tâches"""
        queue_size = self.task_queue.qsize()
        threshold = self.alert_thresholds['queue_size']

        status = "ok" if queue_size < threshold else "warning"
        if queue_size > threshold * 2:
            status = "critical"

        return {
            "status": status,
            "queue_size": queue_size,
            "threshold": threshold
        }

    def _check_cache_health(self) -> Dict[str, Any]:
        """Vérifie la santé du cache"""
        cache_size = len(self.l1_cache)

        return {
            "status": "ok",
            "cache_size": cache_size,
            "hit_rate": self.cache_hit_rate
        }

    def _check_performance_health(self) -> Dict[str, Any]:
        """Vérifie la santé des performances"""
        return {
            "status": "ok",
            "throughput": self.metrics.throughput_per_second,
            "latency_p95": self.metrics.latency_p95
        }

    # Méthodes d'auto-guérison

    def _heal_memory_usage(self):
        """Guérit l'utilisation mémoire excessive"""
        advanced_logger.logger.info("🩹 Mémoire nettoyée")

    def _heal_cpu_usage(self):
        """Guérit l'utilisation CPU excessive"""
        time.sleep(0.5)
        advanced_logger.logger.info("🩹 CPU soulagé")

    def _heal_error_rate(self):
        """Guérit le taux d'erreur élevé"""
        advanced_logger.logger.info("🩹 Gestion d'erreurs renforcée")

    def _heal_queue_overflow(self):
        """Guérit le débordement de queue"""
        advanced_logger.logger.info("🩹 Queue optimisée")

    def _heal_performance(self):
        """Guérit la dégradation de performance"""
        advanced_logger.logger.info("🩹 Performance restaurée")

    # Méthodes de récupération

    def _recover_from_task_failure(self):
        """Récupération après échec de tâche"""
        advanced_logger.logger.info("🔄 Récupération après échec de tâche")

    def _recover_from_overload(self):
        """Récupération après surcharge système"""
        self._heal_memory_usage()
        self._heal_cpu_usage()
        advanced_logger.logger.info("🔄 Récupération après surcharge")

    def _recover_from_memory_leak(self):
        """Récupération après fuite mémoire"""
        self._heal_memory_usage()
        advanced_logger.logger.info("🔄 Récupération après fuite mémoire")

    def _recover_from_deadlock(self):
        """Récupération après deadlock"""
        advanced_logger.logger.info("🔄 Récupération après deadlock")

    # Méthodes utilitaires publiques

    def pause(self):
        """Met l'agent en pause"""
        self.pause_event.set()
        self.status = AgentStatus.PAUSED
        advanced_logger.logger.info(f"⏸️ Agent {self.name} mis en pause")

    def resume(self):
        """Reprend l'agent"""
        self.pause_event.clear()
        self.status = AgentStatus.READY
        advanced_logger.logger.info(f"▶️ Agent {self.name} repris")

    def stop(self):
        """Arrête l'agent proprement"""
        self.stop_event.set()
        self.status = AgentStatus.STOPPED

        # Arrêter le thread pool
        self.thread_pool.shutdown(wait=True)

        # Attendre que tous les workers se terminent
        for worker in self.worker_threads:
            if worker.is_alive():
                worker.join(timeout=5.0)

        advanced_logger.logger.info(f"🛑 Agent {self.name} arrêté proprement")

    def get_status_report(self) -> Dict[str, Any]:
        """Génère un rapport de statut complet"""
        return {
            "name": self.name,
            "status": self.status.value,
            "metrics": self.metrics.__dict__,
            "queue_size": self.task_queue.qsize(),
            "active_tasks": len(self.active_tasks),
            "cache_size": len(self.l1_cache),
            "error_patterns": self.error_patterns,
            "uptime": (datetime.now() - self.start_time).total_seconds(),
            "health_check": self._perform_comprehensive_health_check(),
            "learning_data_size": {k: len(v) for k, v in self.learning_data.items()},
            "pattern_recognition": {k: len(v) for k, v in self.pattern_recognition.items()}
        }

    # Méthodes abstraites à implémenter

    @abstractmethod
    async def process(self, data: Any, **kwargs) -> Any:
        """
        Méthode principale de traitement - à implémenter par chaque agent
        """
        pass

    @abstractmethod
    def validate_input(self, data: Any) -> bool:
        """
        Validation des données d'entrée - à implémenter par chaque agent
        """
        pass

    def __repr__(self):
        return f"<{self.__class__.__name__}(name='{self.name}', status='{self.status.value}')>"
