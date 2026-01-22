# Cloud Infrastructure Blueprint (AWS-Focused)

## 1. Global Content Delivery
- **Route 53:** DNS management.
- **CloudFront:** CDN to serve video assets globally with signed URLs for security.
- **WAF:** Web Application Firewall to prevent SQL injection and DDoS.

## 2. Compute Strategy
- **Frontend:** Vercel (for Next.js optimization).
- **Backend API:** AWS ECS (Fargate) - Serverless container execution for scaling the API based on traffic.
- **Heavy Workers:** AWS EC2 (G4dn instances) for local Whisper/FFmpeg processing, or Lambda (for lightweight triggers).

## 3. Storage & Database
- **Primary Data:** AWS RDS (Aurora PostgreSQL) with auto-scaling storage.
- **Asset Storage:** AWS S3 (Standard for active projects, Intelligent-Tiering for older assets).
- **Transient Data:** AWS ElastiCache (Redis) for fast task handoffs.

## 4. Networking & Security
- **VPC:** Private subnets for Database and Workers.
- **IAM:** Least-privilege roles for service-to-service communication.
- **Secrets Manager:** Handling API keys for OpenAI, Anthropic, and Stripe.

## 5. Monitoring & Observability
- **Sentry:** Error tracking for Frontend and Backend.
- **AWS CloudWatch:** Logging and infra metrics.
- **Datadog/New Relic:** Distributed tracing for AI pipeline latency.