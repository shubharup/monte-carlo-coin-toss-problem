Let $X$ denote the number of heads and $Y$ denote the points scored.

Then we have to calculate the probability: 

$$P(X<3, Y \le 1)$$

$X < 3$ $ \implies$ $X$ can take three values: $0$ (no heads), $1$ (1 head) and $2$ (2 heads).

$Y \le 1$ $ \implies$ Y can take two values: $1$ and $-1$. 

In total, there are $6 \hspace{1.5pt} X,Y$ pairs $(3 \times 2)$ which satisfy the given criteria, and over which we sum probability (in other words, we sum the probability mass assigned to each $X,Y$ pair).


$$P(X<3, Y \le 1) = P(0,-1) + P(1,-1) + P(2,-1) + P(0,1) + P(1,1) + P(2,1)$$ 

It is easily seen that $P(1,-1) = P(2,-1) = 0$; if there were one or more Heads, the score will be $1$, $2$ or $3$, but never $-1$.

Likewise, $P(0,1) = 0$; if there were no heads, the score would be $-1$.

Eliminating the zero terms, the probability expression is reduced to:

$$P(X<3, Y \le 1) = P(0,-1) + P(1,1) + P(2,1)$$ 


Note that $X \sim Binomial(3, \frac{1}{2})$.

So $P(X = k) =$ $3 \choose k$ $( \frac{1}{2})^{k}$ $(1 - \frac{1}{2})^{3 - k}$ $=$ $3 \choose k$ $(\frac{1}{2})^{3}$

1. $P(0,-1)$ $= P(X = 0)$ $\times P(Y = -1 | X = 0)$ $=$ $3 \choose 0$ $(\frac{1}{2})^{3}$ $ \times 1$ $= \frac{1}{8}$ 

2. $P(1,1)$ $= P(X = 1)$ $\times P(Y = 1 | X = 1) =$ $3 \choose 1$ $(\frac{1}{2})^{3}$ $\times$ $\frac{1}{3 \choose 1}$ $ = \frac{1}{8}$

3. $P(2,1)$ $= P(X = 2)$ $\times P(Y = 1 | X = 2) =$ $3 \choose 2$ $(\frac{1}{2})^{3}$ $\times$ $\frac{2}{3 \choose 2}$ $ = 2 \times \frac{1}{8}$

$$ \implies P(X<3, Y \le 1) = 0.5$$


This is the theoretically calculated probability we will check against.