"""
NovaSpace Constellation Demo

Demonstrates forming hyperspace constellations using current
LinkHealth + emotional loyalty modulation (from Solnet + Lyra state).

Run from repo root after `pip install -e .` :
  python examples/constellation_demo.py

Or directly (dev):
  PYTHONPATH=src python examples/constellation_demo.py
"""

import sys
from pathlib import Path

# Allow running directly from examples/ without install
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from novaspace.hyperspace import HyperspaceLink, resonate


def main():
    hs = HyperspaceLink(local_id="sven-nova-prime")
    
    # Simulate current state from mesh + emotional layers (June 2026)
    hs.add_or_update_link("orion-alpha", health_score=0.92, latency_ms=85, loyalty=0.88, bandwidth_mbps=25)
    hs.add_or_update_link("lyra-node-3", health_score=0.78, latency_ms=210, loyalty=0.71, bandwidth_mbps=8)
    hs.add_or_update_link("solnet-relay-7", health_score=0.95, latency_ms=45, loyalty=0.65, bandwidth_mbps=40)
    hs.add_or_update_link("qnet-edge", health_score=0.55, latency_ms=380, loyalty=0.42, bandwidth_mbps=3)
    
    print("Healthy peers:", hs.get_healthy_peers())
    
    # Form a resonant constellation from current state
    const = hs.form_constellation("nova-prime-1", ["orion-alpha", "lyra-node-3", "solnet-relay-7"])
    print(f"Formed {const.name} with resonance {const.resonance:.2f}")
    
    for p in const.members:
        r = hs.resonate(p)
        print(f"  Resonate with {p}: {r:.3f}")
    
    print("Module-level resonate example:", resonate("core", "peer", 0.9, 0.8))


if __name__ == "__main__":
    main()
