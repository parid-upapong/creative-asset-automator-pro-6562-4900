-- Project OVERLORD: Database Schema
-- Database: PostgreSQL 15+

-- Extension for UUID generation
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. IDENTITY & WORKSPACES
CREATE TABLE workspaces (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    full_name VARCHAR(255),
    avatar_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);

CREATE TABLE workspace_members (
    workspace_id UUID REFERENCES workspaces(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    role VARCHAR(50) DEFAULT 'member', -- owner, admin, member
    PRIMARY KEY (workspace_id, user_id)
);

-- 2. BRAND & PREFERENCES
CREATE TABLE brand_kits (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    workspace_id UUID REFERENCES workspaces(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    brand_voice_description TEXT,
    keywords TEXT[],
    primary_color VARCHAR(7), -- Hex code
    font_family VARCHAR(100),
    logo_url TEXT,
    is_default BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. ASSET MANAGEMENT (MASTER ASSETS)
CREATE TYPE asset_status AS ENUM ('uploading', 'processing', 'ready', 'failed');
CREATE TYPE asset_type AS ENUM ('video', 'audio', 'document');

CREATE TABLE master_assets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    workspace_id UUID REFERENCES workspaces(id) ON DELETE CASCADE,
    creator_id UUID REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    file_path TEXT NOT NULL, -- S3 Bucket Path/Key
    source_url TEXT,         -- Original YouTube/Drive link if applicable
    asset_type asset_type NOT NULL,
    status asset_status DEFAULT 'uploading',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE
);

CREATE TABLE asset_metadata (
    asset_id UUID PRIMARY KEY REFERENCES master_assets(id) ON DELETE CASCADE,
    duration_seconds DECIMAL,
    file_size_bytes BIGINT,
    mime_type VARCHAR(100),
    resolution_width INTEGER,
    resolution_height INTEGER,
    frame_rate DECIMAL,
    bitrate INTEGER,
    raw_ffprobe_data JSONB -- Full technical dump
);

-- 4. AI INTELLIGENCE & DERIVATIVES
CREATE TABLE transcripts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    asset_id UUID REFERENCES master_assets(id) ON DELETE CASCADE,
    language_code VARCHAR(10) DEFAULT 'en',
    raw_text TEXT NOT NULL,
    segments JSONB NOT NULL, -- Timestamped words/sentences
    confidence_score DECIMAL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ai_insights (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    asset_id UUID REFERENCES master_assets(id) ON DELETE CASCADE,
    summary TEXT,
    suggested_tags TEXT[],
    key_topics JSONB, -- AI identified themes
    sentiment_analysis JSONB,
    brand_alignment_score DECIMAL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE derived_assets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    master_asset_id UUID REFERENCES master_assets(id) ON DELETE CASCADE,
    brand_kit_id UUID REFERENCES brand_kits(id),
    title VARCHAR(255),
    content_type VARCHAR(50), -- 'tiktok_video', 'linkedin_post', 'newsletter'
    output_text TEXT,
    output_file_path TEXT,    -- S3 path for video/image snippets
    platform_target VARCHAR(50),
    status asset_status DEFAULT 'processing',
    ai_metadata JSONB,        -- Prompts used, specific model versions
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. INDEXING FOR PERFORMANCE
CREATE INDEX idx_master_assets_workspace ON master_assets(workspace_id);
CREATE INDEX idx_derived_assets_master ON derived_assets(master_asset_id);
CREATE INDEX idx_transcripts_asset ON transcripts(asset_id);