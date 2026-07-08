# De Moivre's Theorem

**De Moivre's Theorem** is a powerful tool for computing integer powers and roots of complex numbers when they are expressed in polar form. It states that for a complex number in polar form and any integer $n$:

$$
[r(\cos \phi + i \sin \phi)]^n = r^n(\cos(n\phi) + i \sin(n\phi))
$$

In exponential notation, this becomes:

$$
(r e^{i\phi})^n = r^n e^{in\phi}
$$

# Why This Matters

Using De Moivre's theorem to compute powers of a complex number is far simpler than expanding them algebraically. For instance, computing $(1 + i)^{10}$ by repeated multiplication would be tedious, but using De Moivre's theorem:

$$
(1 + i)^{10} = \left(\sqrt{2} \left(\cos{\frac{\pi}{4}} + i \sin{\frac{\pi}{4}}\right)\right)^{10} = (\sqrt{2})^{10} \left(\cos{\frac{10\pi}{4}} + i \sin{\frac{10\pi}{4}}\right) = 32\left(\cos{\frac{5\pi}{2}} + i \sin{\frac{5\pi}{2}}\right) = 32i
$$

The theorem is particularly useful in applications such as electrical engineering (AC circuit analysis) and physics, where complex exponentials and powers appear frequently.
