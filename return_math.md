
# Computing returns

Our time unity will be days.

Let's design the following evolving equation, with total liquidation value $v(t)$, return at day $t$ $r(t)$, and cash flow $f(t)$ (can be negative). Then:

$$v(t+1) = (v(t) + f(t)) (1 + r(t))$$

The objective is to find $r(t)$ for all $t$ and then compute the annual return. This can be done directly from the above equation:

$$r(t) = \frac{v(t+1) - (v(t) + f(t))}{v(t) + f(t)} = \frac{v(t+1)}{v(t) + f(t)}-1$$

However, if we did not have access to all the $v(t)$ but only had access to the last one, we can do the following. Let's say we have two cash inflows $f(t_1), f(t_2)$, and $f(t) = 0 \;\forall t \not\in \{t_1, t_2\} $ with $t_1 < t_2$. Then we have 

$$v(t_2+\Delta t) = (v(t_2) + f(t_2)) \times (1 + r(t_2))^{\Delta t}$$

which assumes that the daily return from $t_2$ to $t_2 + \Delta t$ was constant. If the final time is $T$ and $\Delta t = T - t_2$:

$$ r(t_2) = \sqrt[\Delta t]{\frac{v(T)}{v(t_2) + f(t_2)} } - 1$$

The full toy problem can not be solved without the values $v(t_1)$ and $v(t_2)$. Luckily we can download this using the button `Export History` on the ameritrade webpage.

With the history, we can compute the daily returns from the beginning by solving the previous equation.

### Solution
In practice, we have the balance history containing a list of `dates`, with subtleties e.g. no weekends, and a list of transactions with `t_dates`, which are few. Both lists have associated amounts. For a given $t$ in `t_dates`, we have that the `t_amounts[t]` (being `[t]` the adequate index) is what we called $f(t)$ above. However, we must update the formula because now the amount `amounts[t]` already includes the cash flow: $v(t) = f(t) + v(t-1)(1 + r(t-1))$.

Then:
$$ \frac{v(t) - f(t)}{v(t-1)} - 1  = r(t-1) $$

In the long term approach without intermediate cashflows:

$$v(t + \Delta t) = v(t) (1 + r(\hat{t}))^{\Delta t}$$

with $r(\hat{t})$ being the estimated daily return for any $\hat{t} \in [t, t + \Delta t)$.

With $n$ cashflows at times $\{t_1 < \dots < t_n\}$:

$$ r(\hat{t}) = \sqrt[\Delta t]{\frac{v(t_1)-f(t_1)}{v(t_s)}}-1 \; \forall \hat{t} \in [t_s, t_1)$$
$$ r(\hat{t}) =\sqrt[\Delta t]{ \frac{v(t_2)-f(t_2)}{v(t_1)}}-1 \; \forall \hat{t} \in [t_1, t_2)$$
$$\dots$$
$$ r(\hat{t}) =\sqrt[\Delta t]{ \frac{v(t_n)-f(t_n)}{v(t_{n-1})}}-1 \; \forall \hat{t} \in [t_{n-1}, t_n)$$
$$ r(\hat{t}) =\sqrt[\Delta t]{ \frac{v(T)}{v(t_{n})}}-1 \; \forall \hat{t} \in [t_n, T)$$

and if we assume $v(t_s)=0$ and that $f(t_1)$ is actually the first funding of the account we can just start from the second equation.

### Computing more numbers

One we have the daily rate $r_d$ between periods we can compute the annual rate $r_a$ as

$$r_a = [(1 + r_d)^{365} - 1] (\times 100)$$ 

the absolute rate $R$ defined as

$$ R = \frac{v(t_f) - f(t_f)}{v(t_i)} - 1 $$

and the total daily rate is the geometric mean of the (1+) rates:

$$ r_a = \sqrt[\Delta t_1 + \Delta t_2 + \dots]{(1+r_{d_1})^{\Delta t_1}(1+r_{d_2})^{\Delta t_2}\dots} -1$$





