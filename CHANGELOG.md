1.0.0 (2021-04-20)
==================

### :sparkles: Added

- Added IAM User assertions: `has.name`, `was.created_at`, `belongs_to.group`
- Added IAM Policy assertions: `has.name`, `has.description`, `was.created_at`, `was.last_updated_at`, `should_be.attached_to`
- Added IAM Group assertions: `has.name`, `was.created_at`, `should.contain`, `has.policy`
- Added IAM Role assertions: `has.name`, `has.description`, `was.created_at`, `was.last_used_on`, `uses.policy`
- Added SNS Topic assertions: `should.receive`

### :pencil2: Changed

- `s3.Bucket.should.contain()` now accepts `s3.Object` as an alternative to a `str` key
- Assertions now `assert` themselves rather than returning a `bool`
- Added better `AssertionError` messages


0.0.13 (2021-04-10)
-------------------

### :pencil2: Changed

- Awssert now works with moto decorators

### :books: Documentation

- README now shows moto decorator usage


0.0.7 (2021-04-07)
------------------

### :books: Documentation

- Added CONTRIBUTING guide


0.0.6 (2021-04-06)
------------------

### :books: Documentation

- Added Progress table to README


0.0.5 (2021-04-06)
------------------

### :pencil2: Changed

- Main functionality is now provided through a pytest plugin rather than a fixture

### :books: Documentation

- Updated README with pytest plugin usage


0.0.4 (2021-04-05)
------------------

### :sparkles: Added

- Added Changelog
