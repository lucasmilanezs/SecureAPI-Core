# CHANGELOG

## [v0.0.1] - 2024-04-12
### Added
- Project structure and base modules
- Initial README and documentation

## [v0.0.2] - 2024-29-12
- Added basic alembic config for DB migrations
- Initial models and schemas for User info


## [v0.0.3] - 2024-30-12

### Added
- POST/user endpoint logic
- password hashing and verification in utils/security.py
- Role lookup helper function in utils/db_helpers.py

### Changed
- UserResponse (schema): update "orm_mode" with newer syntax