# get_in

Access values in nested Python structures that respond to the `[]` indexing syntax.

Inspired by of Elixir's `get_in`. If you squint.

## Usage

For "soft" getting a value, use `get_in(collection, path)` where path is a list of keys/indices. This function optionally takes a `default` value to be returned if the final key/index is not found. The default defaults to `None`.

For "hard" getting a value, use `require_in(collection, path)` where path is a list of keys/indices. This function raises a `NestedValueNotFoundError` if the final key/index is not found.
