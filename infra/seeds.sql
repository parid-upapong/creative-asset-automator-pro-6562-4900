-- Initial Seed Data for Project OVERLORD Development

-- 1. Create a User
INSERT INTO users (id, email, full_name)
VALUES ('00000000-0000-0000-0000-000000000001', 'creator@example.com', 'Alex Creator');

-- 2. Create a Workspace
INSERT INTO workspaces (id, name, slug)
VALUES ('11111111-1111-1111-1111-111111111111', 'Alex Studio', 'alex-studio');

-- 3. Link User to Workspace
INSERT INTO workspace_members (workspace_id, user_id, role)
VALUES ('11111111-1111-1111-1111-111111111111', '00000000-0000-0000-0000-000000000001', 'owner');

-- 4. Create a Brand Kit
INSERT INTO brand_kits (workspace_id, name, brand_voice_description, primary_color)
VALUES (
    '11111111-1111-1111-1111-111111111111', 
    'Main Brand', 
    'Informative, witty, and high-energy tech content.', 
    '#FF5733'
);

-- 5. Insert a Sample Master Asset
INSERT INTO master_assets (id, workspace_id, creator_id, title, file_path, asset_type, status)
VALUES (
    '22222222-2222-2222-2222-222222222222',
    '11111111-1111-1111-1111-111111111111',
    '00000000-0000-0000-0000-000000000001',
    'How AI Changes Creativity.mp4',
    'uploads/1111/master/ai_changes.mp4',
    'video',
    'ready'
);

-- 6. Insert Asset Metadata
INSERT INTO asset_metadata (asset_id, duration_seconds, file_size_bytes, mime_type, resolution_width, resolution_height)
VALUES (
    '22222222-2222-2222-2222-222222222222',
    600.5,
    524288000,
    'video/mp4',
    1920,
    1080
);