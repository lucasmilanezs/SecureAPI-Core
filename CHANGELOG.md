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

## [v0.0.5] - 08/05/2025
### Added
- Endpoint `DELETE /user/{user_id}` implementing soft delete logic via `is_deleted` flag.
- Row-Level Security (RLS) policy on `users` table to restrict access to rows where `is_deleted = false`, applied via Alembic migration.
### Changed
- `User` ORM model updated: added `is_deleted: bool` column to support soft delete.