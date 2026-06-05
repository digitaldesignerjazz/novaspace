"""
NovaSpace Hyperspace Layer

Resonant hyperspace peering, constellation formation, and space-scale
coordination primitives for the NovaNet / xMesh / QNET ecosystem.

Current state integration (June 2026):
- Leverages Solnet LinkHealthScorer for link quality
- Modulated by LyraEmotionalStateMachine (energy, fatigue, loyalty)
- Orion-net resonant routing for constellation decisions
- Part of Nexus unified orchestration
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class LinkState:
    """Current hyperspace link metrics (current state snapshot)."""
    peer_id: str
    latency_ms: float = 120.0
    health_score: float = 0.85  # from LinkHealthScorer EWMA etc.
    bandwidth_mbps: float = 12.5
    flap_count: int = 0
    last_seen: float = field(default_factory=time.time)
    loyalty: float = 0.6  # from emotional layer


@dataclass
class Constellation:
    """A resonant group of nodes/agents in 'space'."""
    name: str
    members: List[str] = field(default_factory=list)
    resonance: float = 0.75
    center: Optional[str] = None
    created: float = field(default_factory=time.time)


class HyperspaceLink:
    """Core hyperspace link abstraction for NovaSpace."""

    def __init__(self, local_id: str = "novaspace-core"):
        self.local_id = local_id
        self.links: Dict[str, LinkState] = {}
        self.constellations: Dict[str, Constellation] = {}

    def add_or_update_link(self, peer_id: str, **metrics) -> LinkState:
        if peer_id not in self.links:
            self.links[peer_id] = LinkState(peer_id=peer_id)
        link = self.links[peer_id]
        for k, v in metrics.items():
            if hasattr(link, k):
                setattr(link, k, v)
        link.last_seen = time.time()
        return link

    def get_healthy_peers(self, min_health: float = 0.7) -> List[str]:
        return [pid for pid, ln in self.links.items() if ln.health_score >= min_health]

    def form_constellation(self, name: str, peers: List[str], base_resonance: float = 0.8) -> Constellation:
        """Form or update a constellation using current link + emotional resonance."""
        avg_loyalty = sum(self.links.get(p, LinkState(p)).loyalty for p in peers) / max(1, len(peers))
        resonance = min(0.98, base_resonance * (0.6 + 0.4 * avg_loyalty))
        const = Constellation(name=name, members=peers[:], resonance=resonance, center=self.local_id)
        self.constellations[name] = const
        return const

    def resonate(self, peer_id: str, intensity: float = 1.0) -> float:
        """Compute resonant score for a peer (current state model)."""
        if peer_id not in self.links:
            return 0.3
        ln = self.links[peer_id]
        # Simple model blending health + loyalty (in real: call into Lyra + Solnet scorer)
        score = (ln.health_score * 0.55 + ln.loyalty * 0.45) * intensity
        return max(0.1, min(0.98, score))


def resonate(local: str, remote: str, health: float, loyalty: float) -> float:
    """Module level helper representing current resonant decision primitive."""
    return max(0.1, min(0.98, health * 0.6 + loyalty * 0.4))
