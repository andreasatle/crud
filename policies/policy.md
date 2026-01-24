## POLICY-P01 — Entity Naming and Role Disambiguation

### Purpose

To prevent semantic ambiguity and hidden coupling caused by reused names with different meanings.

This policy ensures that **entity meaning is always clear from import context and module location**, and that no module contains conflicting interpretations of the same name.

### Rules

1. **Entity names MAY repeat across modules.**

   * The same name (e.g. `Person`) may exist in multiple modules.
   * Meaning is defined by **where the entity is imported from**, not by the name alone.

2. **Entity names MUST NOT repeat within a single module or namespace.**

   * A module MUST NOT define or import two entities with the same name that have different meanings.
   * Aliasing to hide ambiguity (e.g. `Person as DbPerson`) does NOT remove the violation.

3. **Each entity name MUST have exactly one semantic meaning per module.**

   * Within a module, an entity name must map to one and only one conceptual role.

### Rationale

* Reusing names across modules is often necessary and natural.
* Reusing names **within** a module creates ambiguity that:

  * obscures intent
  * complicates reasoning
  * defeats review and validation
* Import context is a reliable and inspectable source of meaning.
* Enforcing one meaning per module keeps code readable and invariant-friendly.

## POLICY-P02 — Boundary vs Domain Modeling

### Purpose
To separate untrusted I/O concerns from authoritative domain and persistence concerns.

### Rules

1. **All API input and output models MUST be defined using Pydantic.**

   * This includes request and response payloads.
   * Pydantic is used for validation, parsing, and schema enforcement at boundaries.

2. **All persisted or domain entities MUST NOT depend on Pydantic.**

   * Domain and persistence models MUST be plain Python (`dataclass` or equivalent).
   * No Pydantic base classes, validators, or field coercion are allowed in domain models.

3. **Conversion between I/O models and domain models MUST be explicit.**

   * Mapping logic must be visible in code.
   * No implicit or magical conversion is allowed.

4. **Invariants apply to domain models, not to I/O models.**

   * I/O models may be partial, permissive, or evolving.
   * Domain models represent authoritative system state.

### Rationale

* Pydantic is optimized for **untrusted data at boundaries**.
* Domain and persistence logic require **predictability and explicit control**.
* Separating the two prevents hidden validation, coercion, and authority inversion.


## POLICY-P03 — No Global Mutable State

### Purpose
To prevent hidden coupling, non-determinism, and authority leakage through module-level state.

### Rules

1. **No mutable global state is allowed.**

   * Module-level variables MUST NOT store application state.
   * This includes caches, singletons, or “initialized once” state.

2. **All state access MUST be explicit per operation.**

   * Each entrypoint call must load required state explicitly.
   * Each mutation must write state explicitly.

3. **Persistence handles MUST NOT be stored globally.**

   * File handles, database connections, sessions, or repositories must be created or acquired explicitly.
   * Passing handles through function arguments or local scope is allowed.

4. **Pure helper functions MAY exist.**

   * Functions without side effects and without state retention are allowed at module level.

### Rationale

* Global state hides dependencies.
* Global state breaks test isolation.
* Global state makes invariants unverifiable.
* Explicit state access keeps behavior inspectable and repairable.


## POLICY-P04 — Object-Oriented Structure Preference

### Purpose
To improve readability, locality of reasoning, and maintainability by favoring object-oriented structure.

### Rules

1. **Core domain and persistence logic SHOULD be structured using classes.**

   * State, behavior, and invariants should be colocated where reasonable.
   * Classes are preferred over free functions for non-trivial logic.

2. **Classes SHOULD encapsulate their internal state.**

   * Internal details MUST NOT be mutated from outside the class except through defined methods.
   * Public methods define the unit of behavior.

3. **Free functions are allowed for:**

   * pure transformations
   * stateless helpers
   * orchestration / wiring code
   * trivial logic

4. **Object boundaries MUST remain explicit.**

   * No hidden global state.
   * No implicit singletons.
   * Object construction must be visible in code.

5. **OOP is a structural preference, not a correctness requirement.**

   * Violating this policy is a design issue, not a functional bug.
   * It may trigger refactoring tasks, not invariant failures.

### Rationale

* Classes improve locality of reasoning.
* Encapsulation reduces cognitive load.
* OOP makes large systems easier to navigate than flat module-level logic.
* Explicit object lifetimes preserve testability and determinism.

## POLICY-P05 — SQL-Based Persistence with ORM

### Purpose  
To fix the persistence technology and access pattern in order to prevent architectural drift and hidden coupling.

### Rules

1. **Persistent storage MUST use a SQL database.**
   * The concrete database engine (e.g. MySQL, PostgreSQL) is fixed per project configuration.

2. **Persistence MUST be implemented using an ORM.**
   * SQLAlchemy is the approved ORM.
   * Raw SQL execution is forbidden.

3. **All persisted entities MUST be represented as ORM-mapped classes.**
   * Table schemas are defined exclusively through ORM mappings.

4. **ORM usage MUST be isolated to the persistence layer.**
   * Domain logic MUST NOT import or depend on ORM-specific APIs.
   * ORM objects MUST NOT leak across module boundaries.

5. **Session and transaction scope MUST be explicit.**
   * ORM sessions MUST be created, used, and disposed per operation.
   * No global or long-lived sessions are allowed.

### Rationale

* Fixes the storage model early to avoid repeated rework.
* Prevents hidden data access paths.
* Keeps persistence decisions inspectable and replaceable.
* Preserves invariant authority while constraining implementation freedom.


## POLICY-P06 — Domain ↔ Persistence Mapping

### Purpose

To define how authoritative domain entities are persisted without leaking persistence concerns into domain logic.

### Rules

1. **Domain entities MUST be persistence-agnostic.**

   * Domain entities MUST NOT contain ORM annotations, base classes, or metadata.
   * Domain entities MUST NOT depend on SQLAlchemy or database concepts.

2. **Persistence entities MUST be ORM-mapped classes.**

   * ORM-mapped classes define tables, columns, keys, and relationships.
   * Persistence entities MAY differ structurally from domain entities.

3. **Mapping between domain and persistence entities MUST be explicit.**

   * Conversion logic MUST be implemented in a dedicated mapping layer.
   * No implicit ORM magic (e.g. automatic session-bound mutation) is allowed.

4. **Domain entities define identity; persistence assigns storage keys.**

   * Domain entities MAY contain stable identifiers.
   * Persistence-layer identifiers MUST map to domain identity explicitly.

5. **Invariants apply to domain entities, not ORM entities.**

   * ORM entities are storage artifacts.
   * Domain entities remain the source of truth.

### Rationale

* Prevents ORM leakage into domain logic.
* Allows persistence strategy changes without rewriting invariants.
* Makes identity, ownership, and lifecycle explicit.
* Preserves your “invariants are authority” principle.
