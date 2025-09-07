"""
Système de logging avancé pour le Multi-Agent System
Le meilleur système de logging du marché avec traçabilité complète
"""

import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, Union
from loguru import logger
import traceback
import functools
import time
import psutil
import threading
from contextlib import contextmanager

class AdvancedLogger:
    """
    Système de logging révolutionnaire avec:
    - Traçabilité complète des opérations
    - Métriques de performance en temps réel
    - Détection automatique d'anomalies
    - Corrélation des événements
    - Alertes intelligentes
    """
    
    def __init__(self, name: str = "MultiAgentSystem"):
        self.name = name
        self.start_time = datetime.now()
        self.operation_stack = []
        self.performance_metrics = {}
        self.error_patterns = {}
        self.success_patterns = {}
        
        # Configuration du logger principal
        logger.remove()  # Supprimer le handler par défaut
        
        # Console avec couleurs et formatage avancé
        logger.add(
            sys.stdout,
            format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                   "<level>{level: <8}</level> | "
                   "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
                   "<level>{message}</level>",
            level="DEBUG",
            colorize=True,
            backtrace=True,
            diagnose=True
        )
        
        # Fichier de logs avec rotation intelligente
        log_path = Path("logs") / f"{name}_{datetime.now().strftime('%Y%m%d')}.log"
        log_path.parent.mkdir(exist_ok=True)
        
        logger.add(
            str(log_path),
            format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} | {message}",
            level="INFO",
            rotation="100 MB",
            retention="30 days",
            compression="zip",
            backtrace=True,
            diagnose=True,
            enqueue=True  # Thread-safe
        )
        
        # Fichier d'erreurs critique
        error_path = Path("logs") / f"{name}_errors_{datetime.now().strftime('%Y%m%d')}.log"
        logger.add(
            str(error_path),
            format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} | {message} | {extra}",
            level="ERROR",
            rotation="50 MB",
            retention="90 days",
            compression="zip",
            backtrace=True,
            diagnose=True,
            enqueue=True
        )
        
        # Fichier de métriques JSON
        metrics_path = Path("logs") / f"{name}_metrics_{datetime.now().strftime('%Y%m%d')}.jsonl"
        logger.add(
            str(metrics_path),
            format="{message}",
            level="INFO",
            filter=lambda record: record["extra"].get("type") == "metrics",
            rotation="10 MB",
            retention="7 days",
            enqueue=True
        )
        
        self.logger = logger.bind(name=name)
        self._log_system_info()
    
    def _log_system_info(self):
        """Log des informations système au démarrage"""
        system_info = {
            "timestamp": datetime.now().isoformat(),
            "system": {
                "cpu_count": psutil.cpu_count(),
                "memory_total": psutil.virtual_memory().total,
                "disk_usage": psutil.disk_usage('/').total,
                "python_version": sys.version,
                "platform": sys.platform
            },
            "process": {
                "pid": psutil.Process().pid,
                "memory_percent": psutil.Process().memory_percent(),
                "cpu_percent": psutil.Process().cpu_percent()
            }
        }
        
        self.logger.info("Système initialisé", extra={"type": "system_info", "data": system_info})
    
    @contextmanager
    def operation(self, operation_name: str, **context):
        """
        Context manager pour tracer les opérations avec métriques automatiques
        """
        operation_id = f"{operation_name}_{int(time.time() * 1000)}"
        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss
        
        self.operation_stack.append(operation_id)
        
        self.logger.info(
            f"🚀 Début opération: {operation_name}",
            extra={
                "type": "operation_start",
                "operation_id": operation_id,
                "operation_name": operation_name,
                "context": context,
                "stack_depth": len(self.operation_stack)
            }
        )
        
        try:
            yield operation_id
            
            # Succès
            duration = time.time() - start_time
            memory_used = psutil.Process().memory_info().rss - start_memory
            
            self._record_success_pattern(operation_name, duration)
            
            self.logger.success(
                f"✅ Opération réussie: {operation_name} ({duration:.3f}s)",
                extra={
                    "type": "operation_success",
                    "operation_id": operation_id,
                    "operation_name": operation_name,
                    "duration": duration,
                    "memory_used": memory_used,
                    "context": context
                }
            )
            
        except Exception as e:
            # Échec
            duration = time.time() - start_time
            error_info = {
                "type": type(e).__name__,
                "message": str(e),
                "traceback": traceback.format_exc()
            }
            
            self._record_error_pattern(operation_name, error_info)
            
            self.logger.error(
                f"❌ Échec opération: {operation_name} ({duration:.3f}s) - {str(e)}",
                extra={
                    "type": "operation_error",
                    "operation_id": operation_id,
                    "operation_name": operation_name,
                    "duration": duration,
                    "error": error_info,
                    "context": context
                }
            )
            raise
            
        finally:
            self.operation_stack.pop()
    
    def _record_success_pattern(self, operation: str, duration: float):
        """Enregistre les patterns de succès pour l'optimisation"""
        if operation not in self.success_patterns:
            self.success_patterns[operation] = {
                "count": 0,
                "total_duration": 0,
                "min_duration": float('inf'),
                "max_duration": 0
            }
        
        pattern = self.success_patterns[operation]
        pattern["count"] += 1
        pattern["total_duration"] += duration
        pattern["min_duration"] = min(pattern["min_duration"], duration)
        pattern["max_duration"] = max(pattern["max_duration"], duration)
    
    def _record_error_pattern(self, operation: str, error_info: Dict):
        """Enregistre les patterns d'erreur pour la prévention"""
        if operation not in self.error_patterns:
            self.error_patterns[operation] = {}
        
        error_type = error_info["type"]
        if error_type not in self.error_patterns[operation]:
            self.error_patterns[operation][error_type] = {
                "count": 0,
                "last_occurrence": None,
                "messages": []
            }
        
        pattern = self.error_patterns[operation][error_type]
        pattern["count"] += 1
        pattern["last_occurrence"] = datetime.now().isoformat()
        pattern["messages"].append(error_info["message"])
        
        # Garder seulement les 10 derniers messages
        if len(pattern["messages"]) > 10:
            pattern["messages"] = pattern["messages"][-10:]
    
    def log_metrics(self, metrics: Dict[str, Any], category: str = "general"):
        """Log des métriques structurées"""
        metrics_data = {
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "metrics": metrics,
            "system": {
                "cpu_percent": psutil.cpu_percent(),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage('/').percent
            }
        }
        
        self.logger.info(
            json.dumps(metrics_data),
            extra={"type": "metrics"}
        )
    
    def get_performance_report(self) -> Dict[str, Any]:
        """Génère un rapport de performance complet"""
        uptime = (datetime.now() - self.start_time).total_seconds()
        
        report = {
            "uptime_seconds": uptime,
            "success_patterns": self.success_patterns,
            "error_patterns": self.error_patterns,
            "system_health": {
                "cpu_percent": psutil.cpu_percent(),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage('/').percent
            }
        }
        
        return report
    
    def auto_optimize_suggestions(self) -> list:
        """Suggestions d'optimisation automatiques basées sur les patterns"""
        suggestions = []
        
        # Analyser les opérations lentes
        for operation, pattern in self.success_patterns.items():
            if pattern["count"] > 5:
                avg_duration = pattern["total_duration"] / pattern["count"]
                if avg_duration > 5.0:  # Plus de 5 secondes en moyenne
                    suggestions.append({
                        "type": "performance",
                        "operation": operation,
                        "issue": f"Opération lente (moyenne: {avg_duration:.2f}s)",
                        "suggestion": "Considérer l'optimisation ou la parallélisation"
                    })
        
        # Analyser les erreurs récurrentes
        for operation, errors in self.error_patterns.items():
            for error_type, pattern in errors.items():
                if pattern["count"] > 3:
                    suggestions.append({
                        "type": "reliability",
                        "operation": operation,
                        "error_type": error_type,
                        "count": pattern["count"],
                        "suggestion": "Ajouter une gestion d'erreur spécifique ou un retry"
                    })
        
        return suggestions

