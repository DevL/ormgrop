# Ormgrop ![Python package](https://github.com/DevL/ormgrop/workflows/Python%20package/badge.svg)

_DevL's own standard library for Python 3._

## Installation

```sh
pip install ormgrop
```

## Collections

`get_in` and `require_in`

Access values in nested Python structures that respond to the `[]` indexing syntax.

Inspired by of Elixir's `get_in`. If you squint.

### Usage

For "soft" getting a value, use `get_in(collection, path)` where path is a list of keys/indices. This function optionally takes a `default` value to be returned if the final key/index is not found. By default this is `None`.

For "hard" getting a value, use `require_in(collection, path)` where path is a list of keys/indices. This function raises a `NestedValueNotFoundError` if the final key/index is not found.

## Debug

`measure` is a function that given a log function, e.g. `logger.debug` returns a decorator that can be used to measure and log the execution time of another function.

### Usage

Create a measure decorator by calling `measure` with a logging function, e.g. `measure(logger.debug)`. By default this will be `logger.debug`.

## Development

To run the tests, ensure that you have installed [pytest-describe](https://pypi.org/project/pytest-describe) and run `pytest`.
