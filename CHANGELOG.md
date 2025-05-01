# CHANGELOG

## [v0.0.1] - 2024-04-12
### Added
- Project structure and base modules
- Initial README and documentation

## [v0.0.2] - 2024-04-29
### Added
- Basic alembic config for DB migrations
- Initial models and schemas for User info

## [v0.0.3] - 2024-04-30
### Added
- POST/user endpoint logic
- password hashing and verification in utils/security.py
- Role lookup helper function in utils/db_helpers.py
### Changed
- UserResponse (schema): update "orm_mode" with newer syntax

## [v0.0.4] - 2024-05-01
### Added
- GET/user endpoint logic
- PUT/user/{id} endpoint logic
- Object finder by id function in utils/db_helpers.py