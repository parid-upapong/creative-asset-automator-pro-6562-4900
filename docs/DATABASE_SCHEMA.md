# Database Schema Design: Project OVERLORD

## 1. Overview
The database for Project OVERLORD is designed using **PostgreSQL** to leverage its robust relational capabilities, JSONB support for dynamic AI metadata, and scalability. The schema focuses on high-performance asset retrieval and maintaining complex relationships between "Master Assets" and their AI-generated derivatives.

## 2. Core Modules
- **Identity & Access:** Users, Profiles, and Workspaces.
- **Brand Intelligence:** Brand Kits and Voice Profiles to ensure AI consistency.
- **Asset Management:** Master assets (source) and Technical metadata.
- **AI Processing:** Transcripts, AI-generated insights, and derived assets (clips/posts).
- **Task Tracking:** Status of background workers for video processing.

## 3. Key Design Decisions
- **UUIDs:** Used for all primary keys to ensure security and ease of migration/sharding.
- **JSONB for AI Metadata:** Since AI models evolve quickly, metadata (tags, sentiment, speaker identification) is stored in JSONB to allow schema-less flexibility within a structured environment.
- **Soft Deletes:** Implemented via `deleted_at` timestamps for data recovery and audit trails.

## 4. Entity Relationship Summary
- A `User` belongs to one or more `Workspaces`.
- A `Workspace` holds many `Assets`.
- A `Master Asset` has one `Technical Metadata` record and many `Derived Assets`.
- A `Brand Kit` is applied during the generation of `Derived Assets` to maintain consistency.