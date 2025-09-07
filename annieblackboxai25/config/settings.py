"""
Configuration settings for the Multi-Agent System
Gestion robuste des configurations avec validation
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional, Dict, Any
import os
from pathlib import Path

class AgentSettings(BaseSettings):
    """Configuration principale du système d'agents"""
    
    # Chemins de base
    BASE_DIR: Path = Field(default_factory=lambda: Path(__file__).parent.parent)
    DATA_DIR: Path = Field(default_factory=lambda: Path(__file__).parent.parent / "data")
    LOGS_DIR: Path = Field(default_factory=lambda: Path(__file__).parent.parent / "logs")
    
    # Configuration des agents
    MAX_RETRIES: int = Field(default=3, description="Nombre maximum de tentatives")
    TIMEOUT_SECONDS: int = Field(default=30, description="Timeout en secondes")
    
    # Configuration du navigateur
    BROWSER_HEADLESS: bool = Field(default=True, description="Mode headless pour le navigateur")
    BROWSER_TIMEOUT: int = Field(default=10, description="Timeout du navigateur")
    USER_AGENT: str = Field(
        default="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        description="User agent pour les requêtes web"
    )
    
    # Configuration des données
    MAX_FILE_SIZE_MB: int = Field(default=100, description="Taille maximale des fichiers en MB")
    SUPPORTED_FORMATS: list = Field(
        default=["csv", "xlsx", "xls", "json", "xml"],
        description="Formats de fichiers supportés"
    )
    
    # Configuration de la recherche
    SEARCH_DELAY_SECONDS: float = Field(default=1.0, description="Délai entre les recherches")
    MAX_SEARCH_RESULTS: int = Field(default=50, description="Nombre maximum de résultats de recherche")
    
    # Configuration du logging
    LOG_LEVEL: str = Field(default="INFO", description="Niveau de logging")
    LOG_ROTATION: str = Field(default="1 day", description="Rotation des logs")
    LOG_RETENTION: str = Field(default="30 days", description="Rétention des logs")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Créer les répertoires nécessaires
        self.DATA_DIR.mkdir(exist_ok=True)
        self.LOGS_DIR.mkdir(exist_ok=True)

# Instance globale des paramètres
settings = AgentSettings()

# Configuration des agents spécifiques
AGENT_CONFIGS = {
    "spreadsheet": {
        "chunk_size": 10000,
        "memory_limit_mb": 500,
        "auto_save": True,
        "backup_enabled": True
    },
    "browser": {
        "implicit_wait": 10,
        "page_load_timeout": 30,
        "script_timeout": 30,
        "download_timeout": 60
    },
    "analyzer": {
        "max_correlation_features": 100,
        "significance_level": 0.05,
        "min_sample_size": 30
    },
    "controller": {
        "max_concurrent_tasks": 5,
        "task_timeout": 300,
        "health_check_interval": 60
    },
    "research": {
        "cache_duration_hours": 24,
        "max_depth": 3,
        "content_similarity_threshold": 0.8
    }
}

def get_agent_config(agent_name: str) -> Dict[str, Any]:
    """Récupère la configuration d'un agent spécifique"""
    return AGENT_CONFIGS.get(agent_name, {})

def validate_file_path(file_path: str) -> bool:
    """Valide qu'un chemin de fichier est sûr et accessible"""
    try:
        path = Path(file_path)
        # Vérifier que le chemin est dans les limites autorisées
        resolved_path = path.resolve()
        base_path = settings.BASE_DIR.resolve()
        
        return str(resolved_path).startswith(str(base_path))
    except Exception:
        return False

def get_safe_filename(filename: str) -> str:
    """Génère un nom de fichier sûr"""
    import re
    # Supprimer les caractères dangereux
    safe_name = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Limiter la longueur
    if len(safe_name) > 200:
        name, ext = os.path.splitext(safe_name)
        safe_name = name[:200-len(ext)] + ext
    return safe_name
