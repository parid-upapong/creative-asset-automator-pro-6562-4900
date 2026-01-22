# The Asset Management Journey: From Raw to Omni-Channel

In Project OVERLORD, an "Asset" is not a static file; it is a dynamic entity that evolves.

## 1. Stage: Ingestion (The Raw State)
- **Input:** MP4, MOV, MP3, or URL.
- **Action:** Asset is hashed for uniqueness and moved to secure S3 storage.
- **Metadata:** Source type, Timestamp, Original Quality.

## 2. Stage: Enrichment (The Intelligent State)
- **AI Processing:**
    - **Transcription:** Text layer generated.
    - **Diarization:** Identifying who is speaking and when.
    - **Sentiment Mapping:** High-energy vs. Low-energy segments.
    - **OCR:** Recognizing text appearing on screen.
- **Result:** A "Smart Master" file enriched with searchable metadata.

## 3. Stage: Fragmentation (The Derived State)
- **Action:** The Master Asset is sliced into "Children Assets."
- **Logic:** AI identifies hooks, climax, and CTA (Call to Action).
- **Relational Mapping:** Each child asset maintains a link to the parent's timestamp for easy reference.

## 4. Stage: Optimization (The Brand-Ready State)
- **Application:** Applying the Brand Identity (from Workflow B).
- **Refinement:**
    - Aspect Ratio adjustment (9:16, 1:1, 16:9).
    - AI-generated captions (Dynamic & Styled).
    - B-roll insertion (Stock footage suggested by AI based on keywords).

## 5. Stage: Distribution (The Final State)
- **Status:** "Live" or "Scheduled."
- **Feedback Loop:** Performance metrics (Likes/Shares) are fed back into the IAM to rank which "Asset Types" perform best for the user, informing the next Ingestion cycle.

## 6. Stage: Archival
- Assets are compressed but remain searchable via the Semantic Index.