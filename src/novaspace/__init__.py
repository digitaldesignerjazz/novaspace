"""
NovaSpace
=========

Hyperspace and NovaNet constellation coordination layer.

Part of the Nexus / Esslinger & Co. sovereign decentralized infrastructure vision (2026).

Provides long-range resonant networking, space-scale peering, and coordination
for AI agent swarms across the stars (or at least the planet-scale mesh).
"""

__version__ = "0.1.0"

from .hyperspace import HyperspaceLink, resonate

__all__ = ["HyperspaceLink", "resonate", "__version__"]
