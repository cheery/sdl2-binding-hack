These are not working bindings.

I tried to create bindings generator that generates python bindings that are isomorphic to the C headers, with outermost namespace prefix removed. This proved to be difficult.

Fortunately there are official python bindings so I do not need to get this working but without a language binding specification there will be problems to use libsdl2 from other languages.

A nice discovery I made is that libclang is just half the solution to binding against C libraries. Better solution is required.

## Ideas for Language Binding Specification

Define parsing expression grammar or ANTLR for something that's fairly easy to modify. This way the standard semantics for specification can be varied if required. Also it won't look like shit as what XML binding specs do.

Minimum needs:

 * Function signatures.
 * Type signatures. Things such as `typedef float Float;`.
 * Structures and Unions, nested and anonymous as well.
 * Macro constants.
 * Simple macro definitions and inlined functions.

Produce generator which translates the binding specification to the C headers and python bindings. Alternatively make the programming languages
itself understand the binding specification and generate structures from it.
