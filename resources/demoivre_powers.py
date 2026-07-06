#!/usr/bin/env python3
"""
Generate a diagram showing De Moivre's theorem: powers of a complex number.
Outputs to demoivre-powers.png in the same directory.
"""

import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(10, 10), dpi=150)
ax.set_aspect('equal')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.axhline(y=0, color='k', linewidth=1.5)
ax.axvline(x=0, color='k', linewidth=1.5)

# Add axis labels
ax.set_xlabel('Real Part', fontsize=12, fontweight='bold')
ax.set_ylabel('Imaginary Part', fontsize=12, fontweight='bold')
ax.set_title("De Moivre's Theorem: Powers of z = 1 + i", fontsize=14, fontweight='bold', pad=20)

# Base complex number: z = 1 + i
z_real, z_imag = 1, 1
r = np.sqrt(z_real**2 + z_imag**2)
phi = np.arctan2(z_imag, z_real)
phi_deg = np.degrees(phi)

# Colors for different powers
colors = ['red', 'blue', 'green', 'orange', 'purple']
powers = [1, 2, 3, 4, 5]

# Compute and plot powers
for n, color in zip(powers, colors):
    r_n = r ** n
    phi_n = n * phi
    z_n_real = r_n * np.cos(phi_n)
    z_n_imag = r_n * np.sin(phi_n)
    
    # Draw line from origin to power
    ax.plot([0, z_n_real], [0, z_n_imag], color=color, linewidth=2, alpha=0.7, label=f'$z^{n}$')
    ax.plot(z_n_real, z_n_imag, 'o', color=color, markersize=10)
    
    # Label the point
    ax.text(z_n_real + 0.1, z_n_imag + 0.1, f'$z^{n}$', fontsize=10, fontweight='bold', color=color)

# Annotate the base complex number
ax.text(z_real + 0.15, z_imag + 0.15, 'z', fontsize=12, fontweight='bold', color='red',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Add formula box
formula_text = (
    'De Moivre\'s Theorem:\n'
    r'$z^n = r^n(\cos(n\varphi) + i \sin(n\varphi))$' + '\n\n'
    f'For z = 1 + i:\n'
    f'r = {r:.3f}, φ = {phi_deg:.1f}°\n'
    f'z² = {r**2:.3f} (cos 90° + i sin 90°) = 2i\n'
    f'z³ = {r**3:.3f} (cos 135° + i sin 135°) = -2 + 2i'
)
ax.text(0.02, 0.98, formula_text, transform=ax.transAxes, fontsize=10, fontweight='bold',
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.9),
        family='monospace')

# Set ticks
ax.set_xticks([-2, -1, 0, 1, 2])
ax.set_yticks([-2, -1, 0, 1, 2])
ax.tick_params(labelsize=10)

# Legend
ax.legend(loc='lower right', fontsize=11, framealpha=0.95)

plt.tight_layout()
plt.savefig('demoivre-powers.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Generated: demoivre-powers.png")
plt.close()
