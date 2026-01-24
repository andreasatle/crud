# CRUD Address Book — Help Document

## Purpose

This document defines the **public API surface** and **intended behavior** of a simple
address book system.

It exists to:

* bound the problem space
* make requests and responses explicit
* serve as input for deriving invariants

This document is **descriptive**, not enforceable.
Only tests enforce behavior.

---

## Domain Model

### Person

A `Person` represents an individual in the address book.

Minimal properties:

* `person_id` — opaque, system-generated identifier

Additional fields (initial version):

* `name` — string
* `email` — string

No assumptions are made about validation beyond basic structural correctness.

---

### Address

An `Address` represents a physical or logical address.

Minimal properties:

* `address_id` — opaque, system-generated identifier
* `person_id` — identifier of owning `Person`

Additional fields (initial version):

* `street`
* `city`
* `postal_code`
* `country`

Each `Address` belongs to **exactly one** `Person`.

---

## Relationships

* A `Person` may have zero or more `Address` entries
* An `Address` belongs to exactly one `Person`
* Ownership of an `Address` never changes
* Deleting a `Person` deletes all owned `Address` entries

---

## API Entrypoints

All entrypoints are synchronous function calls.

No entrypoint implies a workflow.

---

### create_person

**Request**

```
{
  name: string,
  email: string
}
```

**Response**

```
{
  person_id: string
}
```

**Behavior**

* Creates a new `Person`
* Generates a fresh, opaque `person_id`
* Persists the new person
* Returns the identifier

---

### read_person

**Request**

```
{
  person_id: string
}
```

**Response**

```
{
  person_id: string,
  name: string,
  email: string
}
```

**Behavior**

* Returns the persisted state of the person
* Fails if the identifier does not exist

---

### update_person

**Request**

```
{
  person_id: string,
  name?: string,
  email?: string
}
```

**Response**

```
{
  person_id: string
}
```

**Behavior**

* Updates the specified fields of the person
* Does not change the identifier
* Fails if the identifier does not exist

---

### delete_person

**Request**

```
{
  person_id: string
}
```

**Response**

```
{
  deleted: boolean
}
```

**Behavior**

* Deletes the person
* Deletes all addresses owned by the person
* Operation is atomic

---

### create_address

**Request**

```
{
  person_id: string,
  street: string,
  city: string,
  postal_code: string,
  country: string
}
```

**Response**

```
{
  address_id: string
}
```

**Behavior**

* Creates a new address owned by the specified person
* Fails if the person does not exist
* Persists the address

---

### read_address

**Request**

```
{
  address_id: string
}
```

**Response**

```
{
  address_id: string,
  person_id: string,
  street: string,
  city: string,
  postal_code: string,
  country: string
}
```

**Behavior**

* Returns the persisted address
* Fails if the identifier does not exist

---

### update_address

**Request**

```
{
  address_id: string,
  street?: string,
  city?: string,
  postal_code?: string,
  country?: string
}
```

**Response**

```
{
  address_id: string
}
```

**Behavior**

* Updates address fields
* Does not change ownership
* Fails if the identifier does not exist

---

### delete_address

**Request**

```
{
  address_id: string
}
```

**Response**

```
{
  deleted: boolean
}
```

**Behavior**

* Deletes the address
* Does not affect the owning person

---

### list_people

**Request**

```
{}
```

**Response**

```
[
  {
    person_id: string,
    name: string,
    email: string
  }
]
```

**Behavior**

* Returns all persisted persons
* Order is unspecified

---

### list_addresses_for_person

**Request**

```
{
  person_id: string
}
```

**Response**

```
[
  {
    address_id: string,
    street: string,
    city: string,
    postal_code: string,
    country: string
  }
]
```

**Behavior**

* Returns all addresses owned by the person
* Fails if the person does not exist

---

## Global Behavioral Notes

* Identifiers are opaque strings
* Identifiers are system-generated
* Failed operations do not partially mutate state
* Read and list operations do not mutate state

---

## Out of Scope

This document intentionally does **not** define:

* persistence mechanism
* concurrency behavior
* transaction isolation
* validation rules (beyond existence)
* error formats
* performance characteristics
* authorization
* UI concerns

---

## Status

This help document is **input material**.

It exists to support:

* invariant discovery
* test design
* scoped implementation

It is not authoritative.