# Instance globale du logger
advanced_logger = AdvancedLogger()

def log_performance(func):
    """Décorateur pour logger automatiquement les performances des fonctions"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with advanced_logger.operation(f"{func.__module__}.{func.__name__}", args=len(args), kwargs=list(kwargs.keys())):
            return func(*args, **kwargs)
    return wrapper

def log_errors(func):
    """Décorateur pour logger automatiquement les erreurs avec contexte"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            advanced_logger.logger.error(
                f"Erreur dans {func.__name__}: {str(e)}",
                extra={
                    "function": func.__name__,
                    "module": func.__module__,
                    "args": str(args)[:200],  # Limiter la taille
                    "kwargs": str(kwargs)[:200],
                    "error_type": type(e).__name__
                }
            )
            raise
    return wrapper

# Fonctions utilitaires
def log_info(message: str, **extra):
    """Log d'information avec contexte"""
    advanced_logger.logger.info(message, extra=extra)

def log_warning(message: str, **extra):
    """Log d'avertissement avec contexte"""
    advanced_logger.logger.warning(message, extra=extra)

def log_error(message: str, **extra):
    """Log d'erreur avec contexte"""
    advanced_logger.logger.error(message, extra=extra)

def log_success(message: str, **extra):
    """Log de succès avec contexte"""
    advanced_logger.logger.success(message, extra=extra)
