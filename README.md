# Musabaqat: AI Qur'an Recitation Judge

An intelligent judging system for Qur'an recitation competitions (Musabaqat al-Qur'an), featuring real-time audio evaluation, tajweed analysis, and fair scoring based on established competition standards.

## Features

- **Real-time Audio Evaluation** — Live recitation monitoring with instant error detection
- **Tajweed & Memorization Analysis** — Comprehensive scoring on Hifz, Tajweed, Articulation (Makharij), and Voice
- **100-Point Rubric** — Standardized scoring matching official Musabaqat competition criteria
- **Respectful & Encouraging Feedback** — Detailed, specific feedback on exact words/phrases
- **Multi-participant Sessions** — Support for competition rounds with multiple competitors
- **Reference Audio Library** — High-quality qari recordings for verse playback
- **Real-time Alerts** — Non-disruptive audio signals for live mistake detection
- **Scoring Dashboard** — View competition results, participant progress, and analytics

## Architecture

```
├── backend/              FastAPI server, judging engine, audio processing
├── frontend/             React UI for judges and participants
├── audio-processor/      Speech-to-text, tajweed detection, alignment
├── quranic-data/         Verse library, reference recordings, tajweed rules
├── docker-compose.yml    Container orchestration
└── docs/                 API specs, setup guides, architecture
```

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.10+
- Node.js 18+
- PostgreSQL 14+

### Development Setup

```bash
# Clone repository
git clone https://github.com/afissampore9-cpu/Mussabaqat-.git
cd Mussabaqat-

# Start services
docker-compose up

# Backend runs at http://localhost:8000
# Frontend runs at http://localhost:3000
```

### Environment Variables

Create `.env.local` in the root:

```
DATABASE_URL=postgresql://user:password@db:5432/musabaqat
RED_IS_API_KEY=your_api_key
JWT_SECRET=your_jwt_secret
AUDIO_UPLOAD_DIR=/data/uploads
```

## Project Structure

- **Backend** — FastAPI with async audio processing, real-time WebSocket scoring, PostgreSQL persistence
- **Frontend** — React + TypeScript, real-time score updates, audio recording/playback
- **Audio Processor** — Speech-to-text alignment, tajweed rule detection, word-level accuracy scoring
- **Qur'anic Database** — 114 surahs, verse mappings, tajweed annotations, reference recordings

## Scoring Rubric

| Category | Weight | Points |
|----------|--------|--------|
| Hifz (Memorization) | 40% | 40 |
| Tajweed (Recitation Rules) | 30% | 30 |
| Makharij al-Huruf (Articulation) | 20% | 20 |
| Voice & Fluency | 10% | 10 |
| **Total** | **100%** | **100** |

## API Overview

### Judge Operations
- `POST /api/competitions` — Create new competition
- `POST /api/rounds` — Start a competition round
- `POST /api/judge/evaluate` — Submit participant recitation for evaluation
- `GET /api/judge/results/{participant_id}` — View participant score history
- `WebSocket /ws/judge/{session_id}` — Real-time scoring updates

### Participant Operations
- `POST /api/participant/record` — Submit audio recording
- `GET /api/participant/verse` — Get verse to recite
- `GET /api/participant/results` — View personal scores

### Admin Operations
- `POST /api/admin/load-references` — Upload reference qari recordings
- `GET /api/admin/competitions` — Manage competitions
- `POST /api/admin/export-results` — Export final rankings

## Development

### Run Tests

```bash
cd backend && pytest
cd ../frontend && npm test
```

### Build for Production

```bash
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up -d
```

## Documentation

- [API Specification](./docs/API.md)
- [Architecture Guide](./docs/ARCHITECTURE.md)
- [Judging System Details](./docs/JUDGING.md)
- [Deployment Guide](./docs/DEPLOYMENT.md)
- [System Prompt](./musabaqat_judge_prompt.md)

## System Prompt

The AI judge operates under a comprehensive system prompt defining role, evaluation criteria, feedback format, and conduct rules. See [musabaqat_judge_prompt.md](./musabaqat_judge_prompt.md) for full details.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

MIT License

## Support

For issues, feature requests, or questions, open an issue on GitHub.
