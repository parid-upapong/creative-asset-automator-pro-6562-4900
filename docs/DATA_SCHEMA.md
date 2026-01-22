# Core Data Schema (ERD Design)

## Users
- `id`: UUID (PK)
- `email`: String (Unique)
- `stripe_customer_id`: String
- `tier`: Enum (FREE, CREATOR, PRO)

## Assets (Master)
- `id`: UUID (PK)
- `user_id`: UUID (FK)
- `storage_path`: String (S3 Key)
- `mime_type`: String (video/mp4, audio/mpeg)
- `duration`: Float
- `status`: Enum (PENDING, READY, FAILED)

## Transcripts
- `id`: UUID (PK)
- `asset_id`: UUID (FK)
- `raw_text`: Text
- `segments`: JSONB (Timestamps, Speaker ID)

## Derived_Content (The Outputs)
- `id`: UUID (PK)
- `asset_id`: UUID (FK)
- `platform`: Enum (TIKTOK, INSTAGRAM, LINKEDIN, TWITTER)
- `content_type`: Enum (VIDEO_CLIP, TEXT_POST, IMAGE_CAROUSEL)
- `payload`: JSONB (Text content or S3 path to clip)
- `published_at`: Timestamp (Nullable)