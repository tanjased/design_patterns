Some objects are simple and can be created in a single initializer call. Other objects are required to be created in  stages and it takes a lot of time. Having an object with many different initializer args isn't very productive. 

So to avoid a massive call to an initilizer we go for piecewise construction.

**_BUILDER_** - when piecewise object construction is complicated, provide an API to do it succinctly. 

The Builder is required when you have a complcated construction of objects.
