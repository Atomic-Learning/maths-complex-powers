#!/usr/bin/env python3
"""
Generate a diagram showing De Moivre's theorem: nth roots of a complex number.
Outputs to demoivre-roots.png in the same directory.
"""

import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig, ax = plt.subplots(1, 1, figsize=(10, 10), dpi=150)
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
ax.axhline(y=0, color='k', linewidth=1.5)
ax.axvline(x=0, color='k', linewidth=1.5)

# Add axis labels
ax.set_xlabel('Real Part', fontsize=12, fontweight='bold')
ax.set_ylabel('Imaginary Part', fontsize=12, fontweight='bold')
ax.set_title("De Moivre's Theorem: Fourth Roots of 1", fontsize=14, fontweight='bold', pad=20)

# Compute fourth roots of 1
z_real, z_imag = 1, 0
r = np.sqrt(z_real**2 + z_imag**2)  # r = 1
phi = np.arctan2(z_imag, z_real)    # phi = 0
n = 4

# Compute nth roots
r_root = r ** (1 / n)
roots_real = []
roots_imag = []
colors = ['red', 'blue', 'green', 'orange']

for k in range(n):
    phi_k = (phi + 2 * np.pi * k) / n
    root_real = r_root * np.cos(phi_k)
    root_imag = r_root * np.sin(phi_k)
    roots_real.append(root_real)
    roots_imag.append(root_imag)
    
    # Draw line from origin to root
    ax.plot([0, root_real], [0, root_imag], color=colors[k], linewidth=2.5, alpha=0.8)
    ax.plot(root_real, root_imag, 'o', color=colors[k], markersize=12)
    
    # Label the root
    offset = 1.25
    ax.text(offset * root_real, offset * root_imag, f'$w_{k}$', fontsize=11, fontweight='bold', 
            color=colors[k], ha='center', va='center',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Draw circle showing the roots
theta = np.linspace(0, 2*np.pi, 100)
circle_x = r_root * np.cos(theta)
circle_y = r_root * np.sin(theta)
ax.plot(circle_x, circle_y, 'k--', linewidth=1, alpha=0.3, label='All nth roots lie on this circle')

# Add formula box
formula_text = (
    'De Moivre\'s Theorem (Roots):\n'
    r'$w_k = r^{1/n}(\cos(\frac{\varphi + 2\pi k}{n}) + i \sin(\frac{\varphi + 2\pi k}{n}))$' + '\n'
    'where k = 0, 1, ..., n-1\n\n'
    'For the fourth roots of 1:\n'
    r'$w_0 = 1$' + '\n'
    r'$w_1 = i$' + '\n'
    r'$w_2 = -1$' + '\n'
    r'$w_3 = -i$'
)
ax.text(0.02, 0.98, formula_text, transform=ax.transAxes, fontsize=10, fontweight='bold',
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9),
        family='monospace')

# Set ticks
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.tick_params(labelsize=10)

# Legend
ax.legend(loc='lower right', fontsize=10, framealpha=0.95)

plt.tight_layout()
plt.savefig('demoivre-roots.png', dpi=150, bbox_inches='tight', facecolor='white')
print("Generated: demoivre-roots.png")
plt.close()
