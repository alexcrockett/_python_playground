# Building a basic function in Maple

1. [Writing functions](#writing-functions)
2. [Plugging expressions into equations](#plugging-expressions-into-equations)

## Writing functions

Creating a function in Maple is not difficult.

To create a simple function, let's say $x^2$ you simple need to write:

```
f:=x^2;
```

The semi-colon is important. It tells Maple you have completed the command. You could use a colon, but this will suppress the output.

So for example the following are valid:

```
f:=x^2;
f:=x^2:
```

Let us now say we want to create a single variable function. Let us say out function will be $f(x)=x^3*x+50x$

We want to tell Maple that we are creating a function $f$ of $x$ such that $f(x)=x^3*x+50x$. We will therefore write:

```
f:=x->x^3*x+50*x;
```

Notice that we have included `*` where we are multiplying. It is easy to forget to do this and Maple will tell you an operator is missing.

For example if we write:

```
f:=x->x^3x+50x;
```

We have Maple return:

```
Error, missing operator or `;`
```

We can also tell Maple to change our variable. For example if we write:

```
f(z);
```

We will now get:

$z^4 + 50*z$

In return, which can be understood as asking Maple to take f of z.

## Plugging expressions into equations

It is also possible to plug expressions into variables in functions written in Maple using the `subs` command.

For example given the expression

```
f:=x^3*x+50*x;
```

Notice here we did not write `f:=x->` and instead only wrote `f:=`.

We can later write:

```
subs(x=y+z, f);
```

Where we tell Maple what is being substituted in and which function we are substituting in to. This will produce the following output:

```
(y + z)^4 + 50*y + 50*z
```
